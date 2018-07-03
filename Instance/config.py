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

def configdb(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return db
        
    
