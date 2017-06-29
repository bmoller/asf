

class Context:

    def __init__(self, context_data: dict):
        """Creates a new Alexa interaction context
        
        :param context_data:
            The 'context' object from the event passed by the Lambda service to
            the function entry point
        """

        supports_streaming = 'AudioPlayer' in context_data['System']['device']['supportedInterfaces']
        self.device = Device(
            context_data['System']['device']['deviceId'],
            supports_streaming=supports_streaming)


class Device:

    def __init__(self, device_id: str, supports_streaming: bool=False):
        """Creates a new device with the specified ID
        
        :param device_id: ID of the Echo device
        :param supports_streaming:
            Indicates if the requesting device supports the AudioPlayer
            interface
        """

        self.device_id = device_id
        self.supports_streaming = supports_streaming
