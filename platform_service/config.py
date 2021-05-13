import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'halka-ramailo'
    SQLALCHEMY_DATABASE_URI = 'postgres://%s:%s@%s:%s/%s'%(os.environ.get('DB_USER'), os.environ.get('DB_PASSWORD'), os.environ.get('POSTGRES_SERVICE_HOST'), os.environ.get('POSTGRES_SERVICE_PORT'), os.environ.get('DB_NAME'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SQLALCHEMY_ECHO = True
