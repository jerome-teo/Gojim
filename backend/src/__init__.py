from flask import Flask
from auth import auth
from listslogic import listlogic
from users import users
from flask_cors import CORS
import models
from sqlalchemy.orm import sessionmaker
from flask_jwt_extended import JWTManager


app = Flask(__name__)
CORS(app, supports_credentials=True, resources={r"/*": {"origins": "http://localhost:3000"}})
app.register_blueprint(auth)
app.register_blueprint(listlogic)
app.register_blueprint(users)
jwt = JWTManager(app)


Session = sessionmaker(bind=models.engine)
session = Session()

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'hello world this is the secret key'
    app.config['JWT_SECRET_KEY'] = 'hello world this is the jwt secret key'
    app.run(debug=True)