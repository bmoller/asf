

class Session:

    def __init__(self, session_data: dict):

        if session_data['new']:
            self.new = True
        else:
            self.new = False
        self.session_id = session_data['sessionId']

        self.application = Application(
            session_data['application']['applicationId'])

        access_token, consent_token = None, None
        if 'accessToken' in session_data['user']:
            access_token = session_data['user']['accessToken']
        if ('permissions' in session_data['user']
            and 'consentToken' in session_data['user']['permissions']):
            consent_token = session_data['user']['permissions']['consentToken']
        self.user = User(
            session_data['user']['userId'], consent_token=consent_token,
            access_token=access_token)

        if 'attributes' in session_data:
            for attribute, value in session_data['attributes'].items():
                setattr(self, attribute, value)


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
