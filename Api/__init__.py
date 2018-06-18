from flask import Flask
from flask_restful import Api

app = Flask('Api',instance_relative_config=True)

api=Api()
# add resource function 

api.init_app(app)


