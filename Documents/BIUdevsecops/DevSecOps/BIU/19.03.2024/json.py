import json

all_tasks = [
    None,
    {'id': 1, 'title': 'shop', 'details': 'Milk'},
    {'id': 2, 'title': 'post-office', 'details': 'Send Letter'},
    {'id': 3, 'title': 'phone', 'details': 'Call Joan'},
    {'id': 4, 'title': 'kitchen', 'details': 'Wash the dishes'},
]


def get_all_tasks():
    dbfile = get_tasks_db()

    pass


def add_task(task):
    get_tasks_db()
    tasksdb = open('tasks.json')
    all_tasks = json.load(tasksdb)

    str_task = task.decode("utf-8")
    python_task = json.loads(str_task)
    all_tasks["tasks"].append(python_task)
    tasksdb.close()
    tasksdb = open('tasks.json', 'w')
    json.dump(all_tasks, tasksdb)
    tasksdb.close()


def delete_task():
    pass


def update_task():
    pass


def get_tasks_db():
    try:
        dbfile = open('tasks.json')
    except FileNotFoundError:
        dbfile = open('tasks.json', mode='w', encoding='utf-8')
        initial_data = {"id": 1, "tasks": []}

    dbfile.close()