from platform_service.server import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False )
    username = db.Column(db.String(100))
    email = db.Column(db.String(255), unique=True, nullable=False)
    age = db.Column(db.Integer)
    profession = db.Column(db.String(100))
    location = db.Column(db.String(500))
    phone = db.Column(db.String(50), unique=True )
    profile_completed = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return "%s"%(self.__dict__)
    
    def __getitem__(self, item):
        return getattr(self, item)
    
    def seriazlize(self):
        return self.__dict__
        

class Spell(db.Model):
    __tablename__ = "spells"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(255))
    price = db.Column(db.Integer)
    work_type = db.Column(db.String(100))

    def seriazlize(self):
        return self.__dict__

    def __repr__(self):
        return "%s"%(self.__dict__)


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(100))

    def seriazlize(self):
        return self.__dict__

    def __repr__(self):
        return "%s"%(self.__dict__)


class BookingDetails(db.Model):
    __tablename__ = "booking_details"
    id = db.Column(db.Integer, primary_key=True)
    spell_id = db.Column(db.Integer, db.ForeignKey('spells.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False )
    time = db.Column(db.DateTime)
    cost = db.Column(db.Integer)
    status = db.Column(db.String)


    def seriazlize(self):
        return self.__dict__

    def __repr__(self):
        return "%s"%(self.__dict__)


