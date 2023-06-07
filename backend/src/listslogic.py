from flask import Blueprint, request, jsonify, session
import models
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.mutable import MutableList
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_cors import cross_origin
from auth import session

listlogic = Blueprint('listlogic', __name__)

@listlogic.route('/create-new-workout', methods=['POST'])
@cross_origin()
# @jwt_required()
def create_new_workout():
    """
    Get the current user
    Create a workout object
    add the workout obj to myWorkouts db
    """


    data = request.json
    workoutName = data.get('workoutName')
    workoutString = data.get('workoutString')
    tagString = data.get('tagString')

    # get current user
    username = data.get('owner')
    username = username[1:len(username)-1]
    user = session.query(models.User).filter_by(username=username).first()

    # create and add workout obj
    newlist = models.WorkoutLists(name=workoutName, info=workoutString, tags=tagString, likes=0, owner=user.username)
    session.add(newlist)
    session.commit()
    
    return jsonify({"status":"workout created"}), 200

@listlogic.route('/get-my-workouts', methods=['GET'])
@jwt_required()
def get_my_workouts():
    """
    Get the current username
    Get all workouts owned by user
    return workouts?
    """

    # get current username
    data = request.json
    username = data.get('owner')
    username = username[1:len(username)-1]

    # workouts owned by user
    workouts = session.query(models.WorkoutLists).filter_by(owner=username).all()
    # for w in workouts:
    #     print("workouts: ")
    #     print(w)
    
    return workouts # FIX THIS


@listlogic.route('/get-saved-workouts', methods=['GET'])
def get_saved_workouts():
    """
    get the current user
    
    """


    data = request.json
    username = data.get('owner') # "name"
    username = username[1:len(username)-1] # name
    user = session.query(models.User).filter_by(username=username).first()



    # all_workouts_ids = user.saved_workouts
    # all_workouts = set()
    # for workout_id in all_workouts_ids:
    #     workout_obj = session.query(models.WorkoutLists).filter_by(id=workout_id)
    #     all_workouts.add(workout_obj)


    return "<p>Saved Workouts</p>"

@listlogic.route('/save-workout', methods=['GET'])
def save_workout():
    """
    get the current workout
    get the current user
    add it to savedWorkouts list
    """

    # user.saved_workouts.append(workoutObj) ?
    

    return "<p>Saved Workouts</p>"

# Home is where this is called
@listlogic.route('/public-workouts', methods=['GET'])
def public_workouts():
    """
    loop through users
    if they are public
        add all their workouts to a set
    return set of workouts     
    """

    all_public_workouts = set()
    users = session.query(models.User).all()
    for u in users:
        if not u.privacy:
            user_workouts = session.query(models.WorkoutLists).filter_by(owner=u.username).all()
            for w in user_workouts:
                all_public_workouts.append(w)

    # TESTING
    for work, i in all_public_workouts:
        print("workout " + i + " :")
        print(work)
        i += 1
        print()

    
    return all_public_workouts # FIX THIS


@listlogic.route('/like-workout', methods=['GET','POST'])
def like_or_unlike_workout():
    """
    get the current workout
    get plus or minus
    if plus
        increment like variable
    if minus
        decrement like variable
    return that count, and populate it on the frontend so that the like number matches
    """
    return "<p>Likes</p>"