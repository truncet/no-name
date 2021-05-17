from flask import request
from . import state_machine as rsm
from platform_service import authorize
from roles_module import roles


@roles.route('/', methods=['POST'])
@authorize.authorize
def create_role(current_user):
    print (current_user)

    role_name = request.json.get('role_name')
    res, code= rsm.create_role(role_name)
    return res, code