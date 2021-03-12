from .models import db
from .User import User
from .Spell import Spell


class BookingDetails(db.Model):
    __tablename__ = "booking_details"
    id = db.Column(db.Integer, primary_key=True)
    spell_id = db.Column(db.Integer, db.ForeignKey('spell.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False )
    time = db.Column(db.DateTime)
    cost = db.Column(db.Integer)
    status = db.Column(db.String)

    
    