from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key= True)
    doctorsid = db.Column(db.String(10))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstname = db.Column(db.String(150))
    reviews = db.relationship('Review')

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pet = db.Column(db.String(50))
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True),default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

