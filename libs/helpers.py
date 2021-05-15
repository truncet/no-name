from platform_service import serializers
import random, string

class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

def assert_found(instance, message='Not Found', status_code=404):
    if instance == None:
        raise InvalidUsage(message, status_code=status_code)

def assert_true(condition, message='Forbidden', status_code=403):
    if condition == False: 
        raise InvalidUsage(message, status_code=status_code)

def assert_valid(condition, message='Bad Request', status_code=400):
    if condition == False: 
        raise InvalidUsage(message, status_code=status_code)

def respond(object_instance, status_code):
    result = serializers.serialize(object_instance)
    return result, status_code

def random_word(length):
   alpha_numerals = string.ascii_letters + string.digits
   return ''.join(random.choice(alpha_numerals) for i in range(length))   