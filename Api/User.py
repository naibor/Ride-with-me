from flask_restful import Resource, Api
# from flask import Flask
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
# hashes passwords

# app = Flask('Api') 
# flask instance
# api = Api(app)
signup_info = []

class UserSignUp(Resource):
    # inherits from resource

    def get(self):
        return {"okay":"this works"}


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


class UserLogIn(Resource):
    def post(self):
        data = request.get_json()
        for dictionary in signup_info:
            if data.get("username") == dictionary["username"]:
                # compares given and stored hash passwords
                if check_password_hash(dictionary["password"], data.get("password")):
                    access_token =jwt.encode({"username":username, "exp":datetime.utcnow() + datetime.timedelta(hour = 1)},"this is my secret key to encode the token")
                    return {"token":token.decode("UTF -8"),"message":"successfully logged in"},200

                return{"message":"wrong password"}
            return{"message":"signup first"}


            


# api.add_resource(UserSignUp,'api/v1/user/signup')
# api.add_resource(UserLogIn,'api/v1/user/auth')


    
 