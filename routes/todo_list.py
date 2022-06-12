"""TO-DO list API resource"""
from flask.views import MethodView
from marshmallow import Schema, fields


class TodoResponseSchema(Schema):
    title = fields.String(required=True)
    description = fields.String(metadata={'description': "Add full task description"})
    done = fields.Boolean()


class TodoListResponseSchema(Schema):
    todo_list = fields.List(fields.Nested(TodoResponseSchema))


class ToDoList(MethodView):
    """
    TODOLIST
    """
    def get(self):
        """ Get List of Todo
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
        return TodoListResponseSchema().dump({'todo_list': todo_list_data})


todo_list_data = [
    {
        'title': "Book a flight to Bali",
        'description': "Find the cheapest and fastest flight in best-flights.net",
        'done': False
    },
    {
        'title': "Pack the luggage",
        'description': "Write a list, pack the things in the suitcase",
        'done': True
    }
]

