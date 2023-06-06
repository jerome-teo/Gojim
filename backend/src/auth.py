#### Flask Routing Logic
from flask import Blueprint, request, redirect, flash, jsonify, url_for, session
import models
from sqlalchemy.orm import sessionmaker
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS, cross_origin
from flask_jwt_extended import create_access_token, set_refresh_cookies, get_jwt, get_jwt_identity, \
                                unset_jwt_cookies, jwt_required, JWTManager, set_access_cookies, create_refresh_token

# create Session
Session = sessionmaker(bind=models.engine)
session = Session()

auth = Blueprint('auth', __name__)
# CORS(app, supports_credentials=True)

@auth.route('/login', methods=['POST'])
@cross_origin()
def login():
    # data = request.json
    data = request.form
    print("DATA:")
    print(data)
    print()
    username = data.get('username')
    password = data.get('password')

    # newUser = models.User("tim@gmail.com", username, password, privacy=False)
    # session.add(newUser)
    # session.commit()
    # print("newuser: ")
    # print(newUser)
    # print()

    # check if we have this user in our database, look for a specific entry
    user = session.query(models.User).filter_by(username=username).first() # filter all users by this email and returns the first result
    print(user)
    print()

    # should only get one user because users much have usernames
    if user:
        if check_password_hash(user.password, password): # if passwords are the same
            access_token = create_access_token(identity=username)
            refresh_token = create_refresh_token(identity=username)
            response = jsonify({"acess_token": access_token})

            #response.set_cookie('access_token', access_token, httponly=True)
            set_access_cookies(response, access_token)
            set_refresh_cookies(response, refresh_token)
            return response, 200 # turn this into a json object that we can return, but we're returning nothing here
        else:
            return jsonify({"error":"Incorrect password, try again."}),500
    else:
        return jsonify({"error":"user not found, try again."}),500


@auth.route('/logout', methods=['GET'])
# @login_required # don't want user to access this page unless they've logged in
# @jwt_required() # that' you've been loggin in to be able to logout
def logout():
    # session.pop("username")
    # logout_user() # logs-out current user
    # redirects to the page that is rendered in login function

    # response = jsonify({"msg":"logout successful"})
    # unset_jwt_cookies(response)
    # return response
    pass


@auth.route('/sign-up', methods=['POST'])
@cross_origin()
def sign_up():
    # data = request.json
    data = request.form
    email = data.get('email')
    username = data.get('username')
    password1 = data.get('password1')
    password2 = data.get('password2')
    print("DATA:")
    print(data)
    print()

    #### Validating Infomation
    # check to make sure that user doesn't already exist
    user = session.query(models.User).filter_by(username=username).first()
    print(user)
    if user:
        return jsonify({"error": "Signup unsuccessful"}), 500

    if len(email) < 4:
        # tell user there's an issue
        return jsonify({"error": "Signup unsuccessful"}), 500
    elif len(username) < 4:
        return jsonify({"error": "Signup unsuccessful"}), 500
    elif password1 != password2:
        return jsonify({"error": "Signup unsuccessful"}), 500
    elif len(password1) < 7:
        return jsonify({"error": "Signup unsuccessful"}), 500
    else:
        # add user to database
        newUser = models.User(email=email, username=username, password=generate_password_hash(password1, method='sha224'), privacy=False)
        # sha256, scrypt are hashing algorithms, there's others as well
        session.add(newUser) # add user to database
        # commit to the database
        session.commit()
        #login_user(newUser, remember=True)

        # redirect user to home page
        return jsonify({
            "email": newUser.email,
            "username": newUser.username,
            "password": newUser.password
            # "name": newUser.name,
        }), 200


@auth.route('/delete-account', methods=['DELETE'])
def delete_acc():
    return "<p>Delete Account</p>"

# tags:hiit,upperbody,lowerbody,fullbody