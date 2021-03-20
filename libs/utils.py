import uuid
from models import User


def generate_uuid():
    return str(uuid.uuid4())

def check_if_user(param, value):
    return User.query.filter(getattr(User, param) == value).first()