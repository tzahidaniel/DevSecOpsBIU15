from flask import Flask, request
import json
import tasks_db

app = Flask(__name__)


@app.route("/tasks", methods=["GET"])
def get_all_tasks():
    '''this function returns all tasks to the web client
    Note that the current module does not keep DB locally'''
    # Go to tasks_db module, and get all tasks from there
    all_tasks = tasks_db.get_all_tasks()
    return json.dumps({'tasks': all_tasks})


@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            return json.dumps(task),
        return  json.dumps({"message": "Task not found"})



@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    tasks_id = len(tasks) +1
    tasks = {'id': tasks_id, 'title': data['title'], 'details': data['details']}
    tasks.append(task)
    return  json.dumps(["message:": f"Task number {task_id} was added"])




@app.route()