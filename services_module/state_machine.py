from flask import jsonify
from platform_service.server import db
from models import Service

def create():
    return {"message": "Successfully created service"}