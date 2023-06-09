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
    input_tags = input_tag.split('\n')

    all_workouts = session.query(models.WorkoutLists).all()
    for w in all_workouts:
        all_tags = w.tags.split('\n')
        for t in all_tags:
            for tag in input_tags:
                if t == tag:
                    workout_json.append({'id': w.id, 'name':w.name, 'workoutString':w.info, 'likes':w.likes})
    return_workout = []
    #workout_json = list(set(workout_json))
    for workout in workout_json:
        if workout not in return_workout:
            return_workout.append(workout)
    # if workout_json is not empty, successful, else send EMPTY LIST tag not found
    if return_workout:
        return jsonify(return_workout), 200
    else:
        return jsonify(return_workout), 406