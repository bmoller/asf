import unittest

import alexa.response


class AlexaCardTestCase(unittest.TestCase):

    def setUp(self):
        """Set some simple attributes used in multiple places"""

        self.card_text = 'This is some sweet card content'
        self.card_title = 'This is a sweet card title'
        self.image_url = 'https://coolstuff.com/one/sweet/image.jpg'

        self.type_check_test_cases = {
            'int Input': 123,
            'tuple Input': (),
            'list Input': [],
            'dict Input': {},
        }

        self.url_check_test_cases = {
            'HTTP Scheme': 'http://this.isnt/a/ssl/url',
            'Invalid Image Type': 'https://this.image/isnt/a/valid/type.gif',
            'Invalid netloc': 'https://this/is/a/bad/netloc',
            'Invalid Scheme': 'this://is/a/bad/scheme',
            'Missing netloc': 'https:///i/dont/have/a/netloc',
            'Missing Scheme': 'i/dont/have/a/scheme',
        }

        self.card_creation_test_cases = {
            'Simple Card': {
                'input': {
                    'args': [
                        self.card_text,
                    ],
                    'kwargs': {},
                },
                'string': {
                    'content': self.card_text,
                    'type': 'Simple',
                }
            },
            'Simple Card with Title': {
                'input': {
                    'args': [
                        self.card_text,
                    ],
                    'kwargs': {
                        'title': self.card_title,
                    },
                },
                'string': {
                    'content': self.card_text,
                    'title': self.card_title,
                    'type': 'Simple',
                },
            }
        }

    def tearDown(self):
        """Remove the attributes created in test setup"""

        for attribute in [
                'card_text', 'card_title', 'image_url', 'url_check_test_cases',
                'type_check_test_cases', 'card_creation_test_cases', ]:
            delattr(self, attribute)

    def test_card_creation(self):
        """Check that the simple card type returns correctly"""

        for test_case, test_parameters in self.card_creation_test_cases.items():
            test_input = test_parameters['input']
            test_card = alexa.response.Card(
                *test_input['args'], **test_input['kwargs'])

            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_card.text, test_input['args'][0],
                    msg='New Card has incorrect text')

            if 'title' in test_input['kwargs']:
                with self.subTest(test_case=test_case):
                    self.assertEqual(
                        test_card.title, test_input['kwargs']['title'],
                        msg='New Card has an incorrect title')

            if 'small_image' in test_input['kwargs']:
                with self.subTest(test_case=test_case):
                    self.assertEqual(
                        test_card.small_image,
                        test_input['kwargs']['small_image'],
                        msg='New Card has an incorrect small_image URL')

            if 'large_image' in test_input['kwargs']:
                with self.subTest(test_case=test_case):
                    self.assertEqual(
                        test_card.large_image,
                        test_input['kwargs']['large_image'],
                        msg='New Card has an incorrect large_image URL')

    def test_nonstring_parameters_raise_exceptions(self):
        """ Check that nonstring parameters to card creation raise exceptions
        """

        for test_case, test_input in self.type_check_test_cases.items():

            with self.subTest(card_text=test_case):
                with self.assertRaises(
                        TypeError,
                        msg='Non-string card text doesn\'t raise an exception'):
                    alexa.response.Card(test_input)

            with self.subTest(card_title=test_case):
                with self.assertRaises(
                        TypeError,
                        msg='Non-string card title doesn\'t raise an exception'):
                    alexa.response.Card(self.card_text, title=test_input)

            with self.subTest(small_image=test_case):
                with self.assertRaises(
                        TypeError,
                        msg='Non-string small image URL doesn\'t raise an exception'):
                    alexa.response.Card(self.card_text, small_image=test_input)

            with self.subTest(large_image=test_case):
                with self.assertRaises(
                        TypeError,
                        msg='Non-string large image URL doesn\'t raise an exception'):
                    alexa.response.Card(self.card_text, large_image=test_input)

    def test_bad_image_urls_raise_an_exception_at_card_creation(self):
        """Check that various URL's of invalid format raise exceptions"""

        for test_case, test_input in self.url_check_test_cases.items():

            with self.subTest(small_image=test_case):
                with self.assertRaises(
                        ValueError,
                        msg='Invalid small image URL doesn\'t raise an exception'):
                    alexa.response.Card(self.card_text, small_image=test_input)

            with self.subTest(large_image=test_case):
                with self.assertRaises(
                        ValueError,
                        msg='Invalid small image URL doesn\'t raise an exception'):
                    alexa.response.Card(self.card_text, large_image=test_input)

    def test_check_image_url_method(self):
        """ Check image URL verification raises exceptions when appropriate"""

        for test_case, test_input in self.url_check_test_cases.items():
            with self.subTest(test_case=test_case):
                with self.assertRaises(
                        ValueError,
                        msg='No exception was raised for a nonstring image URL'):
                    alexa.response.Card._check_image_url(test_input)
