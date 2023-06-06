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
    add the workout obj to myWorkouts list
    """

    """
    READ THIS:
    When I get my jwt identity, I think it's returning a 401 (missing authorized header)
    If this is solved, the workout should be created successfully,
        same goes for the other routes too
    """

    data = request.json
    workoutName = data.get('workoutName')
    workoutString = data.get('workoutString')
    tagString = data.get('tagString')
    username = data.get('owner')

    username = username[1:len(username)-1]
    user = session.query(models.User).filter_by(username=username).first()

    newlist = models.WorkoutLists(name=workoutName, info=workoutString, tags=tagString, likes=0, owner=user.username)
    session.add(newlist)
    session.commit()
    
    return jsonify({"status":"workout created"}), 200

@listlogic.route('/get-my-workouts', methods=['GET'])
@jwt_required()
def get_my_workouts():
    """
    Get the current user
    
    """

    data = request.json
    username = data.get('owner')
    username = username[1:len(username)-1]

    # the workout has to be owned by the current user
    workouts = session.query(models.User, models.WorkoutLists).filter(models.WorkoutLists.owner == models.User.username).all()
    for w in workouts:
        print("workouts: ")
        print(w)
    


    # user = session.query(models.User).filter_by(username=currUsername).first()
    # all_workouts_ids = user.my_workouts
    # all_workouts = set()
    # for workout_id in all_workouts_ids:
    #     workout_obj = session.query(models.WorkoutLists).filter_by(id=workout_id)
    #     all_workouts.add(workout_obj)

    # for workout in all_workouts:
    #     print(workout)
    #     print()

    return "<p>My Workouts</p>"

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

    # user.saved_workouts.append(workoutObj)
    

    return "<p>Saved Workouts</p>"

# Home is where this is called
@listlogic.route('/public-workouts', methods=['GET'])
def public_workouts():
    """
    loop through all users
    if they are public
        
    """

    # users = session.query(models.User).all()
    # all_workouts = set()
    # for user in users:
    #     if not user.privacy:
    #         all_workouts.add(user.my_workouts)

    # returns all workouts from public accounts
    pass


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

# @listlogic.route('/unlike-workout', methods=['GET','POST'])
# def unlike_workout():
#     """
#     get the current workout
#     decrement like variable
#     return that count, and populate it on the frontend so that the like number matches
#     """
#     return "<p>Un Likes</p>"