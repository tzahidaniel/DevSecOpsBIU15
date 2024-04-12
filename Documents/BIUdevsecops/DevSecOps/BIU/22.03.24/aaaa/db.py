# This is a simple in-memory "database" for our Flask application.

# Initialize the list with one task.
all_tasks = [{'id': 1, 'title': 'shop', 'details': 'Milk'}]

def get_tasks():
    """Return all tasks."""
    return all_tasks

def get_task_by_id(task_id):
    """Return a task by its ID."""
    for task in all_tasks:
        if task['id'] == task_id:
            return task
    return None

def add_task(title, details):
    """Add a new task to the list."""
    new_id = max(task['id'] for task in all_tasks) + 1 if all_tasks else 1
    all_tasks.append({'id': new_id, 'title': title, 'details': details})
    return all_tasks[-1]

def update_task(task_id, title, details):
    """Update an existing task."""
    for task in all_tasks:
        if task['id'] == task_id:
            task['title'] = title
            task['details'] = details
            return task
    return None

def delete_task(task_id):
    """Delete a task by its ID."""
    global all_tasks
    all_tasks = [task for task in all_tasks if task['id'] != task_id]
    return all_tasks
