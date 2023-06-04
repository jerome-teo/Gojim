from flask import Flask, request, jsonify, flash
from auth import auth
from listslogic import listlogic
from users import users
from flask_cors import CORS, cross_origin
import models
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
CORS(app, supports_credentials=True, resources={r"/*": {"origins": "http://localhost:3000"}})
app.register_blueprint(auth)
app.register_blueprint(listlogic)
app.register_blueprint(users)

Session = sessionmaker(bind=models.engine)
session = Session()

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'hello world this is the secret key'
    app.run(debug=True)