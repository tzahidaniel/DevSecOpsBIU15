from flask import Flask, jsonify, request

app = Flask(__name__)

all_tasks = {
    1: {'title': 'buy', 'details': 'milk'},
    2: {'title': 'clean', 'details': 'kitchen'},
    3: {'title': 'call', 'details': 'mary'}
}

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(all_tasks)

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = all_tasks.get(task_id)
    if task:
        return jsonify(task)
    else:
        return jsonify({'message': 'Task not found'}), 404

@app.route('/tasks', methods=['POST'])
def add_task():
    new_task = request.json
    if request.json and 'title' in request.json and 'details' in request.json:
        new_id = max(all_tasks.keys()) + 1
        all_tasks[new_id] = {
            'id' : new_id,
            'title': request.json['title'],
            'details': request.json['details']
        }
        return jsonify(all_tasks[new_id]), 201
    else:
        return jsonify({'message': 'Request must contain title and details'}), 400

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    if task_id in all_tasks and request.json:
        task = all_tasks[task_id]
        task['title'] = request.json.get('title', task['title'])
        task['details'] = request.json.get('details', task['details'])
        return jsonify(task)
    else:
        return jsonify({'message': 'Task not found or invalid request'}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if task_id in all_tasks:
        del all_tasks[task_id]
        return jsonify({'message': 'Task deleted'}), 200
    else:
        return jsonify({'message': 'Task not found'}), 404

if __name__ == '__main__':
    app.run()
