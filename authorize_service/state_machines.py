import os
import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from flask import jsonify, request
from models import User, Spell,BookingDetails, db
from libs.utils import generate_uuid
from platform_service import helpers


## token creation so that only users registered can utilize some functions
def token_required(f):
    @wraps(f)

    def decorated(*args, **kwargs):
        token = None
        secret_key = os.environ['SECRET_KEY']

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        
        if not token:
            return jsonify({'message': 'Token is not present!'}), 401

        try:
            data = jwt.decode(token, secret_key, algorithms='HS256')
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message':'Token is invalid!'}), 403
        
        return f(current_user, *args, **kwargs)

    return decorated



def empty_if_none(t):
    if t is None:
        return ""
    return t

def check_for_user(param, value):

    return User.query.filter(getattr(User, param)==value).first()

def check_for_spell(param, value):
    return Spell.query.filter(getattr(Spell, param)==value).first()



def register_user(request):
    request_data = request.form

    username = request_data['username']
    email = request_data['email']
    password = request_data['password']
    age = request_data['age']
    profession = request_data['profession']
    location = request_data['location']
    phone = request_data['phone']
    role_id = request_data['role_id']
    public_id = generate_uuid()


    user = check_for_user('User','username',username) 

    try:
        helpers.assert_null(len(username.strip()) > 0, message="Null Check")
        helpers.assert_null(len(email.strip()) > 0, message="Null Check")
        helpers.assert_null(len(phone.strip()) > 0, message="Null Check")
        helpers.assert_null(len(password.strip()) > 0, message="Null Check")
        helpers.assert_already_exist(not user, message="Exist Check")
    
    except(helpers.InvalidUsage):
        return "Null check failed", 400

    except (helpers.AlreadyExists):
        return "Already Exist", 400


    hashed_password = generate_password_hash(password, method='sha256')

    new_user = User(public_id=public_id,role_id=role_id, username=username, email=email, password=hashed_password,\
        age=age, profession=profession,location=location, phone=phone)

    db.session.add(new_user)

    db.session.commit()



    return "User added to DB", 200



def login_user(request):
    request_data = request.form

    username = empty_if_none(request_data.get('username'))
    password = empty_if_none(request_data.get('password'))
    

    try:
        helpers.assert_null(len(username) > 0, message='Null Check')
        helpers.assert_null(len(password) > 0, message='Null Check')

    except(helpers.InvalidUsage):
        print ("Dont put empty stuff Man!!")
        return "Null", 400

    user = check_for_user('username', username)

    if not user:
        return "Could not find User", 401
    
    if check_password_hash(user.password, password):
        token = jwt.encode({'public_id':user.public_id, 'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, os.environ['SECRET_KEY'])
        return token, 200 

    return "Could not verify the user", 403



def register_booking(current_user, request):
    print (current_user.username)

    bookee_public_id = request.form.get('public_id') 

    bookee = check_for_user('public_id', bookee_public_id)

    bookee_spell = ""
    if bookee:
        print ('bookee')
        bookee_spell = check_for_spell('user_id', bookee.id)
        if bookee_spell:

            spell_id = bookee_spell.id
            user_id = current_user.id
            time = datetime.datetime.utcnow() + datetime.timedelta(days=1)
            cost = bookee_spell.price
            status = "booked"

            book = BookingDetails(spell_id=spell_id, user_id=user_id, time=time,cost=cost,status=status)
            db.session.add(book)
            db.session.commit()

    return 0,0
    