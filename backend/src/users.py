from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from auth import session
import models

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


@users.route('/make-acc-public', methods=["POST"])
@jwt_required()
def make_acc_public():
    """
    get the current user
    set their privacy boolean to False
    """

    data = request.json
    username = data.get('owner') # "name"
    username = username[1:len(username)-1] # name
    user = session.query(models.User).filter_by(username=username).first()
    user.privacy = False

    return jsonify({"status":"Account made public!"}), 200

@users.route('/make-acc-private', methods=["POST"])
@jwt_required()
def make_acc_public():
    """
    get the current user
    set their privacy boolean to true
    """

    data = request.json
    username = data.get('owner') # "name"
    username = username[1:len(username)-1] # name
    user = session.query(models.User).filter_by(username=username).first()
    user.privacy = True

    return jsonify({"status":"Account made private!"}), 200