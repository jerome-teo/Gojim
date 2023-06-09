from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from flask_cors import cross_origin
from sqlalchemy.orm import sessionmaker
import models
from auth import session
from werkzeug.security import check_password_hash, generate_password_hash

users = Blueprint('users', __name__)

@users.route('/profile', methods=['GET'])
def profile():
    return "<p>Profile</p>"


@users.route('/getprivacy', methods=['POST'])
@cross_origin()
def getprivacy():
    data = request.json
    username = data.get('username')
    username = username.strip('\"')
    user = session.query(models.User).filter_by(username=username).first()
    if not user:
        return jsonify({"error": "No associated account"}), 406
    else:
        privacy = user.privacy
        settings = {
            'privacy' : privacy
        }
        return jsonify(settings), 200


@users.route('/privacy', methods=["POST"])
@cross_origin()
def settings():
    data = request.json
    username = data.get('username')
    username = username.strip('\"')
    user = session.query(models.User).filter_by(username=username).first()
    if not user:
        return jsonify({"error": "No associated account"}), 406
    else:
        user.privacy = not user.privacy
        session.commit()
    return jsonify({"message": "Private settings changed successfully."}), 200


@users.route('/change-pwd', methods=["POST"])
@cross_origin()
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
        session.commit()
    else:
        return jsonify({"error": "Wrong password"}), 406

    return jsonify({"message": "Password changed successfully."}), 200


@users.route('/change-username', methods=["POST"])
@cross_origin()
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
    session.commit()
    return jsonify({"message": "Username changed successfully."}), 200


@users.route('/change-email', methods=["POST"])
@cross_origin()
def change_email():
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
