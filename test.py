from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse



app = Flask(__name__)

app.app_context()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
api = Api(app)
app.app_context().push()

class TODO(db.Model):
    id = db.Column(db.Integer, primary_key = True, index = True)
    name = db.Column(db.String(32), nullable= False)
    description = db.Column(db.String(32), nullable = False )

db.create_all()

@app.route('/')
def welcome():
    return "Welcome"

#@app.route('/getToDo')
#def getToDo():
    #SELECT * FROM todo
    #todo_list = []

    #todo = TODO.query.all()

    #for todo in todo:
        #todoObj = {
            #'id': todo.id,
            #'name': todo.name,
            #'description': todo.description

        #}
        #todo_list.append(todoObj)

    #return jsonify(todo_list)

class TODOListResource(Resource):
    # functon
    # method

    def get(self):
        todo_list = []

        todo = TODO.query.all()

        for todo in todo:
            todoObj = {
                'id' : todo.id,
                'name': todo.name,
                'description': todo.description
            }
            todo_list.append(todoObj)

        return todo_list
    
api.add_resource(TODOListResource, "/allTodo")
