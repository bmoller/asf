import unittest

import alexa.request

from .. import (
    generate_dialog_state, generate_request_id, generate_timestamp,
    generate_confirmation_status)


class IntentRequestTestsMixin:

    BASE_INPUT = {
        'type': 'IntentRequest',
        'requestId': '',
        'timestamp': '',
        'locale': 'en-US',
        'intent': {
            'name': 'my_sweet_intent',
            'confirmationStatus': '',
        },
    }

    def setUp(self):
        # Randomize some input and create an IntentRequest

        self.test_input['requestId'] = generate_request_id()
        self.test_input['timestamp'] = generate_timestamp()
        self.test_input['intent']['confirmationStatus'] = generate_confirmation_status()

        self.intent_request = alexa.request.IntentRequest(self.test_input)

    def test_default_attributes(self):
        # All IntentRequests should have these attributes

        for attribute, expected_value in [
            ('request_type', self.test_input['type']),
            ('timestamp', self.test_input['timestamp']),
            ('request_id', self.test_input['requestId']),
            ('locale', self.test_input['locale']),
        ]:

            self.assertTrue(
                hasattr(self.intent_request, attribute),
                msg="IntentRequest is missing expected attribute '{attribute}'".format(
                    attribute=attribute))

            self.assertEqual(
                getattr(self.intent_request, attribute), expected_value,
                msg="IntentRequest attribute '{attribute}' equals '{actual}'; expected '{expected}'".format(
                    attribute=attribute,
                    actual=getattr(self.intent_request, attribute),
                    expected=expected_value))

        self.assertTrue(
            hasattr(self.intent_request, 'intent'),
            msg="IntentRequest is missing expected attribute 'intent'")

    def test_dialog_state_attribute(self):
        # Check the dialog_state if it's in the input

        if 'dialogState' not in self.test_input:
            return

        self.assertTrue(
            hasattr(self.intent_request, 'dialog_state'),
            msg="IntentRequest is missing expected attribute 'dialog_state'")

        self.assertEqual(
            self.intent_request.dialog_state, self.test_input['dialogState'],
            msg="IntentRequest attribute 'dialog_state' equals '{actual}'; expected '{expected}'".format(
                actual=self.intent_request.dialog_state,
                expected=self.test_input['dialogState']))


class SimpleIntentRequest(IntentRequestTestsMixin, unittest.TestCase):

    test_input = IntentRequestTestsMixin.BASE_INPUT


class SimpleIntentRequest(IntentRequestTestsMixin, unittest.TestCase):

    test_input = IntentRequestTestsMixin.BASE_INPUT
    test_input['dialogState'] = generate_dialog_state()
