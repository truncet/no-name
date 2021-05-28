from flask import jsonify
from platform_service.server import db
from models import Service
from models import User
from platform_service import serializers

def create():
    return {"message": "Successfully created service"}

def get_all_profiles(current_user):
    services = Service.query.all()

    ### this is to send user data to the frontend 
    for t in services:
       t.user.public_id 
    return services
