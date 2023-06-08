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
<<<<<<< Updated upstream
    return "<p>Change Email</p>"
=======
    data = request.json
    username=data.get('username')
    username=username.strip('\"')
    newemail=data.get('email')

    user = session.query(models.User).filter_by(username=username).first()
    emailalreadyexists = session.query(models.User).filter_by(email=newemail).first()
    if not user:
        return jsonify({"error": "No associated account"}), 406
    if len(newemail) < 8:
        return jsonify({"error": "invalid email"}), 406
    if emailalreadyexists:
        return jsonify({"error": "Email already used."}), 406
    user.email = newemail
    session.commit()
    return jsonify({"message": "Email changed successfully."}), 200

@users.route('/delete-account', methods=["POST"])
@cross_origin()
#@jwt_required()
def delete_account():
    data = request.json
    username=data.get('username')
    username=username.strip('\"')
    
    user = session.query(models.User).filter_by(username=username).first()
    if not user:
        return jsonify({"error": "No associated account"}), 406
    session.delete(user)
    session.commit()
    
    return jsonify({"message": "Account deleted."}), 200
>>>>>>> Stashed changes


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