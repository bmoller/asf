import unittest
import uuid

import alexa.context

ACCESS_TOKEN = 'laksfdqiohjweipobqvcljakhnfioquwefoiu'
APPLICATION_ID = '.'.join(['amzn1.ask.skill', str(uuid.uuid4())])
CONSENT_TOKEN = 'Atza|MQEWY...6fnLok'
USER_ID = 'amzn1.ask.account.HCECOV3JK4DJHF84VI7H0EFN6WFH6OSI29HB65JCJAQAXPAPWS4NAV1VR6QSP65SY0523OVNOKBMY4LM8LNW40JH4MD2LVL1XXA67FOKYJZVFEE9DW6XTX2RB6SS4KOB2080ES12T7PC0TWY5QLH935XWA1N6UM48HUOW4OS9MXU81R9M8AZS3OVV3XZGYXYTT1DP4HZQ3EGDL1'


class AlexaApplicationTestCase(unittest.TestCase):

    def setUp(self):
        """Set some class attributes used across multiple tests"""

        self.application_id = APPLICATION_ID

    def tearDown(self):
        """Remove class attributes created at setup"""

        for attribute in ['application_id', ]:
            delattr(self, attribute)

    def test_application_creation(self):
        


class AlexaUserTestCase(unittest.TestCase):

    def setUp(self):
        """Set some class attributes used across multiple tests"""

        self.user_id = USER_ID
        self.consent_token = CONSENT_TOKEN
        self.access_token = ACCESS_TOKEN

    def tearDown(self):
        """Remove class attributes created at setup"""

        for attribute in ['user_id', 'consent_token', 'access_token', ]:
            delattr(self, attribute)

    def test_user_creation(self):
        """Check that a new User returns the attributes it was created with"""

        test_user = alexa.context.User(
            self.user_id, consent_token=self.consent_token,
            access_token=self.access_token)

        with self.subTest(attribute='User.id'):
            self.assertEqual(test_user.user_id, self.user_id)
        with self.subTest(attribute='User.consent_token'):
            self.assertEqual(test_user.consent_token, self.consent_token)


class AlexaContextTestCase(unittest.TestCase):

    def setUp(self):

        self.application_id = APPLICATION_ID

        self.test_context_data = {
            'context': {
                'AudioPlayer': {
                    'playerActivity': 'IDLE'
                },
                'System': {
                    'apiEndpoint': 'https://api.amazonalexa.com',
                    'application': {
                        'applicationId': self.application_id,
                    },
                    'device': {
                        'deviceId': 'amzn1.ask.device.AHGKIGP465ETRXX2V6J3W7LI7P2AUJWDHJZ3Z44JANKODIG2TJKCRDQNPZKKU5JTGDWZJHXP3V2K3UCSWUUGAPU7NTFS6DBJKTNGD67DWM3LCHOTDE35PRXZCHQWVHHTDRGNE7UYMAYMZREKUGQSQM7KUWFA',
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
