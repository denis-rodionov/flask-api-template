"""Flask configuration for unit and integration tests"""
from config.app_config import AppConfig


class AppConfigTest(AppConfig):
    SWAGGER = False