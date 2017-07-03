

class Session(object):
    """The ``session`` JSON object of a request from the Alexa service.

    To create a new :class:`Session <alexa.session.Session>`, pass the
    ``session`` object from the JSON-formatted request::

      >>> my_session = alexa.session.Session(event['session'])

    An example ``session`` JSON object::

      "session": {
          "application": {
              "applicationId": "amzn1.ask.skill.<application_id>"
          },
          "new": true,
          "sessionId": "amzn1.echo-api.session.<session_id>",
          "user": {
              "userId": "amzn1.ask.account.<user_id>"
          }
      }

    For more information, see `the Alexa Skills Kit docs <https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/alexa-skills-kit-interface-reference#session-object>`_.

    In addition to the default attributes listed below, any attributes saved to
    the user's session will be created as attributes directly on the
    :class:`Session <alexa.session.Session>` instance.
    """

    def __init__(self, session_data: dict):
        """
        :param session_data: The ``session`` object from the request sent by
            the Alexa service.
        """

        if session_data['new']:
            #: :class:`bool` indicating if this is a request in an ongoing
            #: dialog, or the first request of a new conversation.
            self.new = True
        else:
            self.new = False

        #: The session ID as a :class:`str`.
        self.session_id = session_data['sessionId']

        #: Am :class:`Application <alexa.session.Application>` representing the
        #: Alexa skill application.
        self.application = Application(session_data['application'])

        #: Represents the Echo user as a :class:`User <alexa.session.User>`.
        self.user = User(session_data['user'])

        # Set session attributes directly on the instance for ease of access
        if 'attributes' in session_data:
            for attribute, value in session_data['attributes'].items():
                setattr(self, attribute, value)


class Application(object):
    """The ``application`` JSON object of a request from the Alexa service.

    To create a new :class:`Application <alexa.session.Application>`, pass the
    ``application`` object from the JSON-formatted request::

      >>> my_session = alexa.session.Application(event['session']['application'])

    An example ``application`` JSON object::

      "application": {
          "applicationId": "amzn1.ask.skill.<application_id>"
      }

    The application ID should match what is shown in
    `the Developer Portal <https://developer.amazon.com/edw/home.html#/>`_ for
    your Alexa skill.
    """

    def __init__(self, application_data: dict):
        """
        :param application_data: The ``application`` object from the request
            sent by the Alexa service.
        """

        #: A :class:`str` of the request's application ID. This can be used to
        #: `confirm a request <https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/handling-requests-sent-by-alexa#verifying-that-the-request-is-intended-for-your-service>`_
        #: is indeed intended for this skill in order to protect your endpoint.
        self.application_id = application_data['applicationId']


class User(object):
    """The ``user`` JSON object of a request from the Alexa service.

    To create a new :class:`User <alexa.session.User>`, pass the ``user``
    object from the JSON-formatted request::

      >>> my_session = alexa.session.Application(event['session']['user'])

    An example ``user`` JSON object::

      "user": {
          "userId": "amzn1.ask.account.<user_id>",
          "permissions": {
              "consentToken": "<token>"
          },
          "accessToken": "<token>"
      }

    """

    def __init__(self, user_data: dict):
        """
        :param user_data: The ``user`` object from the request sent by the
            Alexa service.
        """

        #: :class:`str` containing the Echo user's ID.
        self.user_id = user_data['userId']

        if ('permissions' in user_data
                and 'consentToken' in user_data['permissions']):

            #: A token in :class:`str` format indicating that the user has
            #: granted your skill access to personal information. For example,
            #: your skill can retrieve the user's location to provide more
            #: useful and accurate information; see
            #: `the Alexa Skills Kit docs <https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/device-address-api>`_
            #: for more information.
            self.consent_token = user_data['permissions']['consentToken']

        if 'accessToken' in user_data:
            #: A :class:`str` token provided by your server to identify the
            #: user against your third-party service. This is only required to
            #: integrate data from your external service; persistent data can
            #: easily be stored in a service like DynamoDB. Reference
            #: `the Alexa Skills Kit documentation <https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/linking-an-alexa-user-with-a-user-in-your-system>`_
            #: for direction on setting up service integration.
            self.access_token = user_data['accessToken']
