import datetime
import random
import unittest

import alexa.request

from . import generate_request_id, generate_timestamp


class AlexaRequestTestCase(unittest.TestCase):

    def setUp(self):
        """Set attributes used in multiple places"""

        self.request_id = generate_request_id()
        self.timestamp = generate_timestamp()

        self.request_creation_test_cases = {
            'IntentRequest': {
                'intent': {
                    'name': 'my_sweet_intent',
                },
                'locale': 'en-US',
                'requestId': self.request_id,
                'timestamp': self.timestamp,
                'type': 'IntentRequest',
            }
        }

    def tearDown(self):
        """Remove attributes created in test setup"""

        for attribute in [
                'request_id', 'timestamp', 'request_creation_test_cases']:
            delattr(self, attribute)

    def test_request_creation(self):
        """Test creation of new Request objects"""

        for test_case, test_input in self.request_creation_test_cases.items():
            test_request = alexa.request.Request(test_input)

            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_request.locale, test_input['locale'],
                    msg='New Request has an incorrect locale')

            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_request.request_id, test_input['requestId'],
                    msg='New Request has an incorrect request_id')

            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_request.timestamp, test_input['timestamp'],
                    msg='New Request has an incorrect timestamp')

            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_request.request_type, test_input['type'],
                    msg='New Request has an incorrect type')


class AlexaIntentRequestTestCase(unittest.TestCase):

    def setUp(self):
        """Set attributes used in multiple places"""

        self.request_id = generate_request_id()
        self.timestamp = generate_timestamp()

        self.request_creation_test_cases = {
            'Basic IntentRequest': {
                'intent': {
                    'name': 'my_sweet_intent',
                },
                'locale': 'en-US',
                'requestId': self.request_id,
                'timestamp': self.timestamp,
                'type': 'IntentRequest',
            }
        }

    def tearDown(self):
        """Remove attributes created in test setup"""

        for attribute in [
                'request_id', 'timestamp', 'request_creation_test_cases', ]:
            delattr(self, attribute)

    def test_intent_request_creation(self):
        """Test creation of new IntentRequest objects"""

        for test_case, test_input in self.request_creation_test_cases.items():
            test_request = alexa.request.IntentRequest(test_input)

            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_request.locale, test_input['locale'],
                    msg='New IntentRequest has an incorrect locale')

            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_request.request_id, test_input['requestId'],
                    msg='New IntentRequest has an incorrect request_id')

            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_request.timestamp, test_input['timestamp'],
                    msg='New IntentRequest has an incorrect timestamp')

            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_request.request_type, test_input['type'],
                    msg='New IntentRequest has an incorrect type')

            if 'dialogState' in test_input:
                with self.subTest(test_case=test_case):
                    self.assertEqual(
                        test_request.dialog_state, test_input['dialogState'],
                        msg='New IntentRequest has an incorrect dialog_state')


class AlexaIntentTestCase(unittest.TestCase):

    def setUp(self):
        """Set attributes used in multiple places"""

        self.intent_creation_test_cases = {
            'Simple Intent': {
                'name': 'my_sweet_intent',
                'confirmationStatus': 'NONE',
            },
            'Intent with Slots': {
                'name': 'my_sweet_intent',
                'confirmationStatus': 'NONE',
                'slots': {
                    'slot_1': {
                        'name': 'slot_1',
                        'value': 'value_1',
                        'confirmationStatus': '',
                    },
                    'slot_2': {
                        'name': 'slot_2',
                        'value': 'value_2',
                        'confirmationStatus': '',
                    },
                    'slot_3': {
                        'name': 'slot_3',
                        'value': 'value_3',
                        'confirmationStatus': '',
                    },
                },
            },
        }

    def tearDown(self):
        """Remove attributes created in test setup"""

        for attribute in ['intent_creation_test_cases', ]:
            delattr(self, attribute)

    def test_intent_creation(self):
        """Test creation of new Intent objects"""

        for test_case, test_input in self.intent_creation_test_cases.items():
            test_intent = alexa.request.Intent(test_input)
            self.check_new_intent(test_intent, test_case, test_input)

    @classmethod
    def check_new_intent(
            cls, test_intent: alexa.request.Intent, test_case: str,
            test_input: dict):
        """Check that a new Intent has the expected attributes

        :param test_intent: New Intent to check
        :param test_case: Name of the test case for printing on failure
        :param test_input: Test input that was provided to the __init__ method
        """

        with cls.subTest(test_case=test_case):
            cls.assertEqual(
                test_intent.name, test_input['name'],
                msg='New Intent has an incorrect name')

        with cls.subTest(test_case=test_case):
            cls.assertEqual(
                test_intent.confirmation_status,
                test_input['confirmationStatus'],
                msg='New Intent has an incorrect confirmation_status')


class AlexaSlotTestCase(unittest.TestCase):

    def setUp(self):
        """Set attributes used in tests"""

        self.slot_creation_test_cases = {
            'Simple Slot': {
                'name': 'simple_slot',
                'value': 'simple_value',
                'confirmationStatus': 'NONE',
            },
        }

    def tearDown(self):
        """Remove attributes created in test setup"""

        for attribute in ['slot_creation_test_cases', ]:
            delattr(self, attribute)

    def test_slot_creation(self):
        """Test creation of new Slot objects"""

        for test_case, test_input in self.slot_creation_test_cases.items():
            test_slot = alexa.request.Slot(test_input)

            for attribute in ['name', 'value', ]:
                with self.subTest(test_case=test_case):
                    self.assertEqual(
                        getattr(test_slot, attribute), test_input[attribute],
                        msg='New Slot has an incorrect value for \'{attribute}\' attribute'.format(attribute=attribute))

            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_slot.confirmation_status,
                    test_input['confirmationStatus'],
                    msg='New Slot has an incorrect confirmation_status')


class AlexaSessionEndedRequestTestCase(unittest.TestCase):

    def setUp(self):
        """Set attributes used in multiple places"""

        self.error_type = random.choice([
            'DEVICE_COMMUNICATION_ERROR',
            'INTERNAL_ERROR',
            'INVALID_RESPONSE',
        ])

        self.session_ended_request_creation_test_cases = {
            'Error': {
                'error': {
                    'message': 'A super bad thing happened',
                    'type': self.error_type,
                },
                'locale': 'en-US',
                'reason': 'ERROR',
                'requestId': generate_request_id(),
                'timestamp': generate_timestamp(),
                'type': 'SessionEndedRequest',
            },
            'Exceeded Maximum Re-prompts': {
                'locale': 'en-US',
                'reason': 'EXCEEDED_MAX_REPROMPTS',
                'requestId': generate_request_id(),
                'timestamp': generate_timestamp(),
                'type': 'SessionEndedRequest',
            },
            'User-Initiated': {
                'locale': 'en-US',
                'reason': 'USER_INITIATED',
                'requestId': generate_request_id(),
                'timestamp': generate_timestamp(),
                'type': 'SessionEndedRequest',
            },
        }

    def tearDown(self):
        """Remove attributes created in test setup"""

        for attribute in [
                'error_type', 'session_ended_request_creation_test_cases', ]:
            delattr(self, attribute)

    def test_session_ended_request_creation(self):
        """Test creation of new SessionEndedRequest objects"""

        for test_case, test_input in self.session_ended_request_creation_test_cases.items():
            test_request = alexa.request.SessionEndedRequest(test_input)

            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_request.locale, test_input['locale'],
                    msg='New SessionEndedRequest has an incorrect locale')

            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_request.request_id, test_input['requestId'],
                    msg='New SessionEndedRequest has an incorrect request_id')

            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_request.timestamp, test_input['timestamp'],
                    msg='New SessionEndedRequest has an incorrect timestamp')

            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_request.request_type, test_input['type'],
                    msg='New SessionEndedRequest has an incorrect type')

            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_request.reason, test_input['reason'],
                    msg='New SessionEndedRequest has an incorrect reason')

            if 'error' in test_input:

                if 'message' in test_input['error']:
                    with self.subTest(test_case=test_case):
                        self.assertEqual(
                            test_request.error_message,
                            test_input['error']['message'],
                            msg='New SessionEndedRequest has an incorrect error_message')

                if 'type' in test_input['error']:
                    with self.subTest(test_case=test_case):
                        self.assertEqual(
                            test_request.error_type,
                            test_input['error']['type'],
                            msg='New SessionEndedRequest has an incorrect error_type')
