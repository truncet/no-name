from  flask import request, jsonify
from . import state_machine as usm
from platform_service import authorize, serializers
from users_module import users
from libs import helpers


@users.route('/', methods=['POST'])
@authorize.authorize
def register_user(current_user):
    res, code= usm.check_register_user(current_user)
    return helpers.responsd(res, code)



@users.route('/profile' , methods=['GET'])
@authorize.authorize
def show_profile(current_user):
    res =  usm.show_user_profile(current_user)
    helpers.assert_found(res, message="User doesn't exist.")
    return helpers.respond(res, 200)



@users.route('/profile', methods=['PUT'])
@authorize.authorize
def complete_profile(current_user):
    payload = serializers.deserialize(request.json)
    helpers.assert_true(payload.username!=None, "Invalid username")
    helpers.assert_true(payload.location!=None, "Invalid location")
    helpers.assert_true(payload.phone!=None, "Invalid phone")
    print ('go to function')
    res,code = usm.complete_user_profile(current_user, payload) 
    return helpers.respond(res,code)


@users.route('/home', methods=['GET'])
def home_page():
    return jsonify({'message':'this seems to be user home page'})
    
