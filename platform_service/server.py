from flask import Flask, request
from flask_cors import CORS
from models import db, config
import json

app = Flask(__name__)
CORS(app)


@app.route('/ready', methods=['GET'])
def index():
	return json.dumps({'message': 'Voilaa! Service is up and running...'})

def initialize_database(app):
	app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URL
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	db.init_app(app)

initialize_database(app)
