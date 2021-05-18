from flask import jsonify, request, redirect, url_for
from platform_service.server import db
from libs import utils, helpers
from models import User


def get(id):
    user = utils.find_by_parameters(id=id)
    return user[0] if len(user) > 0 else None

def get_by_public_id(user_id):
    user = utils.find_by_parameters(public_id=user_id)
    return user

def show_user_profile(current_user):
    user_id = current_user.get('user_id')
    user = get_by_public_id(user_id)
    return user

def complete_user_profile(current_user, user):
    user_id = current_user.get('user_id')
    old_user = get_by_public_id(user_id)[0]
    helpers.assert_found(old_user, "User doesn't exist.")
    old_user_id = getattr(old_user, 'id')
    update_with_coalesce = ['age', 'profession']
    update_without_coalesce = ['userName', 'location', 'phone']

    for key in update_with_coalesce:
        value = getattr(user, key)
        print(f"Value for key {key} in user: {value}")
        if value:
            setattr(old_user, key, value)
    
    for key in update_without_coalesce:
        value = getattr(user, key)
        setattr(old_user, key, value)

    setattr(old_user, 'profile_completed',old_user.is_complete())

    db.session.commit()

    return get(old_user_id), 200


def check_register_user(current_user):
    public_id = current_user.get('user_id')

    user = get_by_public_id(public_id)

    if not user:
        email = current_user.get('firebase').get('identities').get('email')[0]
        print (email)
        role = request.json.get('role')
        if role=="worker":
            role_id = 1
        elif role=="searcher":
            role_id = 2

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

