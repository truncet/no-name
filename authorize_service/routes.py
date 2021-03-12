from  flask import render_template, Blueprint
import json


users = Blueprint('users', __name__)


@users.route('/users', methods=['GET'])
def user_show():
    return json.dumps({'message': 'users! Service is up '})