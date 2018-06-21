from flask import Flask
from flask_restful import Resource, Api
from models import user_model
from Instance.config import app_config
from Api.User import UserSignUp, UserLogIn, DriverReg
from Api.ride import RideRequest, RideOffer, DriverRideOffer 
# flask instance 


def create_app(config_name):
    app = Flask('Api')
    app.config.from_object(app_config['development'])
    api=Api(app)

    # api.init_app(app)
    
    api.add_resource(UserSignUp,'/api/v1/user/signup')
    api.add_resource(UserLogIn,'/api/v1/user/auth')
    api.add_resource(DriverReg,'/api/v1/user/register')
    api.add_resource(RideRequest,'/api/v1/user/request')
    api.add_resource(DriverRideOffer,'/api/v1/user/create')
    api.add_resource(RideOffer,'/api/v1/user/offer/<location>', endpoint='location' )
    # api.add_resource(RideOffer,'/api/v1/user/offer/<int:id>', endpoint='arideoffer')

    return app