import json
from pathlib import Path
from libs.roles import roles


class users(roles):

    def __init__(self, event_type=''):
        self.type = event_type

    def _load_json(self, json_path):  # pragma: no cover
        with open(json_path) as f:
            return json.load(f)

    def __parse(self, data):
        return json.loads(data)

    def __is_loaded(self, data):
        return len(data)

    def setUsers(self, data):
        parsed = self.__parse(data)
        if self.__is_loaded(parsed):
            return {'message': 'Users Created'}
        return {}

    def getUsers(self):  # pragma: no cover
        users = self._load_json(USERS_STORAGE)
        parsed_users = self.__parse(users)
        return parsed_users

    def getUserByParent(self, data):  # pragma: no cover
        parsed = self.__parse(data)
        users = self._load_json(USERS_STORAGE)
        parsed_users = self.__parse(users['body'])
        filtered_users = list(filter(lambda i: roles.getRoleById(self, i['Role'])['Parent'] >= parsed['parentId'], parsed_users))
        return filtered_users


# constants
USERS_STORAGE = f'{Path.cwd()}/tests/fixtures/payload/string/users_request.txt'
