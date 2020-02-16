"""Store information into users table about a new user"""
import json
import logging.config
import os

import boto3


LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)
USERS_TABLE = boto3.resource('dynamodb').Table(os.environ['USERS_TABLE_NAME'])


def handler(event, context):
    LOGGER.info(json.dumps(event))
    email = event['request']['userAttributes']['email']
    USERS_TABLE.put_item(Item={'email': email})

    return event
