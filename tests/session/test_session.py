import unittest

import alexa.session

from .. import (
    generate_access_token, generate_application_id, generate_consent_token,
    generate_session_id, generate_user_id)


class SessionTests:

    BASE_INPUT = {
        'application': {
            'applicationId': '',
        },
        'new': True,
        'sessionId': '',
        'user': {
            'userId': '',
            'permissions': {
                'consentToken': ''
            },
            'accessToken': '',
        },
    }

    def setUp(self):
        # Randomize some input and create a Session

        self.test_input['application']['applicationId'] = generate_application_id()
        self.test_input['sessionId'] = generate_session_id()
        self.test_input['user']['userId'] = generate_user_id()
        self.test_input['user']['permissions']['consentToken'] = generate_consent_token()
        self.test_input['user']['accessToken'] = generate_access_token()

        self.session = alexa.session.Session(self.test_input)

    def test_default_attributes(self):
        # All Session objects should have these attributes

        for attribute in ['new', 'session_id', 'application', 'user', ]:
            self.assertTrue(
                hasattr(self.session, attribute),
                msg="Session object is missing expected attribute '{attribute}'".format(
                    attribute=attribute))

        self.assertEqual(
            self.session.new, self.test_input['new'],
            msg="Session attribute 'new' equals '{actual}', expected '{expected}'".format(
                actual=str(self.session.new),
                expected=str(self.test_input['new'])))

        self.assertEqual(
            self.session.session_id, self.test_input['sessionId'],
            msg="Session attribute 'session_id' equals '{actual}', expected '{expected}'".format(
                actual=str(self.session.session_id),
                expected=str(self.test_input['sessionId'])))

    def test_alexa_session_attributes(self):
        # Check any attributes that exist in the input data

        if 'attributes' in self.test_input:
            for attribute, value in self.test_input['attributes'].items():
                self.assertTrue(hasattr(self.session, attribute))
                self.assertEqual(getattr(self.session, attribute), value)


class SimpleSession(SessionTests, unittest.TestCase):
    """Test a Session object with the simple base input"""

    test_input = SessionTests.BASE_INPUT


class SessionWithAttributes(SessionTests, unittest.TestCase):
    """Test a Session object that has some persistent attributes"""

    test_input = SessionTests.BASE_INPUT
    test_input['attributes'] = {
        'attribute1': 'value1',
        'attribute2': 'value2',
        'attribute3': 'value3',
    }
