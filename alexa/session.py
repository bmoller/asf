

class Session:

    def __init__(self, session_data: dict):

        if session_data['new']:
            self.new = True
        else:
            self.new = False
        self.session_id = session_data['sessionId']
        self.application = Application(session_data['application'])
        self.user = User(session_data['user'])

        if 'attributes' in session_data:
            for attribute, value in session_data['attributes'].items():
                setattr(self, attribute, value)


class Application:

    def __init__(self, application_data: dict):
        """Creates an application object from the provided JSON object. The
        application object is useful for confirming that the current request is
        actually intended and authorized.

        :param application_data:
            The 'application' object from the 'session' object in the Lambda
            event
        """

        self.application_id = application_data['applicationId']


class User:

    def __init__(self, user_data: dict):
        """Create a new Alexa user with provided information

        :param user_data:
            The 'user' object from the 'session' object in the Lambda event
        """

        self.user_id = user_data['userId']

        if ('permissions' in user_data
                and 'consentToken' in user_data['permissions']):
            self.consent_token = user_data['permissions']['consentToken']

        if 'accessToken' in user_data:
            self.access_token = user_data['accessToken']
