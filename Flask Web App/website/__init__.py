from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager # manages login related things

db = SQLAlchemy() # object we'll use when we make new users
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hello world this is the secret key'

    # sqlalchemy database is located at sqlite in DB_NAME
    # f string: whatever's put in strings is evaluated
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    #initialize database
    db.init_app(app)
    
    # blueprints imported
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # creating the database
    from .models import User, Note #OR
    #import .models as models // either works
    # importing defines the databases before we create them 
    create_database(app)

    # handles what pages we can and can't access
    loginManager = LoginManager()
    loginManager.login_view = 'auth.login' # name of our template and fnc
    loginManager.init_app(app)

    # tells flask how we load our user & what user we're looking for
    # for more advanced loading, change the body of the fnc
    @loginManager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    # if we change the folder name, change the path name
    '''
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
    '''
    with app.app_context():
        db.create_all()
        print('Created Database!')