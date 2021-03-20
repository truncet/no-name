from  flask import render_template, Blueprint, request, jsonify, redirect, url_for
#from .state_machines import token_required, register_user, login_user, register_booking
from .state_machines import token_required, check_register_user, show_user_profile, complete_user_profile
import json
from flask_cors import CORS, cross_origin


users = Blueprint('users', __name__)


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


@users.route('/user', methods=['POST'])
@token_required
def register_user(current_user):
    print (current_user)
    res, code= check_register_user(current_user)
    return res


@users.route('/user/profiles' , methods=['GET'])
@token_required
def show_profile(current_user):
    res, code =  show_user_profile(current_user)
    return res



@users.route('/user/profile', methods=['PUT'])
@token_required
def complete_profile(current_user):
    res,code = complete_user_profile(current_user) 
    return res

@users.route('/home', methods=['GET'])
def home_page():
    return jsonify({'message':'this seems to be home page'})
    
