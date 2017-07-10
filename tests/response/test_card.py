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

        msg = [
            'Card rendered the output: {output}'.format(
                output=pprint.pformat(sorted(self.card.render()))),
            'Expected output: {expected}'.format(
                expected=pprint.pformat(sorted(self.output))),
        ]

        self.assertEqual(
            sorted(self.card.render()), sorted(self.output),
            msg='\n'.join(msg)
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
