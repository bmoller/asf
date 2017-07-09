import unittest

import alexa.request

from .. import generate_request_id, generate_timestamp


class RequestTestsMixin:

    BASE_INPUT = {
        'type': '',
        'requestId': '',
        'timestamp': '',
        'locale': 'en-US',
    }

    def setUp(self):
        # Randomize some input and create a Request

        self.test_input['requestId'] = generate_request_id()
        self.test_input['timestamp'] = generate_timestamp()

        self.request = alexa.request.Request(self.test_input)

    def test_default_attributes(self):
        # All Request objects should have these attributes

        for attribute, expected_value in [
            ('request_type', self.test_input['type']),
            ('timestamp', self.test_input['timestamp']),
            ('request_id', self.test_input['requestId']),
            ('locale', self.test_input['locale']),
        ]:

            self.assertTrue(
                hasattr(self.request, attribute),
                msg="Request is missing expected attribute '{attribute}'".format(
                    attribute=attribute))

            self.assertEqual(
                getattr(self.request, attribute), expected_value,
                msg="Request attribute '{attribute}' equals '{actual}'; expected '{expected}'".format(
                    attribute=attribute,
                    actual=getattr(self.request, attribute),
                    expected=expected_value))


class SimpleRequest(RequestTestsMixin, unittest.TestCase):

    test_input = RequestTestsMixin.BASE_INPUT
    test_input['type'] = 'LaunchRequest'
