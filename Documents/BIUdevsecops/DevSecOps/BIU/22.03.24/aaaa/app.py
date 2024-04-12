from flask import Flask, request, jsonify
from db import get_tasks, get_task_by_id, add_task, update_task, delete_task
import json

app = Flask(__name__)

@app.route('/tasks', methods=['GET'])
def handle_get_tasks():
    """Return all tasks."""
    tasks = get_tasks()
    return jsonify(tasks)

@app.route('/tasks/<int:task_id>', methods=['GET'])
def handle_get_task_by_id(task_id):
    """Return a task by its ID."""
    task = get_task_by_id(task_id)
    if task:
        return jsonify(task)
    return "Task not found", 404

@app.route('/tasks', methods=['POST'])
def handle_add_task():
    """Add a new task."""
    if request.is_json:
        data = request.get_json()
        task = add_task(data['title'], data['details'])
        return jsonify(task), 201
    return "Invalid request", 400

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def handle_update_task(task_id):
    """Update an existing task."""
    if request.is_json:
        data = request.get_json()
        task = update_task(task_id, data['title'], data['details'])
        if task:
            return jsonify(task)
    return "Task not found or invalid request", 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def handle_delete_task(task_id):
    """Delete a task."""
    delete_task(task_id)
    return "Task deleted", 200

if __name__ == '__main__':
    app.run(debug=True)
