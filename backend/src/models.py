# database for users, workout lists
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Boolean, Table
# from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.mutable import MutableList
# from flask_login import UserMixin
# from flask_sqlalchemy import SQLAlchemy
# import psycopg2

# manage tables
base = declarative_base()
# connect with data base
engine = create_engine('sqlite:///database.db', echo=True)


user_saved_workouts = Table("user_saved_workouts", base.metadata,
                      Column("user_id", Integer, ForeignKey("users.user_id")),
                      Column("workout_id", Integer, ForeignKey("workout_lists.workout_list_id"))
                      )

class WorkoutLists(base):
    __tablename__ = "workout_lists"

    id = Column("workout_list_id", Integer, primary_key=True)
    name = Column("name", String)
    info = Column("info", String)
    tags = Column("tags", String)
    likes = Column("likes", Integer)
    owner = Column("owner", String)
    # owner = Column(Integer, ForeignKey("users.username"))

    def __init__(self, name, info, tags, likes, owner):
        self.name = name
        self.info = info
        self.tags = tags
        self.likes = likes
        self.owner = owner
        # self.owner = owner
    
    # train upper: lats reps: 8 sets: 3 (upperbody) (10 likes) by timsmith 
    def __repr__(self):
        return f"{self.name}: ({self.info}) ({self.tags}) ({self.likes} likes)"


class User(base):
    __tablename__ = "users"

    # we need to be able to uniquely identify objects
    id = Column("user_id", Integer, primary_key=True)
    # you need to pick a max length of characters when you create a String
    # unique=True makes it so that it's impossible for two users to have the same email
    email = Column("email", String, unique=True)
    username = Column("username", String(50), unique=True)
    password = Column("password", String(100))
    privacy = Column("privacy", Boolean)
    saved_workouts = relationship("WorkoutLists", secondary="user_saved_workouts")

    def __init__(self, email, username, password, privacy):
        self.email = email
        self.username = username
        self.password = password
        self.privacy = privacy

    # (timsmith) tim@gmail.com
    def __repr__(self):
        return f"({self.username}) {self.email}"
    
base.metadata.create_all(bind=engine)