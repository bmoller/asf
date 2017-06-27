import unittest

import alexa.user


class AlexaUserTestCase(unittest.TestCase):

    def setUp(self):
        """ Set some class attributes that are used across multiple tests
        """

        self.user_id = 'amzn1.ask.account.HCECOV3JK4DJHF84VI7H0EFN6WFH6OSI29HB65JCJAQAXPAPWS4NAV1VR6QSP65SY0523OVNOKBMY4LM8LNW40JH4MD2LVL1XXA67FOKYJZVFEE9DW6XTX2RB6SS4KOB2080ES12T7PC0TWY5QLH935XWA1N6UM48HUOW4OS9MXU81R9M8AZS3OVV3XZGYXYTT1DP4HZQ3EGDL1'
        self.consent_token = 'Atza|MQEWY...6fnLok'

    def tearDown(self):
        """ Remove class attributes that were created at setup
        """

        for attribute in ['user_id', 'consent_token', ]:
            delattr(self, attribute)

    def test_user_creation(self):
        """ Check that a new User returns the attributes it was created with
        """

        test_user = alexa.user.User(self.user_id,
                                    consent_token=self.consent_token)

        with self.subTest(attribute='User.id'):
            self.assertEqual(test_user.id, self.user_id)
        with self.subTest(attribute='User.consent_token'):
            self.assertEqual(test_user.consent_token, self.consent_token)
