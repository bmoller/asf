import unittest

import alexa.session

from . import (
    generate_access_token, generate_application_id, generate_consent_token,
    generate_session_id, generate_user_id)

ACCESS_TOKEN = generate_access_token()
APPLICATION_ID = generate_application_id()
CONSENT_TOKEN = generate_consent_token()
SESSION_ID = generate_session_id()
USER_ID = generate_user_id()


class AlexaSessionTestCase(unittest.TestCase):

    def setUp(self):
        """Set some attributes used across multiple tests"""

        self.application_id = APPLICATION_ID
        self.session_id = SESSION_ID
        self.user_id = USER_ID

        self.session_attributes = {
            'attribute1': 'value1',
            'attribute2': 'value2',
            'attribute3': 'value3',
        }

        self.test_inputs = {
            'Simple New Session': {
                'application': {
                    'applicationId': self.application_id,
                },
                'new': True,
                'sessionId': self.session_id,
                'user': {
                    'userId': self.user_id,
                }
            }
        }

    def tearDown(self):
        """Remove attributes added at setup"""

        for attribute in [
                'application_id', 'session_id', 'session_attributes', ]:
            delattr(self, attribute)

    def test_session_creation(self):
        """Test creation of a session object with various parameters"""

        for test_case, test_input in self.test_inputs.items():

            test_session = alexa.session.Session(test_input)

            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_session.application.application_id,
                    test_input['application']['applicationId'],
                    msg='Application in new Session has an incorrect application_id')

            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_session.new, test_input['new'],
                    msg='New Session has an incorrect \'new\' attribute')

            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_session.session_id, test_input['sessionId'],
                    msg='New Session has an incorrect session_id')

            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_session.user.user_id, test_input['user']['userId'],
                    msg='User in new Session has an incorrect user_id')


class AlexaApplicationTestCase(unittest.TestCase):

    def setUp(self):
        """Set some class attributes used across multiple tests"""

        self.application_id = APPLICATION_ID

    def tearDown(self):
        """Remove class attributes created at setup"""

        for attribute in ['application_id', ]:
            delattr(self, attribute)

    def test_application_creation(self):
        """Check creation of new Application objects"""

        test_application = alexa.session.Application(self.application_id)
        self.assertEqual(
            test_application.application_id, self.application_id,
            msg='New Application has an incorrect application_id')


class AlexaUserTestCase(unittest.TestCase):

    def setUp(self):
        """Set some class attributes used across multiple tests"""

        self.user_id = USER_ID
        self.consent_token = CONSENT_TOKEN
        self.access_token = ACCESS_TOKEN

        self.test_inputs = {
            'User ID Only': {
                'user_id': self.user_id,
                'consent_token': None,
                'access_token': None,
            },
            'User ID and Consent Token': {
                'user_id': self.user_id,
                'consent_token': self.consent_token,
                'access_token': None,
            },
            'User ID and Access Token': {
                'user_id': self.user_id,
                'consent_token': None,
                'access_token': self.access_token,
            },
            'User ID, Consent Token, and Access Token': {
                'user_id': self.user_id,
                'consent_token': self.consent_token,
                'access_token': self.access_token,
            },
        }

    def tearDown(self):
        """Remove class attributes created at setup"""

        for attribute in ['user_id', 'consent_token', 'access_token', ]:
            delattr(self, attribute)

    def test_user_creation(self):
        """Check creation of new User objects"""

        for test_case, test_input in self.test_inputs.items():

            test_user = alexa.session.User(
                test_input['user_id'],
                consent_token=test_input['consent_token'],
                access_token=test_input['access_token']
            )

            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_user.user_id, self.user_id,
                    msg='New User has an incorrect user_id')

            if test_input['consent_token']:
                with self.subTest(test_case=test_case):
                    self.assertEqual(
                        test_user.consent_token, self.consent_token,
                        msg='New User has an incorrect consent_token')
            else:
                with self.subTest(test_case=test_case):
                    self.assertFalse(
                        hasattr(test_user, 'consent_token'),
                        msg='New User has a consent_token when none was provided')

            if test_input['access_token']:
                with self.subTest(test_case=test_case):
                    self.assertEqual(
                        test_user.access_token, self.access_token,
                        msg='New User has an incorrect access_token')
            else:
                with self.subTest(test_case=test_case):
                    self.assertFalse(
                        hasattr(test_user, 'access_token'),
                        msg='New User has a access_token when none was provided')
