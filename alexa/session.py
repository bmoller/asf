

class Session:

    def __init__(self, session_id: str, application_id: str, new: bool=True,
                 attributes: dict=None):

        self.session_id = session_id
        self.application_id = application_id

        if new:
            self.new = True
        else:
            self.new = False

        if attributes:
            for attribute, value in attributes.items():
                setattr(self, attribute, value)
