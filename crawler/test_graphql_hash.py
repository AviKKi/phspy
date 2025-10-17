import hashlib
import pytest
from graphql.language.printer import print_ast
from graphql.utilities import strip_ignored_characters

from crawler.graphql_hash import (
    document_from_json,
    add_typename_to_document,
    hash_graphql,
)
from crawler.test_query import (
    test_query,
    test_with_typenames,
    test_with_typenames_stripped,
    test_hash,
)


def test_add_typename_print_matches_expected():
    doc = document_from_json(test_query)
    with_typenames = add_typename_to_document(doc)
    printed = print_ast(with_typenames)
    assert printed == test_with_typenames


def test_strip_matches_expected():
    doc = document_from_json(test_query)
    with_typenames = add_typename_to_document(doc)
    printed = print_ast(with_typenames)
    stripped = strip_ignored_characters(printed)
    assert stripped == test_with_typenames_stripped


def test_hash_graphql_matches_expected_sha():
    digest = hash_graphql(test_query)
    assert digest == test_hash


def test_direct_sha_matches_expected():
    doc = document_from_json(test_query)
    with_typenames = add_typename_to_document(doc)
    printed = print_ast(with_typenames)
    stripped = strip_ignored_characters(printed)
    direct_hash = hashlib.sha256(stripped.encode("utf-8")).hexdigest()
    assert direct_hash == test_hash
