import os
import datetime
from functools import wraps
from flask import jsonify, request, redirect, url_for
import google.auth.transport.requests
import google.oauth2.id_token
from libs import utils
from models import db,User


## token creation so that only users registered can utilize some functions
def token_required(f):
    @wraps(f)

    def decorated(*args, **kwargs):
        token = None
        HTTP_REQUEST = google.auth.transport.requests.Request()

        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split().pop()
        
        if not token:
            return jsonify({'message': 'Token is not present!'}), 401

        try:
            user_creds = google.oauth2.id_token.verify_firebase_token(\
                token, HTTP_REQUEST, audience=os.environ.get('GOOGLE_CLOUD_PROJECT'))
            current_user = user_creds
        except:
            return jsonify({'message':'Token is invalid!'}), 403
        
        return f(current_user, *args, **kwargs)

    return decorated



def show_user_profile(current_user):
    return 1

def complete_user_profile(current_user):
    print ("I am here")
    return 1

def check_register_user(current_user):
    user_id = current_user.get('user_id')

    user = utils.check_if_user("public_id", user_id)
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

