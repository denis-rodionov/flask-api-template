from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin

from flask import Flask, jsonify
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

from config.app_config import AppConfig
from routes.todo_list_view import TodoListView
from services.todo_service import TodoService


# TODO: consider IoC instead of multiple dependencies
def create_app(config_object=AppConfig(), todo_service=TodoService()):
    app = Flask(__name__)
    CORS(app)

    # load config
    app.config.from_object(config_object)

    # Register Method Views
    todo_list_view = TodoListView.as_view("todo_list", todo_service=todo_service)
    app.add_url_rule("/todo", view_func=todo_list_view)

    if (app.config['SWAGGER']):
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

    return app