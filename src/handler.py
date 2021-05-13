import sys
import json
from utils.log_integration import LambdaLogIntegration
from libs.roles import roles
from libs.users import users

logger = LambdaLogIntegration()
roles = roles()
users = users()


def setRoles(event, context):
    try:
        response = roles.setRoles(event['body'])

    except Exception as e:
        print(logger.logInfo("ERROR: " + str(e)))
        sys.exit(1)

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }


def setUsers(event, context):
    try:
        response = users.setUsers(event['body'])

    except Exception as e:
        print(logger.logInfo("ERROR: " + str(e)))
        sys.exit(1)

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }


def getSubOrdinates(event, context):
    try:
        response = users.getUserByParent(event['body'])

    except Exception as e:
        print(logger.logInfo("ERROR: " + str(e)))
        sys.exit(1)

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
