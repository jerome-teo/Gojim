from flask import Flask, request, jsonify
from auth import auth
from listslogic import listlogic
from users import users

app = Flask(__name__)
app.register_blueprint(auth)
app.register_blueprint(listlogic)
app.register_blueprint(users)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'hello world this is the secret key'
    app.run(debug=True)