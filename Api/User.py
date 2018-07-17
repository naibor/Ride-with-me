"""user sign up, driver registration and login resource"""
from flask_restful import Resource, Api
from flask import request

from Api.schema_v import Userschema, driverschema
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from models.user_model import User, Driver, login_required


class UserSignUp(Resource):
    """user signup resource"""
    def post(self):
    #     """
    #    User signup
    #    ---
    #    description:User signup
    #    parameters:
    #      - in: body
    #        name: User
    #        type: string
    #        required: true
    #        schema:
    #         $ref: '#/definitions/Passenger_sign_up'
    #    responses:
    #      201:successfully signed up
    #        description: 
    #      400:
    #         description:Bad request

    #     """
        signup_data = request.get_json()   
        data, errors = Userschema.load(signup_data)
        if errors:
           return(errors),400 
        else:
            new_user = User(
                data["name"],
                data["username"],
                data["phone_number"],
                data["password"],
                data["confirmpassword"]
            )
            exist = new_user.user_exist(data["username"])
            if exist:
                return {"message":"user already exists"}, 400
            invalid_password = new_user.confirm_password()
            if invalid_password:
                return invalid_password, 400
            else:
                A_user = new_user.save_user()
                return A_user, 201 

class DriverReg(Resource):
    """Driver registeration resource"""
    def post(self):
    #     """
    #    Driver registration
    #    ---
    #    description:Driver register
    #    parameters:
    #      - in: body
    #        name: Driver
    #        type: string
    #        required: true
    #        schema:
    #         $ref: '#/definitions/Driver_register'
    #    responses:
    #      201:successfully signup as a driver
    #        description: 
    #      400:
    #         description:Bad request

    #     """
        regData = request.get_json()
        data,errors =  driverschema.load(regData)
        if errors:
            return(errors),400 
        else:
            new_driver = Driver(
                data["name"],
                data["username"],
                data["phone_number"],
                data["car"],
                data["password"],
                data["confirmpassword"]
            )
            exist = new_driver.user_exist(data["username"])
            if exist:
                return {"message":"user already exists"}, 400
            invalid_password = new_driver.confirm_password()
            if invalid_password:
                return (invalid_password), 400
            else:
                A_driver = new_driver.save_driver()
                return A_driver, 201

        
class UserLogIn(Resource):
    """userlogin resource"""
    
    def post(self):
        # """
        # Login
        # ---
        # description: User login

        # parameters:
        #     - in: body
        #       name: Login 
        #       schema:
        #         $ref: '#/definitions/User_login'
        # responses:
        # 200:
        #     description: successfully logged in
        # 400:
        #     description: Bad request
        # 404:
        #     description: Wrong password
        # """


        data = request.get_json()
        fetched = User.user_exist(data["username"])
        if not fetched:
            return  {"message": "signup first"}, 400
        response = User.checks_password(data["username"], data["password"])
        return response