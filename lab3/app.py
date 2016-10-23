# Done by: Tan Shun Yu (1001171), Nigel Leong (1001095)
# API for a todo list that can help you to keep track of your tasks
# MISC API - Magic 8 Ball, 6 Sided Dice
from flask import Flask, jsonify, abort, make_response, request
from flask_httpauth import HTTPBasicAuth
from random import randint

app = Flask(__name__)

auth = HTTPBasicAuth()

# hardcoded first 2 tasks in the todo list, the tasks can be created/updated/deleted
# array of dictionaries 'tasks' for storage
tasks = [
    {
        'id': 1,
        'title': 'go to NTUC to buy groceries',
        'desc': 'apples, milk, fish, beansprouts, salmon',
        'done': False
    },
    {
        'id': 2,
        'title': 'learn how to cycle',
        'desc': 'drop by Ulu Pandan Canal with my brand new bike!',
        'done': False
    }
]

# get all tasks in the todo list
@app.route('/todo/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# get a specific task by its id
@app.route('/todo/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    # search tasks array for the desired task
    myTask = [task for task in tasks if task['id'] == task_id]
    if len(myTask) == 0:
        # if task id does not exist in the todo list, throw 404 not found
        abort(404)
    return jsonify({'task': myTask[0]})



# create a new task and add it into the todo list
# able to accept two mimetypes - plain text and json
@app.route('/todo/tasks', methods=['POST'])
def create_task():
    newid = tasks[-1]['id'] + 1
    # plain text POST allows for quickly recording down a reminder or note on-the-go
    if request.headers['Content-Type'] == 'text/plain':
        task = {
            'id': newid,
            'title': 'quick task',
            'desc': request.data.decode('UTF-8'),
            'done': False
        }
        tasks.append(task)
        return jsonify({'task': task}), 201
    # json POST allows for more details in the task recorded
    elif request.headers['Content-Type'] == 'application/json':
        task = {
            'id': newid,
            'title': request.json['title'],
            'desc': request.json.get('desc', ""),
            'done': False
        }
        tasks.append(task)
        return jsonify({'task': task}), 201
    else:
        # bad request
        abort(400)

# update the nouns of an existing task in the todo list
# updating requires authentication
@app.route('/todo/tasks/<int:task_id>', methods=['PUT'])
@auth.login_required
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'desc' in request.json and type(request.json['desc']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['desc'] = request.json.get('desc', task[0]['desc'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

# delete a task from the todo list
# deleting requires authentication
@app.route('/todo/tasks/<int:task_id>', methods=['DELETE'])
@auth.login_required
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'deletion': True})

# login authentication details
@auth.get_password
def get_password(username):
    if username == 'nils':
        return 'elo'
    return None

# error handlers
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'Error': 'Not found, the resource you requested does not exist in the server.'}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'Error': 'The server is unable to understand your request.'}), 404)

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'Error': 'Unauthorized access, please achieve the way of the nils.'}), 403)

@app.route('/misc/8ball', methods=['GET'])
def eightball():
    # magic 8 ball
    eightballdict = {1:'It is certain', 2:'It is known', 3:'Yes, definitely', 4:'Most likely', 5:'Without a doubt', 6:'Ask again later', 7:'Concentrate and ask again', 8:'Dont count on it', 9:'My reply is no', 10:'Very doubtful'}
    return jsonify({'answer': eightballdict[randint(1,10)]})

@app.route('/misc/dice', methods=['GET'])
def rolldice():
    # 6 sided dice
    return jsonify({'rolled': randint(1,6)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
