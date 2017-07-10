import pprint
import unittest

import alexa.response


class CardTestsMixin:

    CARD_TEXT = 'This is some sweet card content'
    CARD_TITLE = 'This is a sweet card title'
    IMAGE_URL = 'https://coolstuff.com/one/sweet/image.jpg'

    def setUp(self):
        # Create a Card

        self.card = alexa.response.Card(*self.args, **self.kwargs)

    def test_attributes(self):
        # Check specified attributes for existence and value

        for attribute, expected_value in self.attributes:

            self.assertTrue(
                hasattr(self.card, attribute),
                msg="Card is missing expected attribute '{attribute}'".format(
                    attribute=attribute))

            self.assertEqual(
                getattr(self.card, attribute), expected_value,
                msg="Card attribute '{attribute}' equals '{actual}'; expected '{expected}'".format(
                    attribute=attribute, actual=getattr(self.card, attribute),
                    expected=expected_value))

    def test_render_method(self):
        # Check that dict output matches the expected value

        self.assertEqual(
            sorted(self.card.render()), sorted(self.output),
            msg='Rendered Card output is incorrect'
        )


class SimpleCard(CardTestsMixin, unittest.TestCase):

    args = [
        CardTestsMixin.CARD_TEXT,
    ]

    kwargs = {}

    attributes = [
        ('text', CardTestsMixin.CARD_TEXT),
    ]

    output = {
        'content': CardTestsMixin.CARD_TEXT,
        'type': 'Simple',
    }


class SimpleCardWithTitle(CardTestsMixin, unittest.TestCase):

    args = [
        CardTestsMixin.CARD_TEXT,
    ]

    kwargs = {
        'title': CardTestsMixin.CARD_TITLE,
    }

    attributes = [
        ('text', CardTestsMixin.CARD_TEXT),
        ('title', CardTestsMixin.CARD_TITLE),
    ]

    output = {
        'content': CardTestsMixin.CARD_TEXT,
        'title': CardTestsMixin.CARD_TITLE,
        'type': 'Simple',
    }


class StandardCardWithImages(CardTestsMixin, unittest.TestCase):

    args = [
        CardTestsMixin.CARD_TEXT,
    ]

    kwargs = {
        'small_image': CardTestsMixin.IMAGE_URL,
        'large_image': CardTestsMixin.IMAGE_URL,
    }

    attributes = [
        ('text', CardTestsMixin.CARD_TEXT),
        ('small_image', CardTestsMixin.IMAGE_URL),
        ('large_image', CardTestsMixin.IMAGE_URL),
    ]

    output = {
        'text': CardTestsMixin.CARD_TEXT,
        'image': {
            'smallImageUrl': CardTestsMixin.IMAGE_URL,
            'largeImageUrl': CardTestsMixin.IMAGE_URL,
        },
        'type': 'Standard',
    }


class StandardCardWithEverything(CardTestsMixin, unittest.TestCase):

    args = [
        CardTestsMixin.CARD_TEXT,
    ]

    kwargs = {
        'title': CardTestsMixin.CARD_TITLE,
        'small_image': CardTestsMixin.IMAGE_URL,
        'large_image': CardTestsMixin.IMAGE_URL,
    }

    attributes = [
        ('text', CardTestsMixin.CARD_TEXT),
        ('title', CardTestsMixin.CARD_TITLE),
        ('small_image', CardTestsMixin.IMAGE_URL),
        ('large_image', CardTestsMixin.IMAGE_URL),
    ]

    output = {
        'text': CardTestsMixin.CARD_TEXT,
        'image': {
            'smallImageUrl': CardTestsMixin.IMAGE_URL,
            'largeImageUrl': CardTestsMixin.IMAGE_URL,
        },
        'title': CardTestsMixin.CARD_TITLE,
        'type': 'Standard',
    }
