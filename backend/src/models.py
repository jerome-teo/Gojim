# database for users, workout lists, & exercises

from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Boolean, ARRAY
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.mutable import MutableList
from flask_login import UserMixin

# manage tables
base = declarative_base()
# connect with data base
engine = create_engine('sqlite:///database.db', echo=True)

class WorkoutLists(base):
    __tablename__ = "workout_lists"

    id = Column("workout_list_id", Integer, primary_key=True)
    name = Column("name", String)
    info = Column("info", String)
    tags = Column("tags", String)
    likes = Column("ikes", Integer)
    # owner = Column(Integer, ForeignKey("users.username"))

    def __init__(self, name, info, tags, likes):
        self.name = name
        self.info = info
        self.tags = tags
        self.likes = likes
        # self.owner = owner
    
    # train upper: lats reps: 8 sets: 3 (upperbody) (10 likes) by timsmith 
    def __repr__(self):
        return f"{self.name}: ({self.info}) ({self.tags}) ({self.likes} likes)"


class User(UserMixin, base):
    __tablename__ = "users"

    # we need to be able to uniquely identify objects
    id = Column("user_id", Integer, primary_key=True)
    # you need to pick a max length of characters when you create a String
    # unique=True makes it so that it's impossible for two users to have the same email
    email = Column("email", String, unique=True)
    username = Column("username", String(50), unique=True)
    password = Column("password", String(100))
    # error is that WorkoutLists need to be initialized here
    my_workouts = Column("my_workouts", MutableList.as_mutable(ARRAY(Integer)))
    saved_workouts = Column("saved_workouts", MutableList.as_mutable(ARRAY(Integer)))
    # my_workouts = Column("my_workouts", ARRAY(Integer))
    # saved_workouts = Column("saved_workouts", ARRAY(Integer))
    privacy = Column("privacy", Boolean)

    def __init__(self, email, username, password, privacy):
        self.email = email
        self.username = username
        self.password = password
        self.privacy = privacy

    # (timsmith) tim@gmail.com
    def __repr__(self):
        return f"({self.username}) {self.email}"

base.metadata.create_all(bind=engine)