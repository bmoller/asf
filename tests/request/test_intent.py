import unittest

import alexa.request

from .. import generate_confirmation_status


class IntentTestsMixin:

    BASE_INPUT = {
        'name': 'my_sweet_intent',
        'confirmationStatus': '',
    }

    def setUp(self):
        # Randomize some input and create an Intent

        self.test_input['confirmationStatus'] = generate_confirmation_status()

        self.intent = alexa.request.Intent(self.test_input)

    def test_default_attributes(self):
        # All Intents should have these attributes

        for attribute, expected_value in [
            ('confirmation_status', self.test_input['confirmationStatus']),
            ('name', self.test_input['name']),
        ]:

            self.assertTrue(
                hasattr(self.intent, attribute),
                msg="Intent is missing expected attribute '{attribute}'".format(
                    attribute=attribute))

            self.assertEqual(
                getattr(self.intent, attribute), expected_value,
                msg="Intent attribute '{attribute}' equals '{actual}'; expected '{expected}'".format(
                    attribute=attribute,
                    actual=getattr(self.intent, attribute),
                    expected=expected_value))

        self.assertTrue(
            hasattr(self.intent, 'slots'),
            msg="Intent is missing expected attribute 'slots'")

    def test_slots_attribute(self):
        # Check Slot count if it's applicable

        if 'slots' not in self.test_input:
            return

        self.assertEqual(
            len(self.intent.slots), len(self.test_input['slots']),
            msg="Intent has {actual} slots; expected {expected}".format(
                actual=len(self.intent.slots),
                expected=len(self.test_input['slots'])))


class SimpleIntent(IntentTestsMixin, unittest.TestCase):

    test_input = IntentTestsMixin.BASE_INPUT


class IntentWithSlots(IntentTestsMixin, unittest.TestCase):

    test_input = IntentTestsMixin.BASE_INPUT
    test_input['slots'] = {
        'slot_1': {
            'name': 'slot_1',
            'value': 'value_1',
            'confirmationStatus': '',
        },
        'slot_2': {
            'name': 'slot_2',
            'value': 'value_2',
            'confirmationStatus': '',
        },
        'slot_3': {
            'name': 'slot_3',
            'value': 'value_3',
            'confirmationStatus': '',
        },
    }
