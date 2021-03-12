from .models import db
from .User import User


class Spell(db.Model):
    __tablename__ = "spell"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(255))
    price = db.Column(db.Integer)
    work_type = db.Column(db.String(100))



    
