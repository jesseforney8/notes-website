from __init__ import db
from flask_login import UserMixin
from sqlalchemy import func

#creates user model for DB

class User(db.Model, UserMixin):

    __tablename__ = 'users'
    #unique id to reprisent object and crearting columns in db. Auto sets ID for you
    id = db.Column(db.Integer, primary_key=True)
    # creates email column and max length is 150, must be unique
    email = db.Column(db.String(150), unique=True)

    password = db.Column(db.String(150))

    firstname = db.Column(db.String(150))

    #adds note id
    notes = db.relationship("Note")

class Note(db.Model):
    __tablename__ = "notes"
    
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    # date = db.Column(db.DateTime(timezone=True), default=func.now)
    
    #assosiate notes with user, foriegn key, one to many relationship
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
