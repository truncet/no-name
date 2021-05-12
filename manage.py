from flask_migrate import Migrate, MigrateCommand

from models import db
from platform_service import server

app = server.create_app() 
migrate = Migrate(app, db)