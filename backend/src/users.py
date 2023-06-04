from flask import Blueprint, request

users = Blueprint('users', __name__)

@users.route('/profile', methods=['GET'])
def profile():
    return "<p>Profile</p>"

@users.route('/settings', methods=["PUT"])
def settings():
    return "<p>Settings</p>"

@users.route('/change-pwd', methods=["POST"])
def change_pwd():
    return "<p>Change Password</p>"

@users.route('/change-username', methods=["POST"])
def change_username():
    return "<p>Change Username</p>"

@users.route('/change-email', methods=["POST"])
def change_email():
    return "<p>Change Email</p>"