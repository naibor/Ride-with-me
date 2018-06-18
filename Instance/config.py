import os

class Config(object):
    """parent congiguration class"""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')

class DevelopmentConfig(Config):
    """configurations for development"""
    DEBUG = True

class TestingConfig(Config):
    """configurations for testing """
    TESTING = True
    DEBUG = True

class StagingConfig(Config):
    """configurations for staging"""
    DEBUG = True

class ProductionConfig(Config):
    """Configuration for production"""
    DEBUG = True
    TESTING = False

app_config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'staging':StagingConfig,
    'production':ProductionConfig,
}
