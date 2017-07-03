import unittest

import alexa.session

from .. import generate_application_id


class ApplicationTestsMixin:

    BASE_INPUT = {
        'applicationId': '',
    }

    def setUp(self):
        # Randomize some input and create an Application

        self.test_input['applicationId'] = generate_application_id()

        self.application = alexa.session.Application(self.test_input)

    def test_default_attributes(self):
        # All Application objects should have these attributes

        for attribute in ['application_id', ]:
            self.assertTrue(
                hasattr(self.application, attribute),
                msg="Application is missing expected attribute '{attribute}'".format(
                    attribute=attribute))

        self.assertEqual(
            self.application.application_id, self.test_input['applicationId'],
            msg="Application attribute 'application_id' equals '{actual}'; expected '{expected}'".format(
                actual=self.application.application_id,
                expected=self.test_input['applicationId']))


class SimpleApplication(ApplicationTestsMixin, unittest.TestCase):

    test_input = ApplicationTestsMixin.BASE_INPUT
