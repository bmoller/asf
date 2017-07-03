import unittest

import alexa.context

from .. import generate_device_id


class DeviceTestsMixin:

    BASE_INPUT = {
        'deviceId': '',
        'supportedInterfaces': {},
    }

    def setUp(self):
        # Randomize some input and create a Device

        self.test_input['deviceId'] = generate_device_id()

        self.device = alexa.context.Device(self.test_input)

    def test_default_attributes(self):
        # All Device objects should have these attributes

        for attribute in ['device_id', 'supports_streaming', ]:
            self.assertTrue(
                hasattr(self.device, attribute),
                msg="Device object is missing expected attribute '{attribute}'".format(
                    attribute=attribute))

        for attribute, actual_value, expected_value in [
            ('device_id', self.device.device_id, self.test_input['deviceId']),
            ('supports_streaming', self.device.supports_streaming,
                'AudioPlayer' in self.test_input['supportedInterfaces']),
        ]:
            self.assertEqual(
                actual_value, expected_value,
                msg="Device attribute '{attribute}' equals '{actual}', expected '{expected}'".format(
                    attribute=attribute, actual=actual_value,
                    expected=expected_value))


class NoStreamingSupport(DeviceTestsMixin, unittest.TestCase):

    test_input = DeviceTestsMixin.BASE_INPUT


class StreamingSupport(DeviceTestsMixin, unittest.TestCase):

    test_input = DeviceTestsMixin.BASE_INPUT
    test_input['supportedInterfaces']['AudioPlayer'] = {}
