#### Flask Routing Logic
from flask import Blueprint, request, redirect, flash, jsonify, url_for
import models
from sqlalchemy.orm import sessionmaker
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

# create Session
Session = sessionmaker(bind=models.engine)
session = Session()

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # newUser = models.User("tim@gmail.com", "shivani", "hello1234", "tim")
    # session.add(newUser)
    # session.commit()

    # check if we have this user in our database, look for a specific entry
    user = session.query(models.User).filter_by(username=username).first() # filter all users by this email and returns the first result
    print(user)

    # should only get one user because users much have usernames
    if user:
        if check_password_hash(user.password, password): # if passwords are the same
            flash('Logged in successfully!', category='success')
            login_user(user, remember=True) # remembers that user is logged
            # redirect user to home page
            return jsonify({}) # turn this into a json object that we can return, but we're returning nothing here
        else:
            flash('Incorrect password, try again.', category='error')
    else:
        flash('Email does not exist.', category='error')
    return jsonify({}) 

    '''
    if username=="shivani" and password=="hello1234":
        response = {"status": "success"}
        return response, 200
    else:
        return 'error', 401
    '''

@auth.route('/logout', methods=['GET'])
@login_required # don't want user to access this page unless they've logged out
def logout():
    logout_user() # logs-out current user
    # redirects to the page that is rendered in login function
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['POST'])
def sign_up():
    email = request.form.get('email')
    username = request.form.get('username')
    name = request.form.get('name')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    #### Validating Infomation
    # check to make sure that user doesn't already exist
    user = session.query(models.User).filter_by(username=username).first()
    print(user)
    if user:
        flash('Email already exists.', category='error')
        return "Signup unsuccessful", 500

    # message flashing: flash a msg on screen using flask, import flash
    if len(email) < 4:
        # tell user there's an issue
        flash('Email must be greater than 3 characters', category='error')
    elif len(username) < 4:
        flash('Username must be greater than 3 characters', category='error')
    elif len(name) < 2:
        flash('Name must be greater than 1 character', category='error')
    elif password1 != password2:
        flash('Passwords don\'t match.', category='error')
    elif len(password1) < 7:
        flash('Password must be at least 7 characters', category='error')
    else:
        # add user to database
        newUser = models.User(email=email, username=username, name=name, password=generate_password_hash(password1, method='scrypt'))
        # sha256, scrypt are hashing algorithms, there's others as well
        session.add(newUser) # add user to database
        # commit to the database
        session.commit()
        login_user(newUser, remember=True)
        flash('Account created!', category='success')

        # redirect user to home page
        return jsonify({}) 

    # try:
    #     create_user(request.form.get('username'),
    #                 request.form.get('password'),
    #                 request.form.get('name'),
    #                 request.form.get('email'))
    # except:
    #     return "Signup unsuccessful", 500 # VERY broad catch statement


#### Backend Authentication Logic

#users = {} # Make into DB table

#def create_user(username, password, name, email, publicly_visible=True):
#   pass


# tags:hiit,upperbody,lowerbody,fullbody