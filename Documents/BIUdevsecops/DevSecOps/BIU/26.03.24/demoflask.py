from flask import Flask, request, jsonify
import db


all_tasks = {
    1 : {'title' : 'buy' , 'details' : 'milk'},
    2 : {'title' : 'clean', 'clean' : 'kitchen'},
    3 : {'title' : 'call', 'details' : 'mary'}
}

all_tasks_2 = [
    {'id':1, 'title' : 'buy' , 'details' : 'milk'},
    {'id':2,'title' : 'clean', 'clean' : 'kitchen'},
    {'id':3, 'title' : 'call', 'details' : 'mary'}
]


all_tasks_3 = [
    [1, 'buy', 'milk'],
    [2, 'clean', 'kitchen'],
    [3, 'call', 'marry']
]

app = Flask(__name__)

app.route("/demo",  methods=["GET"])
def get_demo():
    data = '("key" : "value")'
    return  data

app.route("/demo", methods=["POST"])
def retrieve_demo():


app.run()