import random
import uuid

APPLICATION_ID_PREFIX = 'amzn1.ask.skill'
DEVICE_ID_CHARACTER_SET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
DEVICE_ID_LENGTH = 156
DEVICE_ID_PREFIX = 'amzn1.ask.device'
REQUEST_ID_PREFIX = 'amzn1.echo-api.request'
SESSION_ID_PREFIX = 'amzn1.echo-api.session'
USER_ID_CHARACTER_SET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
USER_ID_LENGTH = 207
USER_ID_PREFIX = 'amzn1.ask.account'


def generate_access_token() -> str:
    """Generates a user access token similar to what might be in an Alexa
    request.

    :return: Generated access token
    """

    return 'laksfdqiohjweipobqvcljakhnfioquwefoiu'


def generate_application_id(prefix: str=APPLICATION_ID_PREFIX) -> str:
    """Generates an Alexa skill application ID, which is composed of a static
    prefix followed by a UUID.

    :param prefix: Optionally-specified prefix to use

    :return: Generated Alexa skill application ID
    """

    return '.'.join([prefix, str(uuid.uuid4())])


def generate_consent_token() -> str:
    """Generates a consent token similar to what might be in an Alexa request.
    Consent tokens indicate which permissions a user has granted a skill and
    are used to request user-specific information from AWS API's.

    :return: Generated Alexa skill consent token
    """

    return 'Atza|MQEWY...6fnLok'


def generate_device_id(
        prefix: str=DEVICE_ID_PREFIX,
        character_set: str=DEVICE_ID_CHARACTER_SET,
        length: int=DEVICE_ID_LENGTH) -> str:
    """Generates a device ID similar to those for an Amazon Echo as seen in an
    Alexa request.

    :param prefix: Optional ID prefix
    :param character_set: Optional character set to use in ID generation
    :param length: Optional length of the generated ID

    :return: Generated Amazon Echo device ID
    """

    device_id = ''
    for count in range(length):
        device_id += random.choice(character_set)

    return '.'.join([prefix, device_id])


def generate_request_id(prefix: str=REQUEST_ID_PREFIX) -> str:
    """Generates an Alexa skill request ID, composed of a static prefix joined
    with a UUID.

    :param prefix: Optional ID prefix

    :return: Generated Alexa skill session ID
    """

    return '.'.join([prefix, str(uuid.uuid4())])


def generate_session_id(prefix: str=SESSION_ID_PREFIX) -> str:
    """Generates an Alexa skill session ID, composed of a static prefix joined
    with a UUID.

    :param prefix: Optional ID prefix

    :return: Generated Alexa skill session ID
    """

    return '.'.join([prefix, str(uuid.uuid4())])


def generate_user_id(
        prefix: str=USER_ID_PREFIX, character_set: str=USER_ID_CHARACTER_SET,
        length: int=USER_ID_LENGTH) -> str:
    """Generates an Alexa skill user ID, composed of a static prefix joined
    with a random string. Alexa skill docs indicate that this ID changes if a
    user disables and subsequently re-enables a skill.

    :param prefix: Optional ID prefix
    :param character_set: Optional character set to use in ID generation
    :param length: Optional length of the generated ID

    :return: Generated Alexa skill user ID
    """

    user_id = ''
    for count in range(length):
        user_id += random.choice(character_set)

    return '.'.join([prefix, user_id])
