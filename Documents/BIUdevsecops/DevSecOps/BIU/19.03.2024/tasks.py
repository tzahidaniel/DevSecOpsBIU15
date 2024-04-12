from random import randint
from flask import Flask

app = Flask(__name__)

@app.route("/get_random")
def random():
    random_number = randint(1, 10)
    return {'random': random_number}, 200 # status code

@app.route('/hello')
@app.route('/hello/<user_name>')
def hello_user(user_name = 'no one'):
    return 'Hello ' + user_name, 200 # status code


@app.route("/welcome")
def welcome():
    return "<H1 id='welcome'>Welcome!</H1>", 200 # status code

app.run(host='127.0.0.1', debug=True, port=5000)