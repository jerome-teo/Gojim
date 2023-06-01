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
    '''
    if username=="shivani" and password=="hello1234":
        response = {"status": "success"}
        return response, 200
    else:
        return 'error', 401
    '''
    return jsonify({}) 

@auth.route('/logout', methods=['GET'])
@login_required # don't want user to access this page unless they've logged out
def logout():
    logout_user() # logs-out current user
    # redirects to the page that is rendered in login function
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['POST'])
def sign_up():
    #try:
        #create_user(request.form.get('username'),
                    #request.form.get('password'),
                    #request.form.get('name'),
                    #request.form.get('email'))
    #except:
        #return "Signup unsuccessful", 500 # VERY broad catch statement
    return "<p>Sign Up</p>"


#### Backend Authentication Logic

#users = {} # Make into DB table

#def create_user(username, password, name, email, publicly_visible=True):
#   pass


# tags:hiit,upperbody,lowerbody,fullbody