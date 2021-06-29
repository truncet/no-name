from flask.json import jsonify
from flask import jsonify
from platform_service.server import db
from models import Role, User


def create_role(role_name):
    if not role_name:
        raise ValueError("Role Name doesn't exist.")
    role = Role(role_name=role_name)
    # db.session.add(role)
    # db.session.commit()
    return jsonify({"message": "Role Added successfully."}), 200


def get_roles():
    return Role.query.distinct(Role.role_name).all()


def get_my_role(current_user):
    user_id = current_user.get('user_id').strip()
    print(user_id)

    user = User.query.filter(User.public_id == user_id).first()
    if user:
        return jsonify({"role": user.role_id}), 200

    return {}, 400
