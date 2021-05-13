import json
import pytest

from pathlib import Path
from handler import setUsers


def load_json(json_path):
    with open(json_path) as f:
        return json.load(f)


@pytest.mark.parametrize("event,expected", [
    (load_json(
        f'{Path.cwd()}/tests/fixtures/payload/string/users_request.txt'),
     load_json(
        f'{Path.cwd()}/tests/fixtures/payload/json/users_response.json'),)
])

def test_setUsers(event, expected):
    assert setUsers(event, {}) == expected