from flask.json import jsonify
from flask import jsonify
from platform_service.server import db
from models import Role

def create_role(role_name):
    if not role_name:
        raise ValueError("Role Name doesn't exist.")
    role = Role(role_name=role_name)
    #db.session.add(role)
    #db.session.commit()
    return jsonify({"message": "Role Added successfully."}), 200


def get_roles():
     return Role.query.distinct(Role.role_name).all()
