import uuid
from models import User


def generate_uuid():
    return str(uuid.uuid4())

def check_if_user(param, value):
    return User.query.filter(getattr(User, param) == value).first()


def find_by_parameters(**kwargs):
    query = None
    for key, value in kwargs.items():
        if value:
            if type(value) is list:
                ## if value is list, find by in_ condition
                if query == None:
                    query = User.query.filter(getattr(User, key).in_(value))
                else:
                    query = query.filter(getattr(User, key).in_(value))
            else:
                if query == None:
                    query = User.query.filter(getattr(User, key) == value)
                else:
                    query = query.filter(getattr(User, key) == value)
    return query.all()