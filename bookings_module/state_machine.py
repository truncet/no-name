from flask import jsonify
from platform_service.server import db
from models import BookingDetails

def create():
    return {"message": "Successfully created Booking"}