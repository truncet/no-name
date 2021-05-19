import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config


db = SQLAlchemy(session_options={'autocommit': False, 'autoflush': True})
migrate = Migrate()


def create_app(config_class=Config):
	app = Flask(__name__)
	CORS(app)
	app.config.from_object(Config)
	db.init_app(app)
	migrate.init_app(app, db)

	from users_module import users as users_blueprint
	app.register_blueprint(users_blueprint, url_prefix='/user')

	from roles_module import roles as roles_blueprint
	app.register_blueprint(roles_blueprint, url_prefix='/role')

	from services_module import services as services_blueprint
	app.register_blueprint(services_blueprint, url_prefix='/service')

	from bookings_module import bookings as bookings_blueprint
	app.register_blueprint(bookings_blueprint, url_prefix='/booking')

	return app
