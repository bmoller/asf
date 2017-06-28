PLAIN_TEXT = 'PlainText'
SSML = 'SSML'


def build_response(
        response_type: str, response_text: str, session_attributes: dict=None,
        should_end_session: bool=True) -> dict:
    """ Builds a dict structure that can be returned as an Alexa skill response

    :param response_type: Using the module attributes, specify whether the
                          response is plain text to be read or speech markup
    :param response_text: The actual response for Alexa to speak
    :param session_attributes: Key/value pairs that will be stored in the
                               user's session
    :param should_end_session: Determines if Alexa should listen for a response
                               or the conversation is over

    :return: An Alexa skill response
    """

    response = {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': response_type,
            },
            'shouldEndSession': should_end_session,
        },
    }

    if response_type == SSML:
        response['response']['outputSpeech']['ssml'] = response_text
    else:
        response['response']['outputSpeech']['text'] = response_text

    if session_attributes:
        response['session_attributes'] = session_attributes

    return response


def build_card():
    pass
