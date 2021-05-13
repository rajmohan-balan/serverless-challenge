import pytest
import json
from pathlib import Path
from libs.roles import roles

roles = roles()


def load_json(json_path):
    with open(json_path) as f:
        return f.read()


@pytest.mark.parametrize("event,expected", [
    (load_json(
        f'{Path.cwd()}/tests/fixtures/payload/string/roles_request.txt'),
     {'message': 'Roles Created'})
])

def test_happy_set_roles(event, expected):
    actual = roles.setRoles(event)
    assert actual == expected


@pytest.mark.parametrize("event,expected", [
    ("[]", {})
])
def test_sad_set_roles(event, expected):
    assert roles.setRoles(event) == expected