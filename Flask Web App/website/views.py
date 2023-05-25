from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
# current_user is used to determine if user is logged in or not and we can access user's attributes
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            # create note obj, add it to database
            newNote = Note(data=note, userID=current_user.id)
            db.session.add(newNote)
            db.session.commit()
            flash('Note added!', category='success')

    # we will be able to reference current user in our template and check if they are authenticated
    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteID = note['noteID']
    note = Note.query.get(noteID)
    if note:
        if note.userID == current_user.id: # if the user that is signed in owns the note (security check)
            db.session.delete(note)
            db.session.commit()
    
    return jsonify({}) # turn this into a json object that we can return, but we're returning nothing here
