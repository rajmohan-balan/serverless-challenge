import json
import pytest

from pathlib import Path
from handler import getSubOrdinates


def load_json(json_path):
    with open(json_path) as f:
        return json.load(f)


@pytest.mark.parametrize("event,expected", [
    (load_json(f'{Path.cwd()}/tests/fixtures/payload/string/subordinates_request.txt')[0], load_json(f'{Path.cwd()}/tests/fixtures/payload/json/subordinates_response.json')[0]['response']),
    (load_json(f'{Path.cwd()}/tests/fixtures/payload/string/subordinates_request.txt')[1], load_json(f'{Path.cwd()}/tests/fixtures/payload/json/subordinates_response.json')[1]['response']),
    (load_json(f'{Path.cwd()}/tests/fixtures/payload/string/subordinates_request.txt')[2], load_json(f'{Path.cwd()}/tests/fixtures/payload/json/subordinates_response.json')[2]['response']),
    (load_json(f'{Path.cwd()}/tests/fixtures/payload/string/subordinates_request.txt')[3], load_json(f'{Path.cwd()}/tests/fixtures/payload/json/subordinates_response.json')[3]['response']),
    (load_json(f'{Path.cwd()}/tests/fixtures/payload/string/subordinates_request.txt')[4], load_json(f'{Path.cwd()}/tests/fixtures/payload/json/subordinates_response.json')[4]['response'])
])

def test_getSubOrdinates(event, expected):
    assert getSubOrdinates(event, {}) == expected