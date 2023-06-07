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
@cross_origin()
#@jwt_required()
def change_username():
    data = request.json
    oldusername = data.get('username')
    oldusername = oldusername.strip('\"')
    newusername = data.get('newusername')
    
    user = session.query(models.User).filter_by(username=oldusername).first()
    #If user is not logged in, unable to change username
    if not user:
        return jsonify({"error": "No associated account"}), 406
    #If the newusername is already taken
    newuser = session.query(models.User).filter_by(username=newusername).first()
    if newuser:
        return jsonify({"error": "Username already taken."}), 406
    #If the newusername is too short or too long
    if len(newusername) < 8 or len(newusername) > 16:
        return jsonify({"error": "invalid username"}), 406
    user.username = newusername
    return jsonify({"message": "Username changed successfully."}), 200


@users.route('/change-email', methods=["POST"])
#@jwt_required()
def change_email():
    return "<p>Change Email</p>"