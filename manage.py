from platform_service import server
from models import User,Spell,Role,BookingDetails

app = server.create_app() 

@app.shell_context_processor
def make_shell_context():
    return {'db': server.db, 'User': User,'Spell':Spell, 'Role':Role, 'BookingDetails':BookingDetails}
