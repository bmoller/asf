

class Context(object):
    """The ``context`` JSON object of a request from the Alexa service.

    To create a new :class:`Context <alexa.context.Context>`, pass the
    ``context`` object from the JSON-formatted request::

      >>> my_context = alexa.context.Context(event['context'])

    An example ``context`` JSON object::

      "context": {
          "AudioPlayer": {
              "playerActivity": "IDLE"
          },
          "System": {
              "apiEndpoint": "https://api.amazonalexa.com",
              "application": {
                  "applicationId": "amzn1.ask.skill.<application_id>"
              },
              "device": {
                  "deviceId": "amzn1.ask.device.<device_id>",
                  "supportedInterfaces": {
                      "AudioPlayer": {}
                  }
              },
              "user": {
                  "userId": "amzn1.ask.account.<account_id>"
              }
          }
      }

    For more information, see `the Alexa Skills Kit docs <https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/alexa-skills-kit-interface-reference#context-object>`_.
    """

    def __init__(self, context_data: dict):
        """
        :param context_data: The ``context`` object from the request sent by
            the Alexa service
        """

        #: A :class:`Device <alexa.context.Device>` representing the Amazon
        #: Echo making the request.
        self.device = Device(context_data['System']['device'])


class Device(object):
    """Represents an Amazon Echo device as described in the ``context`` object.

    To create a new :class:`Device <alexa.context.Device>`, pass the ``device``
    object from a ``context`` object.

    Example::

      >>> my_device = alexa.context.Device(event['context']['System']['device'])

    An example ``device`` JSON object::

      "device": {
          "deviceId": "amzn1.ask.device.<device_id>",
          "supportedInterfaces": {
              "AudioPlayer": {}
          }
      }

    For more information, see `the Alexa Skills kit docs <https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/alexa-skills-kit-interface-reference#system-object>`_.
    """

    def __init__(self, device_data: dict):
        """
        :param device_data: The ``device`` object from the request sent by the
            Alexa service.
        """

        #: A :class:`str` ID uniquely identifying the Amazon Echo device
        #: making the request.
        self.device_id = device_data['deviceId']

        #: :class:`bool` indicating whether the requesting Echo supports audio
        #: streaming.
        self.supports_streaming = 'AudioPlayer' in device_data['supportedInterfaces']
