from flask import Flask, request, jsonify
from auth import auth
from listslogic import listlogic
from users import users
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.register_blueprint(auth)
app.register_blueprint(listlogic)
app.register_blueprint(users)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'hello world this is the secret key'
    app.run(debug=True)