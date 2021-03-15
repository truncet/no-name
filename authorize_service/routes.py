from  flask import render_template, Blueprint, request, jsonify
from .state_machines import token_required, register_user, login_user
import json


users = Blueprint('users', __name__)



@users.route('/user', methods=['GET'])
@token_required
def get_users(current_user):
    return ''


@users.route('/user', methods=['POST'])
@token_required
def create_user():
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


