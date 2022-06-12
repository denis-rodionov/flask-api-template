"""TO-DO list API resource"""
from flask import request
from flask.views import MethodView
from marshmallow import Schema, fields

from services.todo_service import TodoService


class TodoSchema(Schema):
    title = fields.String(required=True)
    description = fields.String(metadata={'description': "Add full task description"})
    done = fields.Boolean()


class TodoListResponseSchema(Schema):
    todo_list = fields.List(fields.Nested(TodoSchema))


class TodoListView(MethodView):
    def __init__(self, todo_service: TodoService):
        self.todo_service = todo_service

    def get(self):
        """
        ---
        summary: To-Do List
        tags:
            - To-Do
        description: Get List of Todos
        responses:
            200:
                description: Return a todo list
                content:
                    application/json:
                        schema: TodoListResponseSchema
        """
        return TodoListResponseSchema().dump({'todo_list': self.todo_service.get_all()})

    def post(self):
        """
        ---
        summary: Creates a new To-Do list item
        tags:
            - To-Do
        description: Creates a new To-Do list item and add it to the list
        requestBody:
            description: Optional description in *Markdown*
            required: true
            content:
                application/json:
                    schema: TodoSchema
        responses:
            201:
                description: Return a created item
                content:
                    application/json:
                        schema: TodoSchema
            400:
                description: validation errors
        """
        if not request.get_json(silent=True):
            return { 'error': "Cannot parse json" }, 400
        data = request.get_json()
        errors = TodoSchema().validate(data)
        if errors:
            return { 'Data validation errors': errors }, 400

        self.todo_service.add(data)
        return TodoSchema().dump(data), 201

