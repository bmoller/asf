import unittest

import alexa.context

from .. import generate_application_id, generate_device_id, generate_user_id


class ContextTests:

    BASE_INPUT = {
        'AudioPlayer': {
            'playerActivity': 'IDLE',
        },
        'System': {
            'apiEndpoint': 'https://api.amazonalexa.com',
            'application': {
                'applicationId': '',
            },
            'device': {
                'deviceId': '',
                'supportedInterfaces': {
                    'AudioPlayer': {},
                }
            },
            'user': {
                'userId': '',
            },
        },
    }

    def setUp(self):
        """Set some class attributes used across multiple tests"""

        self.test_input['System']['application']['applicationId'] = generate_application_id()
        self.test_input['System']['device']['deviceId'] = generate_device_id()
        self.test_input['System']['user']['userId'] = generate_user_id()

        self.context = alexa.context.Context(self.test_input)

    def test_default_attributes(self):
        # All Context objects should have these attributes

        for attribute in ['device', ]:
            self.assertTrue(
                hasattr(self.context, attribute),
                msg="Context object is missing expected attribute '{attribute}'".format(
                    attribute=attribute))


class SimpleContext(ContextTests, unittest.TestCase):

    test_input = ContextTests.BASE_INPUT
