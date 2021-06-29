from flask import request, jsonify
from . import state_machine as ssm
from libs import helpers
from platform_service import authorize
from services_module import services


@services.route('/', methods=['POST'])
@authorize.authorize
def create_service(current_user):
    return ssm.create()


@services.route('/getall', methods=['GET'])
@authorize.authorize
def get_all_service(current_user):
    res = ssm.get_all_profiles(current_user)
    return helpers.respond(res, 200)
