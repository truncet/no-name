from flask import Flask, request
from flask_cors import CORS
from models import db, config
import json



def initialize_database(app):
	app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URL
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	db.init_app(app)


def create_app():
	app = Flask(__name__)
	CORS(app)
	initialize_database(app)

	from authorize_service.routes import users
	app.register_blueprint(users)

	return app
