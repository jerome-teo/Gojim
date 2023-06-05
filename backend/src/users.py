from flask import Blueprint, request
from flask_jwt_extended import jwt_required

users = Blueprint('users', __name__)

@users.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    return "<p>Profile</p>"

@users.route('/settings', methods=["PUT"])
@jwt_required()
def settings():
    return "<p>Settings</p>"

@users.route('/change-pwd', methods=["POST"])
@jwt_required()
def change_pwd():
    return "<p>Change Password</p>"

@users.route('/change-username', methods=["POST"])
@jwt_required()
def change_username():
    return "<p>Change Username</p>"

@users.route('/change-email', methods=["POST"])
@jwt_required()
def change_email():
    return "<p>Change Email</p>"