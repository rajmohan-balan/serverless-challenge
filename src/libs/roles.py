import json
from pathlib import Path


class roles:

    def _load_json(self, json_path):
        with open(json_path) as f:  # pragma: no cover
            return json.load(f)

    def __parse(self, data):
        return json.loads(data)

    def __is_loaded(self, data):
        return len(data)

    def setRoles(self, data):
        parsed = self.__parse(data)
        if self.__is_loaded(parsed):
            return {'message': 'Roles Created'}
        return {}

    def getRoles(self):  # pragma: no cover
        roles = self._load_json(ROLES_STORAGE)
        parsed_roles = self.__parse(roles)
        return parsed_roles

    def getRoleById(self, Id):  # pragma: no cover
        roles = self._load_json(ROLES_STORAGE)
        parsed_roles = self.__parse(roles['body'])
        for role in parsed_roles:
            if role["Id"] == Id:
                return role


# constants
ROLES_STORAGE = f'{Path.cwd()}/tests/fixtures/payload/string/roles_request.txt'
