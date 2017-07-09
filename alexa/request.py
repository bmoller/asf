

class Request:

    def __init__(self, request_data: dict):
        """Creates a new Alexa request
        
        :param request_data:
            The 'request' object from the event passed by the Lambda service to
            the entry function
        """

        self.locale = request_data['locale']
        self.request_id = request_data['requestId']
        self.timestamp = request_data['timestamp']
        self.request_type = request_data['type']


class IntentRequest(Request):

    def __init__(self, request_data: dict):
        """Creates a new Alexa IntentRequest

        :param request_data:
            The 'request' object from the event passed by the Lambda service to
            the entry function
        """

        super().__init__(request_data)

        self.intent = Intent(request_data['intent'])
        if 'dialogState' in request_data:
            self.dialog_state = request_data['dialogState']


class Intent:

    def __init__(self, intent_data: dict):
        """Creates a new Intent

        :param intent_data:
            The 'intent' object from the 'request' object in the Lambda event
        """

        self.confirmation_status = intent_data['confirmationStatus']
        self.name = intent_data['name']

        self.slots = {}
        if 'slots' in intent_data:
            for name, data in intent_data['slots'].items():
                slot = Slot(data)
                self.slots[name] = slot


class Slot:

    def __init__(self, slot_data: dict):
        """Creates a new Slot

        :param slot_data:
            The 'slot' object from an 'intent' object in the Lambda event
        """

        self.confirmation_status = slot_data['confirmationStatus']
        self.name = slot_data['name']
        self.value = slot_data['value']


class SessionEndedRequest(Request):

    def __init__(self, request_data: dict):
        """Creates a new Alexa SessionEndedRequest

        :param request_data:
            The 'request' object from the event passed by the Lambda service to
            the entry function
        """

        super().__init__(request_data)

        self.reason = request_data['reason']

        if 'error' in request_data:
            if 'type' in request_data['error']:
                self.error_type = request_data['error']['type']
            if 'message' in request_data['error']:
                self.error_message = request_data['error']['message']
