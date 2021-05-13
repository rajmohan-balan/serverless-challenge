import json
import pytest

from pathlib import Path
from handler import setRoles


def load_json(json_path):
    with open(json_path) as f:
        return json.load(f)


@pytest.mark.parametrize("event,expected", [
    (load_json(
        f'{Path.cwd()}/tests/fixtures/payload/string/roles_request.txt'),
     load_json(
        f'{Path.cwd()}/tests/fixtures/payload/json/roles_response.json'))
])

def test_setRoles(event, expected):
    assert setRoles(event, {}) == expected