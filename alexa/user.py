

class User:

    def __init__(self, id: str, consent_token: str=None):
        """ Create a new Alexa user with provided information

        :param id: User ID as provided in the session and context
        :param consent_token: Permissions consent token as provided in the
                              session and context
        """

        self.id = id

        if consent_token:
            self.consent_token = consent_token
