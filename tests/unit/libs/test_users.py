import pytest
import json
from pathlib import Path
from libs.users import users

users = users()


def load_json(json_path):
    with open(json_path) as f:
        return f.read()


@pytest.mark.parametrize("event,expected", [
    (load_json(
        f'{Path.cwd()}/tests/fixtures/payload/string/users_request.txt'),
     {'message': 'Users Created'})
])

def test_happy_set_users(event, expected):
    actual = users.setUsers(event)
    assert actual == expected


@pytest.mark.parametrize("event,expected", [
    ("[]", {})
])
def test_sad_set_users(event, expected):
    assert users.setUsers(event) == expected