from flask import request
from . import state_machine as ssm
from platform_service import authorize
from services_module import services

@services.route('/', methods=['POST'])
@authorize.authorize
def create_service(current_user):
    return ssm.create()