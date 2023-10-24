from app import app, db
from app.models import Admin, SensorData

with app.app_context():
    db.create_all()
    user = Admin(username='admin')
    user.set_password('admin')
    db.session.add(user)
    db.session.commit()
