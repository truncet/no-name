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
    payload = serializers.deserialize(request.json)
    helpers.assert_true(payload.sId != None, "Invalid id")
    helpers.assert_true(payload.uId != None, "Invalid userId")
    helpers.assert_true(payload.price != None, "Invalid price")
    helpers.assert_true(payload.date != None, "Invalid ")
    helpers.assert_true(payload.bookid != None, "Invalid price")
    helpers.assert_true(payload.hours != None, "Invalid price")
    helpers.assert_true(payload.status != None, "Invalid Status")
    res, code = bsm.create(payload)
    return res, code


@bookings.route('/', methods=['GET'])
@authorize.authorize
def get_bookings(current_user):
    res, code = jsonify({"message": "failed"}), 400
    res, code = bsm.getall(current_user)
    return res, code
