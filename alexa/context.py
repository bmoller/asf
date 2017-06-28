

class Context:

    def __init__(self, context_data: dict):
        """Creates a new Alexa interaction context
        
        :param context_data:
            The 'context' object from the event passed by the Lambda service to
            the function entry point
        """

        self.application = Application(
            context_data['System']['application']['applicationId'])

        access_token, consent_token = None, None
        if 'accessToken' in context_data['System']['user']:
            access_token = context_data['System']['user']['accessToken']
        if ('permissions' in context_data['System']['user']
                and 'consentToken' in context_data['System']['user']['permissions']):
            consent_token = context_data['System']['user']['permissions']['consentToken']
        self.user = User(
            context_data['System']['user']['userId'],
            consent_token=consent_token, access_token=access_token)

        supports_streaming = 'AudioPlayer' in context_data['System']['device']['supportedInterfaces']
        self.device = Device(
            context_data['System']['device']['deviceId'],
            supports_streaming=supports_streaming)


class Application:

    def __init__(self, application_id: str):
        """Creates an application object with the specified ID
        
        :param application_id:
            ID of the Alexa skill. This can be used to verify that a received
            request is indeed for this skill
        """

        self.application_id = application_id


class User:

    def __init__(
            self, user_id: str, consent_token: str=None,
            access_token: str=None):
        """Create a new Alexa user with provided information

        :param user_id: User ID as provided in the session and context
        :param consent_token:
            Permissions consent token as provided in the session and context
        :param access_token:
            The user's access token provided as part of integration with a
            third-party service
        """

        self.user_id = user_id

        if consent_token:
            self.consent_token = consent_token

        if access_token:
            self.access_token = access_token


class Device:

    def __init__(self, device_id: str, supports_streaming: bool=False):
        """Creates a new device with the specified ID
        
        :param device_id: ID of the Echo device
        :param supports_streaming:
            Indicates if the requesting device supports the AudioPlayer
            interface
        """

        self.device_id = device_id
        self.supports_streaming = supports_streaming
