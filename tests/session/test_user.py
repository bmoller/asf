import unittest

import alexa.session

from .. import generate_access_token, generate_consent_token, generate_user_id


class UserTests:

    BASE_INPUT = {
        'userId': '',
    }

    def setUp(self):
        # Randomize some inputs, create a User

        self.test_input['userId'] = generate_user_id()

        self.user = alexa.session.User(self.test_input)

    def test_default_attributes(self):
        # All User objects should have these attributes

        self.assertTrue(hasattr(self.user, 'user_id'))
        self.assertEqual(self.user.user_id, self.test_input['userId'])

    def test_consent_token(self):
        # Check the consent token, if it exists

        if 'permissions' not in self.test_input:
            self.assertFalse(
                hasattr(self.user, 'consent_token'),
                msg='User object has unexpected attribute \'consent_token\'')
        elif 'consentToken' not in self.test_input['permissions']:
            self.assertFalse(
                hasattr(self.user, 'consent_token'),
                msg='User object has unexpected attribute \'consent_token\'')
        else:
            self.assertTrue(
                hasattr(self.user, 'consent_token'),
                msg='User object is missing expected attribute \'consent_token\'')
            self.assertEqual(
                self.user.consent_token,
                self.test_input['permissions']['consentToken'],
                msg='User attribute \'consent_token\' equals \'{actual}\', expected \'{expected}\''.format(
                    actual=str(self.user.consent_token),
                    expected=self.test_input['permissions']['consentToken']))

    def test_access_token(self):
        # Check the access token, if it exists

        if 'accessToken' not in self.test_input:
            self.assertFalse(
                hasattr(self.user, 'access_token'),
                msg='User object has unexpected attribute \'access_token\'')
        else:
            self.assertTrue(
                hasattr(self.user, 'access_token'),
                msg='User object is missing expected attribute \'access_token\'')
            self.assertEqual(
                self.user.access_token, self.test_input['accessToken'],
                msg='User attribute \'access_token\' equals \'{actual}\', expected \'{expected}\''.format(
                    actual=str(self.user.access_token),
                    expected=self.test_input['accessToken']))


class TestSimpleUser(UserTests, unittest.TestCase):

    test_input = UserTests.BASE_INPUT


class TestUserWithConsentToken(UserTests, unittest.TestCase):

    test_input = UserTests.BASE_INPUT
    test_input['permissions'] = {
        'consentToken': generate_consent_token(),
    }


class TestUserWithAccessToken(UserTests, unittest.TestCase):

    test_input = UserTests.BASE_INPUT
    test_input['accessToken'] = generate_access_token()


class TestUserWithEverything(UserTests, unittest.TestCase):

    test_input = UserTests.BASE_INPUT
    test_input['permissions'] = {
        'consentToken': generate_consent_token(),
    }
    test_input['accessToken'] = generate_access_token()
