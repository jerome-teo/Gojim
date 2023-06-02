from flask import Blueprint, request

users = Blueprint('users', __name__)

@users.route('/profile', methods=['GET'])
def profile():
    return "<p>Profile</p>"

@users.route('/settings', methods=["PUT"])
def settings():
    return "<p>Settings</p>"