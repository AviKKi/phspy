from __future__ import annotations


from typing import Any, Dict, List, Optional
from graphql.language import OperationType
import hashlib
from crawler.test_query import test_query, test_hash, test_with_typenames, test_with_typenames_stripped


from graphql.language import (
    # core node types
    DocumentNode, OperationDefinitionNode, SelectionSetNode, FieldNode, NameNode,
    ArgumentNode, VariableNode, VariableDefinitionNode, DirectiveNode,
    FragmentDefinitionNode, FragmentSpreadNode, InlineFragmentNode, SelectionNode,
    # type nodes
    NamedTypeNode, NonNullTypeNode, ListTypeNode,
    # value nodes
    StringValueNode, IntValueNode, FloatValueNode, BooleanValueNode, EnumValueNode,
    NullValueNode, ListValueNode, ObjectValueNode, ObjectFieldNode,
)
from graphql.language.printer import print_ast
from graphql.utilities import strip_ignored_characters


# ---------- JSON AST -> Python AST converter ----------

def _name(n: Dict[str, Any]) -> NameNode:
    # JSON AST typically: {"kind":"Name","value":"foo"}
    return NameNode(value=n["value"])

def _maybe(v, f):
    return None if v is None else f(v)

def _maybe_list(xs, f):
    if xs is None:
        return None
    return tuple(f(x) for x in xs)  # graphql-core prefers tuples

def _value(node: Dict[str, Any]):
    kind = node["kind"]
    if kind == "StringValue":
        return StringValueNode(value=node.get("value", ""), block=node.get("block", False))
    if kind == "IntValue":
        return IntValueNode(value=node["value"])
    if kind == "FloatValue":
        return FloatValueNode(value=node["value"])
    if kind == "BooleanValue":
        # In GraphQL-JS JSON, "value" is a boolean
        return BooleanValueNode(value=bool(node["value"]))
    if kind == "EnumValue":
        return EnumValueNode(value=node["value"])
    if kind == "NullValue":
        return NullValueNode()
    if kind == "ListValue":
        return ListValueNode(values=tuple(_value(v) for v in node.get("values", [])))
    if kind == "ObjectValue":
        return ObjectValueNode(
            fields=tuple(
                ObjectFieldNode(
                    name=_name(f["name"]),
                    value=_value(f["value"]),
                )
                for f in node.get("fields", [])
            )
        )
    # Variables are also "values" in many contexts
    if kind == "Variable":
        return VariableNode(name=_name(node["name"]))
    raise ValueError(f"Unsupported value kind: {kind}")

def _type(node: Dict[str, Any]):
    kind = node["kind"]
    if kind == "NamedType":
        return NamedTypeNode(name=_name(node["name"]))
    if kind == "NonNullType":
        return NonNullTypeNode(type=_type(node["type"]))
    if kind == "ListType":
        return ListTypeNode(type=_type(node["type"]))
    raise ValueError(f"Unsupported type kind: {kind}")

def _arguments(args_json: Optional[List[Dict[str, Any]]]):
    return _maybe_list(args_json, lambda a: ArgumentNode(name=_name(a["name"]), value=_value(a["value"])))

def _directives(dirs_json: Optional[List[Dict[str, Any]]]):
    return _maybe_list(dirs_json, lambda d: DirectiveNode(
        name=_name(d["name"]),
        arguments=_arguments(d.get("arguments")),
    ))

def _selection(sel: Dict[str, Any]):
    kind = sel["kind"]
    if kind == "Field":
        return FieldNode(
            alias=_maybe(sel.get("alias"), _name),
            name=_name(sel["name"]),
            arguments=_arguments(sel.get("arguments")),
            directives=_directives(sel.get("directives")),
            selection_set=_maybe(sel.get("selectionSet"), _selection_set),
        )
    if kind == "FragmentSpread":
        return FragmentSpreadNode(
            name=_name(sel["name"]),
            directives=_directives(sel.get("directives")),
        )
    if kind == "InlineFragment":
        return InlineFragmentNode(
            type_condition=_maybe(sel.get("typeCondition"), _type),
            directives=_directives(sel.get("directives")),
            selection_set=_selection_set(sel["selectionSet"]),
        )
    raise ValueError(f"Unsupported selection kind: {kind}")

def _selection_set(ss: Dict[str, Any]):
    return SelectionSetNode(selections=tuple(_selection(s) for s in ss.get("selections", [])))

def _variable_definitions(vdefs: Optional[List[Dict[str, Any]]]):
    return _maybe_list(
        vdefs,
        lambda vd: VariableDefinitionNode(
            variable=VariableNode(name=_name(vd["variable"]["name"])),
            type=_type(vd["type"]),
            default_value=_maybe(vd.get("defaultValue"), _value),
            directives=_directives(vd.get("directives")),
        ),
    )

def _operation_def(op: Dict[str, Any]):
    # GraphQL-JS JSON gives: op["operation"] == "query" | "mutation" | "subscription"
    op_str = op["operation"]
    if isinstance(op_str, str):
        # be tolerant of accidental uppercase etc.
        op_enum = OperationType(op_str.lower())
    else:
        # already an enum (or validated elsewhere)
        op_enum = op_str

    return OperationDefinitionNode(
        operation=op_enum,
        name=_maybe(op.get("name"), _name),
        variable_definitions=_variable_definitions(op.get("variableDefinitions")),
        directives=_directives(op.get("directives")),
        selection_set=_selection_set(op["selectionSet"]),
    )


def _fragment_def(fd: Dict[str, Any]):
    return FragmentDefinitionNode(
        name=_name(fd["name"]),
        type_condition=_type(fd["typeCondition"]),
        directives=_directives(fd.get("directives")),
        selection_set=_selection_set(fd["selectionSet"]),
    )

def _definition(defn: Dict[str, Any]):
    kind = defn["kind"]
    if kind == "OperationDefinition":
        return _operation_def(defn)
    if kind == "FragmentDefinition":
        return _fragment_def(defn)
    raise ValueError(f"Unsupported definition kind: {kind}")

def document_from_json(ast_json: Dict[str, Any]) -> DocumentNode:
    # Expect the JS-style AST root: {"kind":"Document","definitions":[...]}
    if ast_json.get("kind") != "Document":
        raise ValueError("Root must have kind='Document'")
    return DocumentNode(definitions=tuple(_definition(d) for d in ast_json.get("definitions", [])))


# ---------- Apollo-style __typename injection ----------

_TYPENAME_FIELD = FieldNode(name=NameNode(value="__typename"))

def _has_typename(ss: SelectionSetNode) -> bool:
    return any(isinstance(s, FieldNode) and s.name.value == "__typename" for s in ss.selections)

def _transform_selection(sel: SelectionNode) -> SelectionNode:
    if isinstance(sel, FieldNode):
        if sel.selection_set:
            child = _add_typename_to_selection_set(sel.selection_set, parent_field=sel.name.value, is_root=False)
            return FieldNode(
                alias=sel.alias,
                name=sel.name,
                arguments=sel.arguments,
                directives=sel.directives,
                selection_set=child,
            )
        return sel
    if isinstance(sel, InlineFragmentNode):
        return InlineFragmentNode(
            type_condition=sel.type_condition,
            directives=sel.directives,
            selection_set=_add_typename_to_selection_set(sel.selection_set, parent_field=None, is_root=False),
        )
    # FragmentSpreadNode has no inline selection set here
    return sel

def _add_typename_to_selection_set(selection_set: SelectionSetNode, parent_field: str | None, is_root: bool) -> SelectionSetNode:
    transformed_children: tuple[SelectionNode, ...] = tuple(_transform_selection(s) for s in selection_set.selections)

    # Skip adding on introspection fields or at root
    is_introspection_parent = parent_field in {"__schema", "__type"}

    new_set = SelectionSetNode(selections=transformed_children)
    if not is_root and not is_introspection_parent and not _has_typename(new_set):
        # Append to match expected output ordering
        new_set = SelectionSetNode(selections=(*transformed_children, _TYPENAME_FIELD))

    return new_set

def add_typename_to_document(doc: DocumentNode) -> DocumentNode:
    new_defs = []
    for d in doc.definitions:
        if isinstance(d, OperationDefinitionNode):
            ss = _add_typename_to_selection_set(d.selection_set, parent_field=None, is_root=True)
            new_defs.append(
                OperationDefinitionNode(
                    operation=d.operation,
                    name=d.name,
                    variable_definitions=d.variable_definitions,
                    directives=d.directives,
                    selection_set=ss,
                )
            )
        elif isinstance(d, FragmentDefinitionNode):
            ss = _add_typename_to_selection_set(d.selection_set, parent_field=None, is_root=False)
            new_defs.append(
                FragmentDefinitionNode(
                    name=d.name,
                    type_condition=d.type_condition,
                    directives=d.directives,
                    selection_set=ss,
                )
            )
        else:
            new_defs.append(d)
    return DocumentNode(definitions=tuple(new_defs))


# ---------- Hash exactly like browser (withTypenames + strip) ----------

def apq_hash_with_typenames_and_strip(doc: DocumentNode) -> str:
    with_typenames = add_typename_to_document(doc)
    printed = print_ast(with_typenames)
    stripped = strip_ignored_characters(printed)
    return hashlib.sha256(stripped.encode("utf-8")).hexdigest()


# ---------- Hash function you asked for ----------

def hash_graphql(ast_json: dict) -> str:
    """
    Convert a GraphQL-JS style JSON AST into graphql-core Python nodes,
    inject __typename like Apollo, print, strip ignored characters, and return SHA-256.
    """
    doc_node = document_from_json(ast_json)
    return apq_hash_with_typenames_and_strip(doc_node)


def _first_diff(a: str, b: str) -> int:
    limit = min(len(a), len(b))
    for i in range(limit):
        if a[i] != b[i]:
            return i
    return limit if len(a) != len(b) else -1


def _show_context(s: str, idx: int, radius: int = 80) -> str:
    start = max(0, idx - radius)
    end = min(len(s), idx + radius)
    return s[start:end]