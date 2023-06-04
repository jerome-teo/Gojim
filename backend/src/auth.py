#### Flask Routing Logic
from flask import Blueprint, request, redirect, flash, jsonify, url_for, session
import models
#from __init__ import app
from sqlalchemy.orm import sessionmaker
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS, cross_origin
from flask_jwt_extended import create_access_token, get_jwt, get_jwt_identity, \
                                unset_jwt_cookies, jwt_required, JWTManager

# create Session
Session = sessionmaker(bind=models.engine)
session = Session()

auth = Blueprint('auth', __name__)
# CORS(app, supports_credentials=True)

@auth.route('/login', methods=['POST'])
@cross_origin()
def login():
    #json or form???
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # newUser = models.User("tim@gmail.com", "shivani", "hello1234",)
    # session.add(newUser)
    # session.commit()

    # check if we have this user in our database, look for a specific entry
    user = session.query(models.User).filter_by(username=username).first() # filter all users by this email and returns the first result
    print(user)

    # should only get one user because users much have usernames
    if user:
        # HEREE: i try to store the username of the curr session's user, but for some reason it's failing here
        # which means that it's failing to create a new workout list in listlogic
        #session["username"] = request.form['username'] # create a session for them
        if check_password_hash(user.password, password): # if passwords are the same
            access_token = create_access_token(identity=username)
            # SUS
            # login_user(user, remember=True) # remembers that user is logged
            # redirect user to home page
            response = {"acess_token": access_token}
            return jsonify(response), 200 # turn this into a json object that we can return, but we're returning nothing here
        else:
            return jsonify({"error":"Incorrect password, try again."}),500
    else:
        return jsonify({"error":"Incorrect password, try again."}),500
    '''
    if username=="shivani" and password=="hello1234":
        response = {"status": "success"}
        return response, 200
    else:
        return 'error', 401
    '''

@auth.route('/logout', methods=['GET'])
# @login_required # don't want user to access this page unless they've logged in
@jwt_required # that' you've been loggin in to be able to logout
def logout():
    # session.pop("username")
    # logout_user() # logs-out current user
    # redirects to the page that is rendered in login function

    response = jsonify({"msg":"logout successful"})
    unset_jwt_cookies(response)
    return response
    # return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['POST'])
@cross_origin()
def sign_up():
    data = request.json
    email = data.get('email')
    username = data.get('username')
    password1 = data.get('password1')
    password2 = data.get('password2')
    #check
    #return jsonify({"message": "DONE"}), 200
    # email = request.form.get('email')
    # username = request.form.get('username')
    # #name = request.form.get('name')
    # password1 = request.form.get('password1')
    # password2 = request.form.get('password2')

    #### Validating Infomation
    # check to make sure that user doesn't already exist
    user = session.query(models.User).filter_by(username=username).first()
    print(user)
    if user:
        flash('Email already exists.', category='error')
        return jsonify({"error": "Signup unsuccessful"}), 500

    # message flashing: flash a msg on screen using flask, import flash
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
        #I removed name=name
        newUser = models.User(email=email, username=username, password=generate_password_hash(password1, method='scrypt'), privacy=False)
        # sha256, scrypt are hashing algorithms, there's others as well
        session.add(newUser) # add user to database
        # commit to the database
        session.commit()
        login_user(newUser, remember=True)

        # redirect user to home page
        return jsonify({
            "email": newUser.email,
            "username": newUser.username,
            "password": newUser.password
            # "name": newUser.name,
        }), 200

    # try:
    #     create_user(request.form.get('username'),
    #                 request.form.get('password'),
    #                 request.form.get('name'),
    #                 request.form.get('email'))
    # except:
    #     return "Signup unsuccessful", 500 # VERY broad catch statement

@auth.route('/delete-account', methods=['DELETE'])
def delete_acc():
    return "<p>Delete Account</p>"

# tags:hiit,upperbody,lowerbody,fullbody