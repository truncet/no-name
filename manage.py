from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from models import db
from platform_service import server

app = server.create_app() 
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('runserver', Server(host='localhost', port=5000, use_debugger=True))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()