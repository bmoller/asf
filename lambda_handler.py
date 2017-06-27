import importlib

import alexa.session
import alexa.user


def lambda_handler(event: dict, context) -> dict:
    """

    :param event: Lambda event object passed to all functions by the Lambda
                  service
    :param context: Lambda context object passed to all Lambda functions

    :return: An Alexa-skill structured response object
    """

    session_data = event['session']
    context_data = event['context']
    request_data = event['request']

    keyword_parameters, parameters = {}, [
        session_data['sessionId'],
        session_data['application']['applicationId']
    ]
    if not session_data['new']:
        keyword_parameters['new'] = False
    if 'attributes' in session_data and session_data['attributes']:
        keyword_parameters['attributes'] = session_data['attributes']
    if keyword_parameters:
        alexa_session = alexa.session.Session(*parameters, **keyword_parameters)
    else:
        alexa_session = alexa.session.Session(*parameters)

    if ('permissions' in session_data['user']
            and 'consentToken' in session_data['user']['permissions']
            and session_data['user']['permissions']['consentToken']):
        alexa_user = alexa.user.User(session_data['user']['userId'],
                                     session_data['user']['permissions']['consentToken'])
    else:
        alexa_user = alexa.user.User(session_data['user']['userId'])

    intent_handler = importlib('.'.join(['intents', request_data['intent']['name']]))

    return intent_handler.handle_intent(alexa_session, alexa_user)
