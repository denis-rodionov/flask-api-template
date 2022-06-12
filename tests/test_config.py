import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app("config.app_config_test.AppConfigTest")
    # other setup can go here
    return app.test_client()
    # clean up / reset resources here