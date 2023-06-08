from flask import Blueprint, request, jsonify
import models
from auth import session
from flask_jwt_extended import jwt_required
from flask_cors import cross_origin

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

    workout_json = []
    # workouts owned by user
    workouts = session.query(models.WorkoutLists).filter_by(owner=username).all()
    for w in workouts:
        print("workouts: ")
        print(w)
        workout_json.append({'id': w.id, 'name':w.name, 'info':w.info, 'likes':w.likes})

    # return json object of workouts
    return workout_json, jsonify({"status":"got my workouts in json object"}), 200


@listlogic.route('/save-workout', methods=['POST'])
def save_workout():
    """
    get the current workout
    get the current user
    add it to savedWorkouts list
    """
    
    data = request.json

    # get current workout
    workout_id = data.get("id")
    workout = session.query(models.User).filter_by(id=workout_id).first()

    # get current user
    username = data.get('owner') # "name"
    username = username[1:len(username)-1] # name
    user = session.query(models.User).filter_by(username=username).first()

    # add saved workout to user
    user.saved_workouts.append(workout)
    session.commit()

    return jsonify({"status":"workout saved!"}), 200


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
    saved_workouts_json = []
    for w in user.saved_workouts:
        saved_workouts_json.append({'id': w.id, 'name':w.name, 'info':w.info, 'likes':w.likes})

    # return json object of workouts
    return saved_workouts_json, jsonify({"status":"got saved workouts in json object"}), 200


# Home is where this is called
@listlogic.route('/get-public-workouts', methods=['GET'])
def get_public_workouts():
    """
    loop through users
    if they are public
        add all their workouts to a set
    return set of workouts     
    """

    all_public_workout_json = []

    # get all users
    users = session.query(models.User).all()
    for u in users:
        # if they're public
        if not u.privacy:
            user_workouts = session.query(models.WorkoutLists).filter_by(owner=u.username).all()
            # add names of all workouts into list
            for w in user_workouts:
                all_public_workout_json.append({'id': w.id, 'name':w.name, 'info':w.info, 'likes':w.likes})

    # TESTING
    for work, i in all_public_workout_json:
        print("workout " + i + " :")
        print(work)
        i += 1
        print()

    # return json object of workouts
    return all_public_workout_json, jsonify({"status":"got public workouts in json object"}), 200


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
    currWokroutid = data.get("id")
    plus_or_minus = data.get("plus_or_minus")

    workout = session.query(models.WorkoutLists).filter_by(id=currWokroutid).first()
    # get current like count
    workout_like = workout.like

    # increment or decrement it
    if (plus_or_minus == "plus"):
        workout.like = workout_like + 1
        session.commit()
        return jsonify({"status":"workout liked"}), 200
    elif (plus_or_minus == "minus"):
        workout.like = workout_like - 1
        session.commit()
        return jsonify({"status":"workout unliked"}), 200

    return jsonify({"status":"failed to perform action"}), 406

def create_default_workout(workoutName, workoutString, tagString):
    # create and add workout obj
    newlist = models.WorkoutLists(name="Default Back", info="Seated Row:  Reps: 10 Sets: 4\nDeadlift:  Reps: 8 Sets: 3-4\nDumbbell Row:  Reps: 10 Sets: 3-4", tags="Upper-body\nBack\nBeginner", likes=0, owner="admin")
    session.add(newlist)
    session.commit()

    newlist = models.WorkoutLists(name="Default Chest", info="Bench Press:  Reps: 8 Sets: 4\nPush-ups:  Reps: 10 Sets: 3-4\nSvend Press:  Reps: 10 Sets: 3-4", tags="Upper-body\nChest\nBeginner", likes=0, owner="admin")
    session.add(newlist)
    session.commit()

    newlist = models.WorkoutLists(name="Default Legs", info="Calf Raises:  Reps: 12 Sets: 4\nSquats:  Reps: 8 Sets: 3-4\nLeg Press:  Reps: 12 Sets: 4\nDeadlift:  Reps: 8 Sets: 3", tags="Lower-body\nLegs\nBeginner", likes=0, owner="admin")
    session.add(newlist)
    session.commit()

    newlist = models.WorkoutLists(name="Default Arms", info="Concentration Curls:  Reps: 10 Sets: 4\nOverhead Tricep Extensions:  Reps: 10 Sets: 4\nHammer Curls:  Reps: 10 Sets: 3\nDumbbell floor press:  Reps: 10 Sets: 3", tags="Upper-body\nArms\nBeginner", likes=0, owner="admin")
    session.add(newlist)
    session.commit()

    newlist = models.WorkoutLists(name="Default Shoulders", info="Lateral Raises:  Reps: 10 Sets: 3-4\nDumbbell shrugs:  Reps: 10 Sets: 3\nShoulder Press:  Reps: 10 Sets: 3-4", tags="Upper-body\nShoulders\nBeginner", likes=0, owner="admin")
    session.add(newlist)
    session.commit()