from flask import jsonify, request, redirect, url_for
from platform_service.server import db
from libs import utils
from models import User

def show_user_profile(current_user):
    return jsonify({"message": "Shown user profile"}), 200

def complete_user_profile(current_user):
    user_id = current_user.get('user_id')
    userExist = utils.check_if_user("public_id", user_id)

    if not userExist:
        error_msg = "This user is not registered. Signup again"
        return jsonify({"message":error_msg}), 403
    else:
        try:
            user_name = request.json.get('userName')
            age = request.json.get('age')
            profession = request.json.get('profession')
            location = request.json.get('location')
            number = request.json.get('number')

            user = User.query.filter_by(public_id=user_id).first()
            user.username = user_name
            user.age = age
            user.profession = profession
            user.location = location
            user.phone = number

            db.session.commit()
            return jsonify({"message":"Database updated"}), 200
        except:
            return jsonify({"message":"Could not update the db"}), 500

def check_register_user(current_user):
    user_id = current_user.get('user_id')

    user = utils.check_if_user("public_id", user_id)
    if not user:
        public_id = current_user.get('user_id')
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

