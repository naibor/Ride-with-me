"""imports and endpoints from resources"""
from flask import Flask
from flask_restful import Resource, Api
from Instance.config import app_config
from models import user_model
from Api.User import UserSignUp, UserLogIn, DriverReg
from Api.ride import RideOffer,RideRequest, SpecificRequest



def create_app(config_name):
    app = Flask('Api')
    app.config.from_object(app_config[config_name])
    api = Api(app)

 
    api.add_resource(UserSignUp,'/api/v1/auth/signup')
    api.add_resource(UserLogIn,'/api/v1/auth/login')
    api.add_resource(DriverReg,'/api/v1/auth/register')
    api.add_resource(RideOffer,'/api/v1/users/rides')
    api.add_resource(RideRequest, '/api/v1/users/rides/<int:id>')
    api.add_resource(SpecificRequest,'/api/v1/users/rides/<int:id>/request',endpoint='join_ride_request')
    return app