from threading import currentThread
from flask import request
from . import state_machine as rsm
from platform_service import authorize
from roles_module import roles
from libs import helpers


@roles.route('/', methods=['POST'])
@authorize.authorize
def create_role(current_user):
    print(current_user)

    role_name = request.json.get('role_name')
    res, code = rsm.create_role(role_name)
    return res, code


@roles.route('/', methods=['GET'])
@authorize.authorize
def get_roles(current_user):
    res = rsm.get_roles()
    helpers.assert_found(res, message="No Roles found.")
    return helpers.respond(res, 200)


@roles.route('/get', methods=['GET'])
@authorize.authorize
def get_role_individual(current_user):
    res, code = rsm.get_my_role(current_user)
    helpers.assert_found(res, message="No Roles found")
    return res, code
