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


def cancel(payload):
    booking_id = payload.booking_id
    status = payload.status
    booking = BookingDetails.query.filter(
        BookingDetails.booking_id == booking_id).first()
    if not booking:
        return jsonify({"message": "could not find the booking "}), 400

    booking.status = status

    db.session.commit()

    return jsonify({"message": "Completed cancellation"}), 200


def who_booked_me(current_user):
    final_res = []
    user_id = current_user.get('user_id')
    user = User.query.filter(User.public_id == user_id).first()
    if user:
        id = user.id
        my_bookings = BookingDetails.query.join(
            Service).filter(Service.user_id == id).all()
        for i in range(len(my_bookings)):
            booked_user_id = my_bookings[i].user_id
            booked_user = User.query.filter(User.id == booked_user_id).first()
            if booked_user:
                booking_id = my_bookings[i].booking_id
                cost = my_bookings[i].cost
                status = my_bookings[i].status
                date = my_bookings[i].date
                username = booked_user.username
                user_phone = booked_user.phone
                user_location = booked_user.location

                final_res.append({"booking_id": booking_id, "cost": cost, "status": status, "date": date,
                                  "username": username, "user_phone": user_phone, "user_location": user_location})
        return jsonify(final_res), 200


def reschedule(payload):
    booking_id = payload.book_id
    new_date = payload.new_date

    booking = BookingDetails.query.filter(
        BookingDetails.booking_id == booking_id).first()
    if not booking:
        return jsonify({"message": "Update Failed"})

    print(booking_id)
    booking.date = new_date
    print(booking.date)
    db.session.commit()
    return jsonify({"message": "Update Successful"}), 200


def accept(payload):
    booking_id = payload.booking_id
    status = payload.status
    booking = BookingDetails.query.filter(
        BookingDetails.booking_id == booking_id).first()
    if not booking:
        return jsonify({"message": "could not find the booking "}), 400

    booking.status = status

    db.session.commit()

    return jsonify({"message": "Booking Accepted"}), 200
