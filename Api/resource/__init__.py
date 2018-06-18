from Instance.config import app_config
from Api import api
from flask import Flask

def create_app(config_name):
    app = Flask("Api", instance_relative_config=True)
    app.config.from_object(app_config['development'])
    return app