import datetime
import unittest

import alexa.request

from . import generate_request_id


class AlexaRequestTestCase(unittest.TestCase):

    def setUp(self):
        """Set attributes used in multiple places"""

        self.request_id = generate_request_id()

        right_now = datetime.datetime.now(tz=datetime.timezone.utc)
        self.timestamp = right_now.strftime('%Y-%m-%dT%H:%M:%SZ')

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
