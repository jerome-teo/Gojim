from flask import Blueprint, request, jsonify
import models
from auth import session
from flask_cors import cross_origin


listlogic = Blueprint('listlogic', __name__)


# DONE
@listlogic.route('/create-new-workout', methods=['POST'])
@cross_origin()
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



# DONE
@listlogic.route('/get-num-workouts', methods=['POST'])
@cross_origin()
def get_num_workouts():

    # get current username
    data = request.json
    username = data.get('owner')
    username = username[1:len(username)-1]

    print("username")
    print(username)
    print()
    # workouts owned by user
    workouts = session.query(models.WorkoutLists).filter_by(owner=username).all()
    i = 0
    for w in workouts:
        i = i + 1
        print(w)
    print("num workouts:")
    print(i)
    print()

    jsonObj = [{"num_workouts":i}]

    return jsonify(jsonObj), 200


# DONE
@listlogic.route('/get-my-workouts', methods=['POST'])
@cross_origin()
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
        workout_json.append({'id': w.id, 'name':w.name, 'workoutString':w.info, 'likes':w.likes})

    # return json object of workouts
    return jsonify(workout_json), 200


# DONE
@listlogic.route('/save-workout', methods=['POST'])
@cross_origin()
def save_workout():
    """
    get the current workout
    get the current user
    add it to savedWorkouts list
    """
    
    data = request.json

    # get current workout
    workout_id = data.get("workoutId")
    print("workoutid:")
    print(workout_id)
    print()
    workout = session.query(models.WorkoutLists).filter_by(id=workout_id).first()

    print("workout")
    print(workout)
    print()

    # get current user
    username = data.get('owner') # "name"
    print("username")
    print(username)
    print()
    username = username[1:len(username)-1] # name
    user = session.query(models.User).filter_by(username=username).first()

    print(user)

    # add saved workout to user
    user.saved_workouts.append(workout)
    session.commit()

    for w in user.saved_workouts:
        print("saved workouts: ")
        print(w)
        print()

    return jsonify({"status":"workout saved!"}), 200


# DONE
@listlogic.route('/unsave-workout', methods=['POST'])
@cross_origin()
def unsave_workout():
    """
    get the current user
    get the current workout id
    remove from saved workouts list
    """

    data = request.json

    # get current workout
    workout_id = data.get("workoutId")
    print("workout id")
    print(workout_id)
    print()
    workout = session.query(models.WorkoutLists).filter_by(id=workout_id).first()

    # get current user
    username = data.get('owner') # "name"
    username = username[1:len(username)-1] # name
    user = session.query(models.User).filter_by(username=username).first()

    # remove saved workout
    user.saved_workouts.remove(workout)
    session.commit()

    return jsonify({"status":"workout unsaved!"}), 200


# DONE
@listlogic.route('/get-saved-workouts', methods=['POST'])
@cross_origin()
def get_saved_workoutS():
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
        saved_workouts_json.append({'id': w.id, 'name':w.name, 'workoutString':w.info, 'likes':w.likes})

    # return json object of workouts
    return jsonify(saved_workouts_json), 200


# DONE
@listlogic.route('/get-public-workouts', methods=['GET'])
@cross_origin()
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
                all_public_workout_json.append({'id': w.id, 'name':w.name, 'workoutString':w.info, 'likes':w.likes})

    # TESTING
    for work in all_public_workout_json:
        print("workout:")
        print(work)
        print()

    # return json object of workouts
    return jsonify(all_public_workout_json), 200


@listlogic.route('/like-or-unlike-workout', methods=['POST'])
@cross_origin()
def like_or_unlike_workout():
    """
    get the current workout
    get the current user
    add or remove the workout to the liked list
    """

    # get the current workout
    data = request.json
    currWorkoutId = data.get("workoutId")
    workout = session.query(models.WorkoutLists).filter_by(id=currWorkoutId).first()

    print("workout")
    print(workout)
    print()

    # get the current number of likes
    workout_like = workout.likes
    print("workout likes: ")
    print(workout_like)
    print()

    # get the username
    username = data.get('owner') # "name"
    username = username[1:len(username)-1] # name
    user = session.query(models.User).filter_by(username=username).first()


    # add it if it's in there
    if workout not in user.liked_workouts:
        user.liked_workouts.append(workout)
        workout.likes = workout_like + 1
    else:
        user.liked_workouts.remove(workout)
        workout.likes = workout_like - 1

    session.commit()

    jsonObj = [{"num_likes":workout.likes}]

    return jsonify(jsonObj), 200


# DONE
@listlogic.route('/get-num-likes', methods=['POST'])
@cross_origin()
def get_num_likes():

    # get current workout
    data = request.json
    currWorkoutId = data.get("workoutId")
    workout = session.query(models.WorkoutLists).filter_by(id=currWorkoutId).first()

    jsonObj = [{"num_likes":workout.likes}]

    return jsonify(jsonObj), 200


# IP
@listlogic.route('/get-if-liked', methods=['POST'])
@cross_origin()
def get_if_liked():

    # get current workout
    data = request.json
    currWorkoutId = data.get("workoutId")
    workout = session.query(models.WorkoutLists).filter_by(id=currWorkoutId).first()
    
    print("workout right now!")
    print(workout)
    print()

    # get current user
    username = data.get('owner') # "name"
    username = username[1:len(username)-1] # name
    user = session.query(models.User).filter_by(username=username).first()

    jsonObj = []
    for w in user.liked_workouts:
        print("w and workout")
        print(w)
        print(workout)
        if w.id == workout.id:
            jsonObj = [{"liked": True}]
        else:
            jsonObj = [{"liked": False}]
    
    print("here")
    print(jsonObj)
    print()
    
    return jsonify(jsonObj), 200


# DONE
@listlogic.route('/delete-workout', methods=['POST'])
@cross_origin()
def delete_workout():
    
    # get current workout
    data = request.json
    currWorkoutId = data.get("workoutId")

    print("current workout id:")
    print(currWorkoutId)
    print()
    
    # delete workout
    workout = session.query(models.WorkoutLists).filter_by(id=currWorkoutId).first()
    if not workout:
        return jsonify({"error": "No associated workout"}), 406
    session.delete(workout)
    session.commit()

    return jsonify({"status":"workout deleted!"}), 200
