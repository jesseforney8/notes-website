from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from __init__ import db
from models import Note
import json
# stores routes

views = Blueprint("views", __name__)

@views.route('/', methods=["POST", "GET"])
@login_required
def home():
    if request.method == "POST":
        note = request.form.get("note")
        note1 = Note(data=note, user_id=current_user.id)
        db.session.add(note1)
        db.session.commit()

    return render_template("home.html", email=current_user.email, user=current_user)
# will run when you hit page

@views.route("/test", methods=["POST", "GET"])
def test():
    data = request.form
    print(data)
    return render_template("test1.html")

@views.route("/delete-note", methods=["POST"])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            
    return jsonify({})