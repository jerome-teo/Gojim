from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
# to hash a password, import from flask login
from werkzeug.security import generate_password_hash, check_password_hash
# never store password as an actual password, you gotta make it secure
# hash fnc is a one way fnc such that it doesn't have an inverse
from . import db

from flask_login import login_user, login_required, logout_user, current_user
# current_user stuff can be used because we imported UserMixin in models.py

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    #data = request.form
    #print(data)
    # look at request.form attribute to look at the data in the login form

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # check if we have this user in our database, look for a specific entry
        user = User.query.filter_by(email=email).first() # filter all users by this email
        # should only get one user because users much have unique emails
        if user:
            if check_password_hash(user.password, password): # if passwords are the same
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True) # remembers that user is logged
                # redirect user to home page
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)
    # this is how you pass values to your template
    # you can also pass multiple variables
    # return render_template("login.html", text="Testing", user="Tim")

@auth.route('/logout')
@login_required # don't want user to access this page unless they've logged out
def logout():
    logout_user() # logs-out current user
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # validating infomation

        # check to make sure that user doesn't already exist
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')

        # message flashing: flash a msg on screen using flask, import flash
        if len(email) < 4:
            # tell user there's an issue
            flash('Email must be greater than 3 characters', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 character', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            # add user to database
            newUser = User(email=email, firstName=firstName, password=generate_password_hash(password1, method='scrypt'))
            # sha256, scrypt are hashing algorithms, there's others as well
            db.session.add(newUser) # add user to database
            # commit to the database
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created!', category='success')

            # redirect user to home page
            return redirect(url_for('views.home')) # views is the name of my blueprint and home is the fnc name that we wanna go to

    return render_template("sign_up.html", user=current_user)