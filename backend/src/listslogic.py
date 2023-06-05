from flask import Blueprint, request, jsonify, session
import models
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.mutable import MutableList
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_login import current_user

# create Session
Session = sessionmaker(bind=models.engine)
session = Session()

listlogic = Blueprint('listlogic', __name__)

@listlogic.route('/create-new-workout', methods=['GET','POST'])
@jwt_required()
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
    currUsername = get_jwt_identity()
    print("current username:")
    print(currUsername)
    print()
    data = request.json
    # data = request.form
    name = data.get("name")
    info = data.get('info')
    tags = data.get('tags')
    request.u
    print("data: ")
    print(data)
    print()

    newlist = models.WorkoutLists(name=name, info=info, tags=tags, likes=0)
    print(newlist)
    print()
    session.add(newlist)
    user = session.query(models.User).filter_by(username=currUsername).first()
    print(user)
    print()
    user.my_workouts.append(newlist)
    session.commit()
    
    return jsonify({}), 200

@listlogic.route('/get-my-workouts', methods=['GET'])
@jwt_required()
def get_my_workouts():
    """
    Get the current user
    return myWorkouts list
    """

    currUsername = get_jwt_identity()
    print("curr username:")
    print(currUsername)
    print()
    print()
    user = session.query(models.User).filter_by(username=currUsername).first()
    all_workouts_ids = user.my_workouts
    all_workouts = set()
    for workout_id in all_workouts_ids:
        workout_obj = session.query(models.WorkoutLists).filter_by(id=workout_id)
        all_workouts.add(workout_obj)

    for workout in all_workouts:
        print(workout)
        print()

    return "<p>My Workouts</p>"

@listlogic.route('/get-saved-workouts', methods=['GET'])
def get_saved_workouts():
    """
    get the current user
    return savedWorkouts list
    """

    currUsername = get_jwt_identity
    user = session.query(models.User).filter_by(username=currUsername).first()
    all_workouts_ids = user.saved_workouts
    all_workouts = set()
    for workout_id in all_workouts_ids:
        workout_obj = session.query(models.WorkoutLists).filter_by(id=workout_id)
        all_workouts.add(workout_obj)


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
        return their myWorkouts list
    """

    users = session.query(models.User).all()
    all_workouts = set()
    for user in users:
        if not user.privacy:
            all_workouts.add(user.my_workouts)

    # returns all workouts from public accounts
    return all_workouts


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