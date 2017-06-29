import random
import uuid

APPLICATION_ID_PREFIX = 'amzn1.ask.skill'
DEVICE_ID_CHARACTER_SET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
DEVICE_ID_PREFIX = 'amzn1.ask.device'
SESSION_ID_PREFIX = 'amzn1.echo-api.session'
USER_ID_CHARACTER_SET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
USER_ID_PREFIX = 'amzn1.ask.account'


def generate_access_token() -> str:

    return 'laksfdqiohjweipobqvcljakhnfioquwefoiu'


def generate_application_id() -> str:

    return '.'.join([APPLICATION_ID_PREFIX, str(uuid.uuid4())])


def generate_consent_token() -> str:

    return 'Atza|MQEWY...6fnLok'


def generate_device_id() -> str:

    device_id = ''
    for count in range(156):
        device_id += random.choice(DEVICE_ID_CHARACTER_SET)

    return '.'.join([DEVICE_ID_PREFIX, device_id])


def generate_session_id() -> str:

    return '.'.join([SESSION_ID_PREFIX, str(uuid.uuid4())])


def generate_user_id() -> str:

    user_id = ''
    for count in range(207):
        user_id += random.choice(USER_ID_CHARACTER_SET)

    return '.'.join([USER_ID_PREFIX, user_id])
