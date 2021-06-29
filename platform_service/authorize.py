import os
from flask import jsonify, request
from functools import wraps
import google.auth.transport.requests
import google.oauth2.id_token


# token creation so that only users registered can utilize some functions
def authorize(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        HTTP_REQUEST = google.auth.transport.requests.Request()

        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split().pop()

        if not token:
            return jsonify({'message': 'Token is not present!'}), 401

        try:
            user_creds = google.oauth2.id_token.verify_firebase_token(
                token, HTTP_REQUEST, audience=os.environ.get('GOOGLE_CLOUD_PROJECT'))
            current_user = user_creds
        except:
            return jsonify({'message': 'Token is invalid!'}), 403

        return f(current_user, *args, **kwargs)

    return decorated
