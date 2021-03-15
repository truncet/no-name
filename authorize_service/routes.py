from  flask import render_template, Blueprint, request, jsonify
from .state_machines import token_required, register_user, login_user, register_booking
import json


users = Blueprint('users', __name__)



@users.route('/user', methods=['GET'])
@token_required
def get_current_user_info(current_user):
    return jsonify({'message':current_user.username + " is logged in"}), 200
    



@users.route('/book', methods=['GET'])
@token_required
def get_current_booking(current_user):
    return ''


@users.route('/book', methods=['POST'])
@token_required
def new_booking(current_user):
    
    res, code = register_booking(current_user, request)
    return ''




@users.route('/register', methods=['POST'])
def register():
    result, code = register_user(request) 
    print (result, code)

    return jsonify({'message':result}), code


@users.route('/login', methods=['POST'])
def login():
    result, code = login_user(request)

    print (result, code)

    return jsonify({'message':result}), code


