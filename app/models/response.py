class Response:
    def __init__(self, success, data = None, error = None, message = None):
        self.success = success
        self.data = data
        self.error = error
        self.message = message

    def to_json(self):
        return self.__dict__
