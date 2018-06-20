from flask_restful import Resource, Api
# from flask import Flask
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
# hashes passwords

# app = Flask('Api') 
# flask instance
# api = Api(app)
signup_info = []
driver_info = []
driver_details = {}

class UserSignUp(Resource):
    # inherits from resource

    def post(self):
        # user post signup data
        signup_data = request.get_json()
        # returns data in json format
        hashed_password = generate_password_hash(signup_data.get("password"), method="sha256")

        # validation starts now
        # firstname
        # lastname
        # username
        # password
        # confirmpassword

        # checks if data field is empty
        if not signup_data.get("firstname"):
            return{'message':"enter first name"},401
        if not signup_data.get("lastname"):
            return{'message':"enter last name"},401
        if not signup_data.get("username"):
            return{'message':"enter user name"},401
        if not signup_data.get("password"):
            return{'message':"enter password"},401
        if not signup_data.get("confirmpassword"):
            return{'message':"enter confirm password"},401

        # checks if data is an empty string

        if signup_data.get("firstname") == " ":
            return{'message':"enter visible character"},401
        if signup_data.get("lastname") == " ":
            return{'message':"enter visible character"},401
        if signup_data.get("username") == " ":
            return{'message':"enter visible character"},401
        if signup_data.get("password") == " ":
            return{'message':"enter visible character"},401
        if signup_data.get("confirmpassword") == " ":
            return{'message':"enter visible character"},401

        # confirms confirm password and password is the same
        if signup_data.get("password") != signup_data.get("confirmpassword"):
            return{"message":"put same shit"}
        
        # an instance of class ser containing user data
        new_user = User(signup_data.get("firstname"),
                        signup_data.get("lastname"),
                        signup_data.get("username"),
                        hashed_password
                        )

                        
        # save new user to signup info a list
        signup_info.append({"firstname":new_user.firstname,
                      "lastname":new_user.lastname,
                      "username":new_user.username,
                       "password":hashed_password
                       })
        return{"message":"Welcome you have successfully signed up"},201            
 
 class DriverReg(Resource):
     def post(self):
        regData = request.get_json()
        hashed_password = generate_password_hash(regData.get("password"), method="sha256")

        # check empty field
        if not regData.get("firstname"):
            return{'message':"enter first name"},401
        if not regData.get("lastname"):
            return{'message':"enter last name"},401
        if not regData.get("username"):
            return{'message':"enter user name"},401
        if not regData.get("phone_number"):
            return{'message':"enter phone number"},401
        if not regData.get("password"):
            return{'message':"enter password"},401
        if not regData.get("car"):
            return{'message':"enter your type of car"},401
        if not regData.get("confirmpassword"):
            return{'message':"enter confirm password"},401

        # checks for spaces only field
        if regData.get("firstname") == " ":
            return{'message':"enter visible character"},401
        if regData.get("lastname") == " ":
            return{'message':"enter visible character"},401
        if regData.get("username") == " ":
            return{'message':"enter visible character"},401
        if regData.get("phone_number") == " ":
            return{'message':"enter visible character"},401
        if regData.get("car") == " ":
            return{'message':"enter visible character"},401    
        if regData.get("password") == " ":
            return{'message':"enter visible character"},401
        if regData.get("confirmpassword") == " ":
            return{'message':"enter visible character"},401

     # confirms confirm password and password is the same
        if regData.get("password") != regData.get("confirmpassword"):
            return{"message":"password and confirm password not the same"}
        
        # an instance of class ser containing user data
        new_driver = Driver(regData.get("firstname"),
                            regData.get("lastname"),
                            regData.get("username"),
                            regData.get("car"),
                            hashed_password
                            )
        # save driver_details a dict the one people will see
        driver_details[new_driver.firstname] = {"type_of_car":new_driver.car}

                        
        # save new drive to driver info a list
        driver_info.append({"firstname":new_user.firstname,
                            "lastname":new_user.lastname,
                            "username":new_user.username,
                            "password":hashed_password,
                            "driver_detail":driver_details
                            })
        return{"message":"Welcome you have successfully registeredto be a driver"},201  


<<<<<<< HEAD
=======
class UserLogIn(Resource):
    # userlogin resource
    def post(self):
        # username and password requied
        data = request.get_json()
        for dictionary in signup_info:
            if data.get("username") == dictionary["username"]:
                # compares given and stored hash passwords
                if check_password_hash(dictionary["password"], data.get("password")):
                    access_token =jwt.encode({"username":username, "exp":datetime.utcnow() + datetime.timedelta(hour = 1)},"this is my secret key to encode the token")
                    return {"token":token.decode("UTF -8"),"message":"successfully logged in"},200

                return{"message":"wrong password"}
            return{"message":"signup first"}

>>>>>>> ft-login-api-158430273

            


# api.add_resource(UserSignUp,'api/v1/user/signup')
# api.add_resource(UserLogIn,'api/v1/user/auth')
# api.add_resource(DriverReg,'api/v1/user/register')


    
 