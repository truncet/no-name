from flask import json, jsonify
from platform_service.server import db
from models import BookingDetails, User, Service
from libs import utils


def get_by_params(user_id):
    user = utils.find_by_parameters(public_id=user_id)
    if user:
        return user[0]
    return user


def create(payload):
    uId = payload.uId
    sId = payload.sId
    price = payload.price
    time = payload.datetime
    book_id = payload.bookid
    user = get_by_params(uId)
    user_id = None
    if user:
        user_id = user.id
        new_booking = BookingDetails(
            service_id=sId, user_id=user_id, time=time, cost=price, booking_id=book_id)
        db.session.add(new_booking)
        db.session.commit()
        return jsonify({'message': 'Successfully created Booking'}), 200


def getall():
    return BookingDetails.query.all(), 200
    # return jsonify({'message': 'Successfully sent Booking'}), 200
