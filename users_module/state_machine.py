from flask import jsonify, request, redirect, url_for
from platform_service.server import db
from libs import utils, helpers
from models import User


def get_by_public_id(user_id):
    user = utils.find_by_parameters(public_id=user_id)
    return user

def show_user_profile(current_user):
    user_id = current_user.get('user_id')
    user = get_by_public_id(user_id)
    return user

def complete_user_profile(current_user):
    print ("I am here")
    return 1

def check_register_user(current_user):
    user_id = current_user.get('user_id')

    user = get_by_public_id(user_id)
    if not user:
        public_id = current_user.get('user_id')
        email = current_user.get('firebase').get('identities').get('email')
        role_id = request.form.get('role_id')

        new_user = User(public_id=public_id, email=email, role_id=role_id)
        db.session.add(new_user)
        db.session.commit()

        print ("new_user_added")
        return jsonify({'message':'register complete'}), 302
    else:
        display_name = user.username
        if not display_name:
            print ("this")
            return jsonify({'message':'complete profile now'}), 302

    return jsonify({'message':' profile complete'}), 200

