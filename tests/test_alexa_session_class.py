import unittest
import uuid

import alexa.session


class AlexaSessionTestCase(unittest.TestCase):

    def setUp(self):
        """Set some attributes used across multiple tests"""

        self.application_id = '.'.join(['amzn1.ask.skill', str(uuid.uuid4())])
        self.session_id = '.'.join(['amzn1.echo-api.session', str(uuid.uuid4())])

        self.session_attributes = {
            'attribute1': 'value1',
            'attribute2': 'value2',
            'attribute3': 'value3',
        }

    def tearDown(self):
        """Remove attributes added at setup"""

        for attribute in [
                'application_id', 'session_id', 'session_attributes', ]:
            delattr(self, attribute)

    def test_session_creation(self):
        """Test creation of a session object with various parameters"""

        test_session = alexa.session.Session(
            self.session_id, self.application_id)

        with self.subTest(attribute='session_id'):
            self.assertEqual(test_session.session_id, self.session_id)
        with self.subTest(attribute='application_id'):
            self.assertEqual(test_session.application_id, self.application_id)
        with self.subTest(attribute='new'):
            self.assertTrue(test_session.new)

        test_session = alexa.session.Session(
            self.session_id, self.application_id, new=False)

        with self.subTest(attribute='session_id'):
            self.assertEqual(test_session.session_id, self.session_id)
        with self.subTest(attribute='application_id'):
            self.assertEqual(test_session.application_id, self.application_id)
        with self.subTest(attribute='new'):
            self.assertFalse(test_session.new)

        test_session = alexa.session.Session(
            self.session_id, self.application_id,
            attributes=self.session_attributes)

        with self.subTest(attribute='session_id'):
            self.assertEqual(test_session.session_id, self.session_id)
        with self.subTest(attribute='application_id'):
            self.assertEqual(test_session.application_id, self.application_id)
        with self.subTest(attribute='new'):
            self.assertTrue(test_session.new)

        for attribute, value in self.session_attributes.items():
            with self.subTest(has_attribute=attribute):
                self.assertTrue(hasattr(test_session, attribute))
            with self.subTest(attribute=attribute):
                self.assertEqual(getattr(test_session, attribute), value)

        test_session = alexa.session.Session(
            self.session_id, self.application_id, new=False,
            attributes=self.session_attributes)

        with self.subTest(attribute='session_id'):
            self.assertEqual(test_session.session_id, self.session_id)
        with self.subTest(attribute='application_id'):
            self.assertEqual(test_session.application_id, self.application_id)
        with self.subTest(attribute='new'):
            self.assertFalse(test_session.new)

        for attribute, value in self.session_attributes.items():
            with self.subTest(has_attribute=attribute):
                self.assertTrue(hasattr(test_session, attribute))
            with self.subTest(attribute=attribute):
                self.assertEqual(getattr(test_session, attribute), value)
