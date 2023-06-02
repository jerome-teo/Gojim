from flask import Blueprint, request

listlogic = Blueprint('listlogic', __name__)

@listlogic.route('/my-workouts', methods=['GET'])
def my_workouts():
    return "<p>My Workouts</p>"

@listlogic.route('/saved-workouts', methods=['GET'])
def saved_workouts():
    return "<p>Saved Workouts</p>"

@listlogic.route('/public-workouts', methods=['GET'])
def public_workouts():
    return "<p>Public Workouts</p>"

@listlogic.route('/new-workout', methods=['POST'])
def new_workout():
    return "<p>Add New Workout</p>"