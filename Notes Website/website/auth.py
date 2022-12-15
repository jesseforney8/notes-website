from flask import Blueprint, render_template, request, flash, redirect, url_for
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
from __init__ import db
from flask_login import login_required, login_user, logout_user, current_user

# stores routes

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["POST", "GET"])

# will run when you hit page
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in", category="success")
                login_user(user, remember=True)
                return redirect("/")
            else:
                flash("Incorrect Password!", category="error")
        else:
            flash("Account doesn't Exist!", category="error")
            #return redirect("/sign-up")

    return render_template("login.html", user=current_user)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/login")

@auth.route("/sign-up", methods=["GET", "POST"])

def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        firstname = request.form.get("firstname")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        print(email, firstname, password1, password2)
        

        user = User.query.filter_by(email=email).first()

        if user:
            flash("Email already exists.", category="error")
        elif len(email) <= 4:
            flash("Email must be greater than 4 characters.", category="error")
        elif password1 != password2:
            flash("Passwords don't match!.", category="error")
        elif len(password1) <= 4:
            flash("Password must be greater than 4 characters.", category="error")
        else:
            new_user = User(email=email, firstname=firstname, password=generate_password_hash(password1, method="sha256"))

            db.session.add(new_user)
            db.session.commit()
            # login_user(user, remember=True)
            flash("Account created!", category="success")
            return redirect("/")


    return render_template("sign_up.html", user=current_user)



