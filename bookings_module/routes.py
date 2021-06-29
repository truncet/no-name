from flask import request, jsonify
from . import state_machine as bsm
from platform_service import authorize
from bookings_module import bookings
from platform_service import serializers
from libs import helpers


@bookings.route('/', methods=['POST'])
@authorize.authorize
def create_bookings(current_user):
    res, code = jsonify({"message": "failed"}), 400
    try:
        payload = serializers.deserialize(request.json)
        helpers.assert_true(payload.sId != None, "Invalid id")
        helpers.assert_true(payload.uId != None, "Invalid userId")
        helpers.assert_true(payload.price != None, "Invalid price")
        helpers.assert_true(payload.date != None, "Invalid ")
        helpers.assert_true(payload.bookid != None, "Invalid price")
        helpers.assert_true(payload.hours != None, "Invalid price")
        helpers.assert_true(payload.status != None, "Invalid Status")
        res, code = bsm.create(payload)
    except:
        pass
    return res, code


@bookings.route('/', methods=['GET'])
@authorize.authorize
def get_bookings(current_user):
    res, code = jsonify({"message": "failed"}), 400
    try:
        res, code = bsm.getall(current_user)
    except:
        pass
    return res, code


@bookings.route('/cancel', methods=['PUT'])
@authorize.authorize
def cancel_booking(current_user):
    res, code = jsonify({"message": "failed"}), 400
    try:
        payload = serializers.deserialize(request.json)
        helpers.assert_true(payload.booking_id != None, "Invalid book_id")
        helpers.assert_true(payload.status != None, "Invalid status")
        res, code = bsm.cancel(payload)
    except:
        pass

    return res, code


@bookings.route('/get/work', methods=['GET'])
@authorize.authorize
def get_work_bookings(current_user):
    res, code = jsonify({"message": "failed"}), 400
    res, code = bsm.who_booked_me(current_user)
    return res, code


@bookings.route('/reschedule', methods=['PUT'])
@authorize.authorize
def reschedule_booking(current_user):
    res, code = jsonify({"message": "failed"}), 400
    try:
        payload = serializers.deserialize(request.json)
        helpers.assert_true(payload.book_id != None, "Invalid book_id")
        helpers.assert_true(payload.new_date != None, "Invalid date")

        res, code = bsm.reschedule(payload)
    except:
        pass
    return res, code


@bookings.route('/accept', methods=['PUT'])
@authorize.authorize
def accept_booking(current_user):
    res, code = jsonify({"message": "failed"}), 400
    try:
        payload = serializers.deserialize(request.json)
        helpers.assert_true(payload.booking_id != None, "Invalid book_id")
        helpers.assert_true(payload.status != None, "Invalid status")

        res, code = bsm.accept(payload)
    except:
        pass
    return res, code
