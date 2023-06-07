from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from flask_cors import cross_origin
from sqlalchemy.orm import sessionmaker
import models
from auth import session
from werkzeug.security import check_password_hash, generate_password_hash

users = Blueprint('users', __name__)

@users.route('/profile', methods=['GET'])
#@jwt_required()
def profile():
    return "<p>Profile</p>"

@users.route('/settings', methods=["PUT"])
#@jwt_required()
def settings():
    return "<p>Settings</p>"

@users.route('/change-pwd', methods=["POST"])
@cross_origin()
#@jwt_required()
def change_pwd():
    data = request.json
    oldpassword = data.get('oldpassword')
    newpassword = data.get('newpassword')
    
    username = data.get('username')
    username=username.strip('\"')
    user = session.query(models.User).filter_by(username=username).first()
    if not user:
        return jsonify({"error": "No associated account"}), 406
    if check_password_hash(user.password, oldpassword):
        if len(newpassword) < 8:
            return jsonify({"error": "Invalid password"}), 406
        user.password = generate_password_hash(newpassword, method='sha224')
    else:
        return jsonify({"error": "Wrong password"}), 406

    return jsonify({"message": "Password changed successfully."}), 200

@users.route('/change-username', methods=["POST"])
#@jwt_required()
def change_username():
    return "<p>Change Username</p>"

@users.route('/change-email', methods=["POST"])
#@jwt_required()
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
def make_acc_private():
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