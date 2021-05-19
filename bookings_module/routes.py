from flask import request
from . import state_machine as bsm
from platform_service import authorize
from bookings_module import bookings

@bookings.route('/', methods=['POST'])
@authorize.authorize
def create_bookings(current_user):
    return bsm.create()