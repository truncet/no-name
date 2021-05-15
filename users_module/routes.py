from  flask import request, jsonify
from . import state_machine as usm
from platform_service import authorize
from users_module import users
from libs import helpers

# @users.route('/user', methods=['GET'])
# @token_required
# def get_current_user_info(current_user):
#     return jsonify({'message':current_user.username + " is logged in"}), 200
    



# @users.route('/book', methods=['GET'])
# @token_required
# def get_current_booking(current_user):
#     return ''


# @users.route('/book', methods=['POST'])
# @token_required
# def new_booking(current_user):
    
#     res, code = register_booking(current_user, request)
#     return ''




# @users.route('/register', methods=['POST'])
# def register():
#     result, code = register_user(request) 
#     print (result, code)

#     return jsonify({'message':result}), code


# @users.route('/login', methods=['POST'])
# def login():
#     result, code = login_user(request)

#     print (result, code)

#     return jsonify({'message':result}), code


@users.route('/', methods=['POST'])
@authorize.authorize
def register_user(current_user):
    print (current_user)
    res, code= usm.check_register_user(current_user)
    return res, code


@users.route('/profile' , methods=['GET'])
@authorize.authorize
def show_profile(current_user):
    res =  usm.show_user_profile(current_user)
    helpers.assert_found(res, message="User doesn't exist.")
    return helpers.respond(res, 200)



@users.route('/user/profile', methods=['PUT'])
@authorize.authorize
def complete_profile(current_user):
    res,code = usm.complete_user_profile(current_user) 
    return res

@users.route('/home', methods=['GET'])
def home_page():
    return jsonify({'message':'this seems to be home page'})
    
