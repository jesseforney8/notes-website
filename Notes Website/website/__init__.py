from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

#creates DB and then assigns it a name
db = SQLAlchemy()
DB_NAME = "database.db"

#creates flask app then returns it
def create_app():
    app1 = Flask(__name__)

    # encrypt cookies for website
    app1.config["SECRET_KEY"] = "hfh^%$#@383"

    # telling flash where the db is located
    app1.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    
    #initalizing db and pointing it to the flask app
    db.init_app(app1)


    # register and import blueprints from views and auth

    from views import views
    from auth import auth

    app1.register_blueprint(views, url_prefix="/")
    app1.register_blueprint(auth, url_prefix="/")

    #import models file so it deinfes the classes for the DB
    from models import User, Note

    with app1.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = "/login"
    login_manager.init_app(app1)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app1

#creates DB

