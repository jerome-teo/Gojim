# database for users, workout lists, & exercises

from sqlalchemy import create_engine, ForeignKey, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# manage tables
base = declarative_base()
# connect with data base
engine = create_engine('sqlite:///database.db', echo=True)

class User(base):
    __tablename__ = "users"

    # we need to be able to uniquely identify objects
    id = Column("user_id", Integer, primary_key=True)
    # you need to pick a max length of characters when you create a String
    # unique=True makes it so that it's impossible for two users to have the same email
    email = Column("email", String, unique=True)
    username = Column("username", String(50), unique=True)
    name = Column("name", String(150))
    password = Column("password", String(100))

    # create a list of workout_lists
    #my_workout_lists = Co

    def __init__(self, email, username, name, password):
        self.email = email
        self.username = username
        self.name = name
        self.password = password

    # tim smith (timsmith) tim@gmail.com
    def __repr__(self):
        return f"{self.name} ({self.username}) {self.email}"

#class WorkoutLists():


base.metadata.create_all(bind=engine)