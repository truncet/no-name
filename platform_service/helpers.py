

class InvalidUsage(Exception):

    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

class AlreadyExists(Exception):

    status_code = 400
    message = "Something Went Wrong"

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload



def assert_null(condition, message='Bad Request', status_code=400):
    if condition is False:
        raise InvalidUsage(message, status_code=status_code)

def assert_already_exist(condition, message='Bad Request', status_code=400):
    if condition is False:
        raise AlreadyExists(message, status_code=status_code )