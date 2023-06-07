from flask import Blueprint, request, jsonify, session
import models
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

@listlogic.route('/get-my-workouts-names', methods=['GET'])
@jwt_required()
def get_my_workout_names():
    """
    Get the current username
    Get all workouts owned by user
    return workouts?
    """

    # get current username
    data = request.json
    username = data.get('owner')
    username = username[1:len(username)-1]

    workout_names = []
    # workouts owned by user
    workouts = session.query(models.WorkoutLists).filter_by(owner=username).all()
    for w in workouts:
        print("workouts: ")
        print(w)
        workout_names.append(w.name)

    # return list of names
    return workout_names, jsonify({"status":"got my workout names"}), 200

@listlogic.route('/get-workout-info', methods=['GET'])
@jwt_required()
def get_workout_info():
    """
    Get the current workout
    return workout.info
    """

    # get current workout

    # get workout.info
    # workout_info = workout.info

    # return info
    # return workout_info, jsonify({"status":"got my workout info"}), 200

@listlogic.route('/get-workout-likes', methods=['GET'])
@jwt_required()
def get_workout_likes():
    """
    Get the current workout
    return workout.likes
    """

    # get current workout

    # get workout.likes
    # workout_likes = workout.likes

    # return likes
    # return workout_likes, jsonify({"status":"got my workout likes"}), 200


@listlogic.route('/save-workout', methods=['POST'])
def save_workout():
    """
    get the current workout
    get the current user
    add it to savedWorkouts list
    """

    # get current workout

    # get current user
    data = request.json
    username = data.get('owner') # "name"
    username = username[1:len(username)-1] # name
    user = session.query(models.User).filter_by(username=username).first()

    # add saved workout to user
    # user.saved_workouts.append(workoutObj)
    # session.commit()
    

    return "<p>Saved Workouts</p>"


@listlogic.route('/get-saved-workout-names', methods=['GET'])
def get_saved_workout_names():
    """
    get the current user
    loop through saved workouts
        add names to list
    return list
    """

    # get current user
    data = request.json
    username = data.get('owner') # "name"
    username = username[1:len(username)-1] # name
    user = session.query(models.User).filter_by(username=username).first()

    # loop through saved workouts
    saved_workouts = []
    for w in user.saved_workouts:
        saved_workouts.append(w.name)

    # RETURNS list of saved workouts' NAMES
    return saved_workouts, jsonify({"status":"got my workout names"}), 200


# Home is where this is called
@listlogic.route('/public-workouts-names', methods=['GET'])
def public_workouts_names():
    """
    loop through users
    if they are public
        add all their workouts to a set
    return set of workouts     
    """

    all_public_workout_names = []

    # get all users
    users = session.query(models.User).all()
    for u in users:
        # if they're public
        if not u.privacy:
            user_workouts = session.query(models.WorkoutLists).filter_by(owner=u.username).all()
            # add names of all workouts into list
            for w in user_workouts:
                all_public_workout_names.append(w.name)

    # TESTING
    for work, i in all_public_workout_names:
        print("workout " + i + " :")
        print(work)
        i += 1
        print()

    # return list of public workout names
    return all_public_workout_names


@listlogic.route('/like-workout', methods=['POST'])
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

    # get current workout & if it's plus or minus
    data = request.json
    plus_or_minus = data.get("plus_or_minus")

    # get current like count
    # workout_like = workout.like

    # increment or decrement it
    if (plus_or_minus == "plus"):
        # workout.like = workout_like + 1
        # session.commit()
        return jsonify({"status":"workout liked"}), 200
    elif (plus_or_minus == "minus"):
        # workout.like = workout_like - 1
        # session.commit()
        return jsonify({"status":"workout unliked"}), 200

    return jsonify({"status":"failed to perform action"}), 406