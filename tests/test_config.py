from unittest.mock import Mock

import pytest

from app import create_app


@pytest.fixture
def todo_service():
    return Mock()


@pytest.fixture
def client(todo_service):
    app = create_app("config.app_config_test.AppConfigTest", todo_service)
    # other setup can go here
    return app.test_client()
    # clean up / reset resources here