from flask import Blueprint, jsonify, request
import models
from auth import session
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_cors import cross_origin

search = Blueprint('search', __name__)

@search.route('/search', methods=['POST'])
@cross_origin()
# @jwt_required()
def search_for_workout():
    """
    get the input word (advaned, upper-body, intermediate, etc etc)
    get all the workout objs
    loop through workout objs
        loop through the tags in the workout obj
        if the tag matches the input
        add it to a list of workouts_json
    return the list of workouts json obj
    """

    workout_json = []

    data = request.json
    input_tag = data.get("tagString")
    print("this is input tag")
    print(input_tag)
    print()

    input_tags = input_tag.split('\n')

    print("here is input tags:")
    print(input_tags)
    print()

    inputs = []
    for tag in input_tags:
        if tag != "":
            inputs.append(tag)

    print("new tags:")
    print(inputs)
    print()

    all_workouts = session.query(models.WorkoutLists).all()
    for w in all_workouts:
        # Find owner of workout
        # Query the session for owner's privacy settings
        # Save privacy setting into a boolean
        user = session.query(models.User).filter_by(username=w.owner).first()
        privacy = user.privacy
        all_tags = w.tags.split('\n')
        for t in all_tags:
            for tag in inputs:
                if t == tag and privacy == False:
                    print("the tag is:")
                    print(tag)

                    # Add workout only if user is public
                    workout_json.append({'id': w.id, 'name':w.name, 'workoutString':w.info, 'likes':w.likes})
    return_workout = []
    
    # workout_json = list(set(workout_json))
    for workout in workout_json:
        if workout not in return_workout:
            print("here are workouts:")
            print(workout)
            return_workout.append(workout)

    # if workout_json is not empty, successful, else send EMPTY LIST tag not found
    if return_workout:
        return jsonify(return_workout), 200
    else:
        return jsonify(return_workout), 406