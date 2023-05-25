# have a database model for users and notes

# import from this current website package, import db
from . import db
from flask_login import UserMixin # custom class we can inhert that gives user obj things specific for flask login
from sqlalchemy.sql import func

# a database model is just a layout/blueprint for an obj that's gonna be stored in your database
# so all notes need to conform to this model --> you know ur info is gonna be consistent
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # we want multiple notes for one user, so we want to establish a relationship between notes & user
    # foreign key: column in database that always references a column in another database
    # reference id of the user when a note is created
    # one to many relationship: one user has many nodes (which are notes), ie one obj has many children
    userID = db.Column(db.Integer, db.ForeignKey('user.id'))

#class Reminder(db.Model):

# define name of object and inherit from db.Model
class User(db.Model, UserMixin):
    # we need to be able to uniquely identify objects
    id = db.Column(db.Integer, primary_key=True)
    # you need to pick a max length of characters when you create a String
    # unique=True makes it so that it's impossible for two users to have the same email
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    notes = db.relationship('Note') # when a note is created, add it to this list
    # see how Note is capitalized above
