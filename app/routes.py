from flask import request
from app import app
from flask_restful import Resource, Api, marshal_with, fields
from app.models import Task
from app.database import db
from app.serializers import taskFields
from datetime import datetime


api = Api(app)

# This handles List and Create operations for Task.
class Items(Resource):
    
    # List operations
    @marshal_with(taskFields)
    def get(self):
        tasks = Task.query.all()
        return tasks
    
    # Create operations
    @marshal_with(taskFields)
    def post(self):
        data = request.json
        task = Task(name=data['name'], status=data['status'])
        db.session.add(task)
        db.session.commit()
        return task
    

# This handles Detail, Update, and Delete operations for Task instances
class Item(Resource):
    
    # Details of a Task instance
    @marshal_with(taskFields)
    def get(self, pk):
        task = Task.query.filter_by(id=pk).first()
        return task
    
    # Update the Task instance
    @marshal_with(taskFields)
    def put(self, pk):
        task = Task.query.filter_by(id=pk).first()
        task.name = request.json['name']
        task.status = request.json['status']
        task.last_updated = datetime.now()
        db.session.commit()
        return task
    
    # Deletes a Task Instance
    @marshal_with(taskFields)
    def delete(self, pk):
        task = Task.query.filter_by(id=pk).first()
        db.session.delete(task)
        db.session.commit()
        return task
    

# Route Links for List & Create tasks
api.add_resource(Items, '/')

# Route Links for Detail, Update, and Delete tasks using <pk> as Instance identifier
api.add_resource(Item, '/<int:pk>')
