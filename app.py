from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin

from flask import Flask, jsonify
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

from routes.todo_list import ToDoList

app = Flask(__name__)
CORS(app)

# Register Method Views
todo_list_view = ToDoList.as_view("todo_list")
app.add_url_rule("/todo", view_func=todo_list_view)

# Create an APISpec
api_url = '/api/swagger.json'
spec = APISpec(
    title="Swagger Spec for TO-DO List API",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)

with app.test_request_context():
    spec.path(view=todo_list_view, summary="TO-DO List API", description="Manage to-do lists")

@app.route(api_url)
def create_swagger_spec():
    return jsonify(spec.to_dict())


# Registering Swagger UI
swagger_url = '/swagger'
swaggerui_blueprint = get_swaggerui_blueprint(
    swagger_url,
    api_url,
    config={
        'app_name': "Test REST API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=swagger_url)


if __name__ == '__main__':
        app.run(host='0.0.0.0')