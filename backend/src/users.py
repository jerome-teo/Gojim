from flask import Blueprint, request
from flask_jwt_extended import jwt_required

users = Blueprint('users', __name__)

@users.route('/profile', methods=['GET'])
#@jwt_required
def profile():
    return "<p>Profile</p>"

@users.route('/settings', methods=["PUT"])
@jwt_required
def settings():
    return "<p>Settings</p>"