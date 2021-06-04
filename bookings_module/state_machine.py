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
    date = payload.date
    book_id = payload.bookid
    status = payload.status
    hours = payload.hours
    user = get_by_params(uId)
    user_id = None
    if user:
        user_id = user.id
        new_booking = BookingDetails(
            service_id=sId, user_id=user_id, hours=hours, date=date, status=status, cost=price, booking_id=book_id)
        db.session.add(new_booking)
        db.session.commit()
        return jsonify({'message': 'Successfully created Booking'}), 200


def getall(current_user):
    all_bookings = []
    user = User.query.filter(
        User.public_id == current_user.get('user_id')).first()
    if not user:
        return jsonify({"Error": "Could not find user. try to relogin"}), 403
    my_bookings = BookingDetails.query.filter(
        BookingDetails.user_id == user.id).all()
    for book in my_bookings:
        worker_name = book.service.user.username
        date = book.date
        status = book.status
        book_id = book.booking_id
        cost = book.cost
        work_name = book.service.name
        work_type = book.service.work_type

        all_bookings.append({"booking_id": book_id, "date": date, "worker_name": worker_name,
                            "status": status, "cost": cost, "work_type": work_type, "work_name": work_name})

    return jsonify(all_bookings), 200
