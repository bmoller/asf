import unittest

import alexa.context

from . import (
    generate_access_token, generate_application_id, generate_consent_token,
    generate_device_id, generate_user_id)

ACCESS_TOKEN = generate_access_token()
APPLICATION_ID = generate_application_id()
CONSENT_TOKEN = generate_consent_token()
DEVICE_ID = generate_device_id()
USER_ID = generate_user_id()


class AlexaContextTestCase(unittest.TestCase):

    def setUp(self):
        """Set some class attributes used across multiple tests"""

        self.application_id = APPLICATION_ID
        self.device_id = DEVICE_ID
        self.user_id = USER_ID

        self.context_creation_test_cases = {
            'Basic Context': {
                'AudioPlayer': {
                    'playerActivity': 'IDLE'
                },
                'System': {
                    'apiEndpoint': 'https://api.amazonalexa.com',
                    'application': {
                        'applicationId': self.application_id,
                    },
                    'device': {
                        'deviceId': self.device_id,
                        'supportedInterfaces': {
                            'AudioPlayer': {}
                        },
                    },
                    'user': {
                        'userId': self.user_id
                    },
                },
            },
        }

    def tearDown(self):
        """Remove class attributes created at setup"""

        for attribute in [
                'application_id', 'device_id', 'user_id',
                'context_creation_test_cases', ]:
            delattr(self, attribute)

    def test_context_creation(self):
        """Test creation of new Context objects"""

        for test_case, test_input in self.context_creation_test_cases.items():
            test_context = alexa.context.Context(test_input)

            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_context.device.device_id,
                    test_input['System']['device']['deviceId'],
                    msg='Device in new Context has an incorrect device_id')

            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_context.device.supports_streaming,
                    'AudioPlayer' in test_input['System']['device']['supportedInterfaces'],
                    msg='Device in new Context reports incorrect streaming support')


class AlexaDeviceTestCase(unittest.TestCase):

    def setUp(self):
        """Set some class attributes used across multiple tests"""

        self.device_id = DEVICE_ID

        self.device_creation_test_cases = {
            'No Streaming Support': {
                'device_id': self.device_id,
                'supports_streaming': False,
            },
            'Has Streaming Support': {
                'device_id': self.device_id,
                'supports_streaming': True,
            }
        }

    def tearDown(self):
        """Remove class attributes created at setup"""

        for attribute in ['device_id', 'device_creation_test_cases', ]:
            delattr(self, attribute)

    def test_device_creation(self):
        """Test creation of new Device objects"""

        for test_case, test_input in self.device_creation_test_cases.items():
            test_device = alexa.context.Device(
                test_input['device_id'],
                supports_streaming=test_input['supports_streaming'])

            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_device.device_id, test_input['device_id'],
                    msg='New Device has an incorrect device_id')

            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_device.supports_streaming,
                    test_input['supports_streaming'],
                    msg='New Device reports incorrect streaming support')
