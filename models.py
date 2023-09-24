from app import db
from datetime import datetime

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer)
    humidity = db.Column(db.Integer)
    ec = db.Column(db.Integer)
    ph= db.Column(db.Integer)
    turbidity= db.Column(db.Integer)
    tds = db.Column(db.Integer)
    temperature = db.Column(db.Integer)
    time = db.Column(db.DateTime, default = datetime.now())