from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    TP2 = db.Column(db.Float)
    TP3 = db.Column(db.Float)
    H1 = db.Column(db.Float)
    DV_pressure = db.Column(db.Float)
    Reservoirs = db.Column(db.Float)
    Oil_temperature = db.Column(db.Float)
    Flowmeter = db.Column(db.Float)
    Motor_current = db.Column(db.Float)
    COMP = db.Column(db.Boolean)
    DV_eletric = db.Column(db.Boolean)
    Towers = db.Column(db.Boolean)
    MPG = db.Column(db.Boolean)
    LPS = db.Column(db.Boolean)
    Oil_level = db.Column(db.Boolean)
    Caudal_impulses = db.Column(db.Boolean)
    gpsSpeed = db.Column(db.Integer)
    
    pred_label = db.Column(db.Integer)
    pred_class = db.Column(db.String(20))
    confidence = db.Column(db.Float)
    
    actual_label = db.Column(db.Integer, default=0) # Zero for normal

    def __repr__(self):
        return f'<SensorData id={self.id}>'


class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
