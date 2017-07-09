import unittest

import alexa.request

from .. import generate_confirmation_status


class SlotTestsMixin:

    BASE_INPUT = {
        'name': 'simple_slot',
        'value': 'simple_value',
        'confirmationStatus': '',
    }

    def setUp(self):
        # Randomize some input and create a Slot

        self.test_input['confirmationStatus'] = generate_confirmation_status()

        self.slot = alexa.request.Slot(self.test_input)

    def test_default_attributes(self):
        # All Slots should have these attributes

        for attribute, expected_value in [
            ('name', self.test_input['name']),
            ('value', self.test_input['value']),
            ('confirmation_status', self.test_input['confirmationStatus']),
        ]:

            self.assertTrue(
                hasattr(self.slot, attribute),
                msg="Slot is missing expected attribute '{attribute}'".format(
                    attribute=attribute))

            self.assertEqual(
                getattr(self.slot, attribute), expected_value,
                msg="Slot attribute '{attribute}' equals '{actual}'; expected '{expected}'".format(
                    attribute=attribute, actual=getattr(self.slot, attribute),
                    expected=expected_value))


class SimpleSlot(SlotTestsMixin, unittest.TestCase):

    test_input = SlotTestsMixin.BASE_INPUT
