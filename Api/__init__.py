from flask import Flask
from flask_restful import Resource, Api
from Api.resource import signup_info

app = Flask('Api',instance_relative_config=True)
# flask instance 

# mash = Marshmallow(app)
# add resource function 


api=Api()
api.add_resource(ViewOffer,"/")   
# api.init_app(app)