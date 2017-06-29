import unittest

import alexa.card


class AlexaCardTestCase(unittest.TestCase):
    """

    """

    def setUp(self):
        """ Set some simple attributes used in multiple places
        """

        self.card_text = 'This is some sweet card content'
        self.card_title = 'This is a sweet card title'
        self.image_url = 'https://coolstuff.com/one/sweet/image.jpg'
        self.bad_types = [
            123,
            (),
            [],
            {},
        ]
        self.bad_urls = {
            'missing_scheme': 'i/dont/have/a/scheme',
            'missing_netloc': 'https:///i/dont/have/a/netloc',
            'bad_scheme': 'this://is/a/bad/scheme',
            'bad_netloc': 'https://this/is/a/bad/netloc',
            'http_scheme': 'http://this.isnt/a/ssl/url',
            'not_jpeg_or_png': 'https://this.image/isnt/a/valid/type.gif',
        }.values()

    def tearDown(self):
        """ Remove the attributes created in test setup
        """

        for attribute in ['card_text', 'card_title', 'image_url', 'bad_types',
                          'bad_urls', ]:
            delattr(self, attribute)

    def test_simple_card(self):
        """ Check that the simple card type returns correctly
        """

        expected_card_output = {
            'type': 'Simple',
            'content': self.card_text,
        }
        card_output = alexa.card.build_card(self.card_text)

        self.assertEqual(card_output, expected_card_output)

    def test_simple_card_with_title(self):
        """ Check that the simple card type returns correctly with a title
        """

        expected_card_output = {
            'type': 'Simple',
            'title': self.card_title,
            'content': self.card_text,
        }
        card_output = alexa.card.build_card(self.card_text,
                                            title=self.card_title)

        self.assertEqual(card_output, expected_card_output)

    def test_standard_card_with_images(self):
        """ Check that the standard card type returns correctly with images
        """

        for image_type in [('small_image', 'smallImageUrl'),
                           ('large_image', 'largeImageUrl'), ]:

            with self.subTest(image_type=image_type):
                expected_card_output = {
                    'type': 'Standard',
                    'text': self.card_text,
                    'image': {
                        image_type[1]: self.image_url,
                    },
                }
                image_parameter = {
                    image_type[0]: self.image_url,
                }
                card_output = alexa.card.build_card(self.card_text,
                                                    **image_parameter)

                self.assertEqual(card_output, expected_card_output)

        with self.subTest():
            expected_card_output = {
                'type': 'Standard',
                'text': self.card_text,
                'image': {
                    'smallImageUrl': self.image_url,
                    'largeImageUrl': self.image_url,
                },
            }
            card_output = alexa.card.build_card(self.card_text,
                                                small_image=self.image_url,
                                                large_image=self.image_url)

            self.assertEqual(card_output, expected_card_output)

        with self.subTest():
            expected_card_output = {
                'type': 'Standard',
                'text': self.card_text,
                'title': self.card_title,
                'image': {
                    'smallImageUrl': self.image_url,
                    'largeImageUrl': self.image_url,
                },
            }
            card_output = alexa.card.build_card(self.card_text,
                                                title=self.card_title,
                                                small_image=self.image_url,
                                                large_image=self.image_url)

            self.assertEqual(card_output, expected_card_output)

    def test_nonstring_parameters_raise_exceptions(self):
        """ Check that nonstring parameters to card creation raise exceptions
        """

        for bad_type in self.bad_types:

            with self.subTest(card_text=bad_type):
                with self.assertRaises(TypeError):
                    alexa.card.build_card(bad_type)

            with self.subTest(card_title=bad_type):
                with self.assertRaises(TypeError):
                    alexa.card.build_card(self.card_text, title=bad_type)

            with self.subTest(small_image=bad_type):
                with self.assertRaises(TypeError):
                    alexa.card.build_card(self.card_text, small_image=bad_type)

            with self.subTest(large_image=bad_type):
                with self.assertRaises(TypeError):
                    alexa.card.build_card(self.card_text, large_image=bad_type)

    def test_bad_image_urls_raise_an_exception(self):
        """ Check that various URL's of invalid format raise exceptions
        """

        for bad_url in self.bad_urls:

            with self.subTest(small_image_url=bad_url):
                with self.assertRaises(ValueError):
                    alexa.card.build_card(self.card_text, small_image=bad_url)

            with self.subTest(large_image_url=bad_url):
                with self.assertRaises(ValueError):
                    alexa.card.build_card(self.card_text, large_image=bad_url)

    def test_check_image_url_method(self):
        """ Check that the image URL check method raises exceptions when appropriate
        """

        for bad_url in self.bad_urls:
            with self.subTest(url=bad_url):
                with self.assertRaises(ValueError):
                    alexa.card._check_image_url(bad_url)
