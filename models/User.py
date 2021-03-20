from .models import db
from .Role import Role

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False )
    username = db.Column(db.String(100))
    email = db.Column(db.String(255), unique=True, nullable=False)
    age = db.Column(db.Integer)
    profession = db.Column(db.String(100))
    location = db.Column(db.String(500))
    phone = db.Column(db.String(50), unique=True )

    def __repr__(self):
        return self.name

