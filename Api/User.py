
from flask_restful import Resource, Api

from flask import request

from Api.schema_v import Userschema, driverschema

from werkzeug.security import generate_password_hash, check_password_hash
# hashes passwords
from datetime import datetime, timedelta
# to get departure time
from models.user_model import User,Driver
import jwt

signup_info = []
# where user signup information is stored
driver_info = []
# where driver information is stored after registration
driver_details = {}
# the driver details a passanger user sees while viewing ride_offers[].

# the driver details a passanger user sees while viewing ride_offers[].


class UserSignUp(Resource):
    # inherits from resource
    def post(self):
        # user post signup data
        signup_data = request.get_json()        
        # returns data in json format
        # validation starts
        data, errors =Userschema.load(signup_data)
        if errors:
           return{"error":errors},400 

        # confirms confirm password == password is the same
        if signup_data.get("password") != signup_data.get("confirmpassword"):
            return{"message":"password and confirm password not the same"}
        # checks for an existing ussesr.avoid multiple signups
        for user in signup_info:
            if signup_data.get("username") == user["username"]:
                return {"message":"username already exist"},400
        # an instance of User in models containing user data

        hashed_password = generate_password_hash(signup_data.get("password"), method="sha256")
        hashed_confirmpassword = generate_password_hash(signup_data.get("confirmpassword"), method="sha256")
        new_user = User(signup_data.get("name"),
                        signup_data.get("username"),
                        hashed_password,
                        hashed_confirmpassword
                        )           
        # save new user as a {}, to signup info[]
        signup_info.append({"name":new_user.name,
                            "username":new_user.username,
                            "password":hashed_password
                          })
        # import pdb;pdb.set_trace()
        return{"message":"Welcome you have successfully signed up"},201            
 
    def get(self):
        return {"message":"Welcome to Ride with me"}
        pass


class DriverReg(Resource):
    #class driver registration  resource

    def post(self):
        regData = request.get_json()
        hashed_password = generate_password_hash(regData.get("password"), method="sha256")
        hashed_confirmpassword = generate_password_hash(regData.get("confirmpassword"), method="sha256")


        # validation required
        data,errors =driverschema.load(regData)
        if errors:
            return{"error":errors},400 
            # instance of driver
        new_driver = Driver(regData.get("name"),
                        regData.get("username"),
                        regData.get("phone_number"),
                        regData.get("car"),
                        hashed_password,
                        hashed_confirmpassword 
                            )

        # check if the driver is an exisiting driver
        for driver in driver_info:
            if regData.get("username") == driver["username"]:
                return {"message":"This is an existing driver"},400
                        
        # save new drive to driver info[]

        driver_info.append({"name":new_driver.name,
                            "username":new_driver.username,
                            "password":hashed_password,
                            "driver_detail":driver_details
                            })
        print("driver_info")
        return{"message":"Welcome you have successfully registered as a driver"},201  

class UserLogIn(Resource):
    # userlogin resource
    def post(self):
        
        # username and password requied
        data = request.get_json()
        for dictionary in signup_info:
            if data.get("username") == dictionary["username"]:
                # compares given and stored hash passwords
                if check_password_hash(dictionary["password"], data.get("password")):
                    # access_token =jwt.encode({"username":dictionary["username"],
                    #                           "exp":datetime.utcnow() + timedelta(minutes=60)},
                    #                           "this is my secret key to encode the token")
                    # import pdb;pdb.set_trace()
                    # "token":access_token.decode("UTF -8"),
                    return {"message":"successfully logged in"},200

                return{"message":"wrong password"},401
        return{"message":"signup first"},400
