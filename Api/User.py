"""user sign up, driver registration and login resource"""
from flask_restful import Resource, Api
from flask import request
from Api.schema_v import Userschema, driverschema
from werkzeug.security import generate_password_hash, check_password_hash
# hashes passwords
from datetime import datetime, timedelta
# to get departure time
from models.user_model import User,Driver

signup_info = []
# where user signup information is stored
driver_info = []
# where driver information is stored after registration
driver_details = {}
# the driver details a passanger user sees while viewing ride_offers[].
class UserSignUp(Resource):
    """user signup resource"""
    # inherits from resource
    def post(self):
        # user post signup data
        signup_data = request.get_json()   
        # validation starts
        data, errors = userschema.load(signup_data)
        if errors:
           return{errors},400 
        else:
            new_user = User(
                data["name"],
                data["username"],
                data["password"],
                data["confirmpassword"]
            )
            Exist = new_user.User_exist()
            if Exist:
                return Exist, 400
            invalid_password = new_user.confirm_password()
            if invalid_password:
                return invalid_password, 400
            else:
                A_user = new_user.save_user()
                return A_user, 201 

class DriverReg(Resource):
    """Driver registeration resource"""
    #class driver registration  resource
    def post(self):
        regData = request.get_json()
        # validation required
        data,errors =  driverschema.load(regData)
        if errors:
            return{errors},400 
        else:
            new_driver = Driver(
                data["name"],
                data["username"],
                data["phone_number"],
                data["car"],
                data["password"],
                data["confirmpassword"]
            )
            exist = new_driver.driver_exist()
            if exist:
                return exist, 400
            invalid_password = new_driver.confirm_password()
            if invalid_password:
                return invalid_password, 400
            else:
                A_driver = new_driver.save_driver()
                return A_driver, 201 

        
class UserLogIn(Resource):
    """userlogin resource"""
    def post(self):
        # username and password requied
        data = request.get_json()
        for dictionary in signup_info:
            if data["username"] == dictionary["username"]:
                # compares given and stored hash passwords
                if check_password_hash(dictionary["password"], data["password"]):
                    return {"message":"successfully logged in"},200
                return{"message":"wrong password"},401
        return{"message":"signup first"},400

