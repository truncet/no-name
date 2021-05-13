from platform_service import server
from models import User

app = server.create_app() 

@app.shell_context_processor
def make_shell_context():
    return {'db': server.db, 'User': User}