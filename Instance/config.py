import os
from configparser import ConfigParser

class Config(object):
    """parent congiguration class"""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    

class DevelopmentConfig(Config):
    """configurations for development"""
    DEBUG = True
    DATABASE = os.getenv('.env')


class TestingConfig(Config):
    """configurations for testing """
    TESTING = True
    DEBUG = True
    DATABASE = os.getenv('.env.testing')


class ProductionConfig(Config):
    """Configuration for production"""
    DEBUG = True
    TESTING = False
    DATABASE = os.getenv('.env')

app_config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,
}
