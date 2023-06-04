from flask import Blueprint, request, jsonify, session
import models
from sqlalchemy.orm import sessionmaker

# create Session
Session = sessionmaker(bind=models.engine)
session = Session()

listlogic = Blueprint('listlogic', __name__)

@listlogic.route('/new-workout', methods=['POST'])
def new_workout():
    data = request.json
    name = data.get("name")
    info = data.get('info')
    tags = data.get('tags')

    # HERE IS THE ERROR 
    # i'm trying to get the current user of this session
    currUser = session["username"]

    # with the curr user, i can create the new list by assigning the owner to be the cur user
    newlist = models.WorkoutLists(info=info, name=name, tags=tags, likes=0, owner=currUser)
    session.add(newlist)
    session.commit()

    return jsonify({}), 200

@listlogic.route('/my-workouts', methods=['GET'])
def my_workouts():
    return "<p>My Workouts</p>"

@listlogic.route('/saved-workouts', methods=['GET'])
def saved_workouts():
    return "<p>Saved Workouts</p>"

@listlogic.route('/public-workouts', methods=['GET'])
def public_workouts():
    return "<p>Public Workouts</p>"