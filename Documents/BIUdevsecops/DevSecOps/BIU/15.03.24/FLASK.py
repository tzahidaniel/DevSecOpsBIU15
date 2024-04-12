the "tasks" project

Create a "tasks" project based on Flask.
It will run a REST-API server that will enable you to create/read/update/delete (CRUD)
tasks that you have to do.
A single task should contain a title and some details:
('title':'shop', 'details':'Milk'}

This is how you should use your program using "curl":

# Get all tasks
# This will use GET by default
curl http://127.0.0.1:5000/tasks


# This will use GET to get a specific task
curl http://127.0.0.1:5000/tasks/2


# Add a new task:
# (You have to specify Content-Type to send data as json)
curl  -X POST
      -H "Content-Type: application/json"
      -d '{  "title": "buy", "details": "Milk"}' http://127.0.0.1:5000/tasks

Use simmilar patterns to implement delete and update.

GET  (to read data)
POST (to create a new one)
PUT  (to update an existing one)
DELETE (to delete an existing one)