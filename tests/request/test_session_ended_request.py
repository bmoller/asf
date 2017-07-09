import unittest

import alexa.request

from .. import (
    generate_request_id, generate_timestamp, generate_session_ended_error_type)


class SessionEndedRequestTestsMixin:

    BASE_INPUT = {
        'type': 'SessionEndedRequest',
        'requestId': '',
        'timestamp': '',
        'reason': '',
        'locale': 'en-US',
    }

    def setUp(self):
        # Randomize some input and create a SessionEndedRequest

        self.test_input['requestId'] = generate_request_id()
        self.test_input['timestamp'] = generate_timestamp()

        if self.test_input['reason'] == 'ERROR':
            self.test_input['error']['type'] = generate_session_ended_error_type()

        self.session_ended_request = alexa.request.SessionEndedRequest(self.test_input)

    def test_default_attributes(self):
        # All SessionEndedRequests should have these attributes

        for attribute, expected_value in [
            ('request_type', self.test_input['type']),
            ('request_id', self.test_input['requestId']),
            ('timestamp', self.test_input['timestamp']),
            ('reason', self.test_input['reason']),
            ('locale', self.test_input['locale']),
        ]:

            self.assertTrue(
                hasattr(self.session_ended_request, attribute),
                msg="SessionEndedRequest is missing expected attribute '{attribute}'".format(
                    attribute=attribute))

            self.assertEqual(
                getattr(self.session_ended_request, attribute), expected_value,
                msg="SessionEndedRequest attribute '{attribute}' equals '{actual}'; expected '{expected}'".format(
                    attribute=attribute,
                    actual=getattr(self.session_ended_request, attribute),
                    expected=expected_value))

    def test_error_attribute(self):
        # Check the error attribute if applicable

        if self.session_ended_request.reason != 'ERROR':
            return

        for attribute, expected_value in [
            ('error_type', self.test_input['error']['type']),
            ('error_message', self.test_input['error']['message']),
        ]:

            self.assertTrue(
                hasattr(self.session_ended_request, attribute),
                msg="SessionEndedRequest is missing expected attribute '{attribute}'".format(
                    attribute=attribute))

            self.assertEqual(
                getattr(self.session_ended_request, attribute), expected_value,
                msg="SessionEndedRequest attribute '{attribute}' equals '{actual}'; expected '{expected}'".format(
                    attribute=attribute,
                    actual=getattr(self.session_ended_request, attribute),
                    expected=expected_value))


class UserInitiatedSessionEndedRequest(
        SessionEndedRequestTestsMixin, unittest.TestCase):

    test_input = SessionEndedRequestTestsMixin.BASE_INPUT
    test_input['reason'] = 'USER_INITIATED'


class ErrorSessionEndedRequest(
        SessionEndedRequestTestsMixin, unittest.TestCase):

    test_input = SessionEndedRequestTestsMixin.BASE_INPUT
    test_input['reason'] = 'ERROR'
    test_input['error'] = {
        'type': '',
        'message': 'A super bad thing happened',
    }


class ExceededMaxRepromptsSessionEndedRequest(
    SessionEndedRequestTestsMixin, unittest.TestCase):

    test_input = SessionEndedRequestTestsMixin.BASE_INPUT
    test_input['reason'] = 'EXCEEDED_MAX_REPROMPTS'
