import os
import sys
import types
from typing import Any, Callable, Dict, Optional
import pytest
import requests

# Ensure repository root is on sys.path so `import crawler` works reliably
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

class _MockResponse:
    def __init__(self, status_code: int = 200, json_body: Optional[Dict[str, Any]] = None, text: str = ""):
        self.status_code = status_code
        self._json = json_body
        self.text = text or ("" if json_body is None else str(json_body))

    def json(self) -> Dict[str, Any]:
        return {} if self._json is None else self._json


class _RequestsMocker:
    def __init__(self):
        self._responses: Dict[str, Dict[str, Dict[str, Any]]] = {"POST": {}}
        self._orig_post: Optional[Callable[..., Any]] = None

    def start(self):
        if self._orig_post is None:
            self._orig_post = requests.post

        def _post(url: str, *args, **kwargs):
            entry = self._responses["POST"].get(url)
            if not entry:
                return _MockResponse(status_code = 404, json_body = {"error": "Not Found"}, text = "Not Found")
            if entry.get("exc") is not None:
                raise entry["exc"]
            return _MockResponse(status_code = entry.get("status_code", 200), json_body = entry.get("json"), text = entry.get("text", ""))

        requests.post = _post  # type: ignore[assignment]

    def stop(self):
        if self._orig_post is not None:
            requests.post = self._orig_post  # type: ignore[assignment]
            self._orig_post = None

    # API compatible with requests_mock plugin used in tests
    def post(self, url: str, json: Optional[Dict[str, Any]] = None, status_code: int = 200, exc: Optional[BaseException] = None, **kwargs):
        self._responses["POST"][url] = {"json": json, "status_code": status_code, "exc": exc, **kwargs}
        return None


@pytest.fixture
def requests_mock():
    mocker = _RequestsMocker()
    mocker.start()
    try:
        yield mocker
    finally:
        mocker.stop()


