"""User and driver models"""
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from flask import request
from functools import wraps
from models.db import db  
from datetime import timedelta 

class User():
    """User model class"""
    def __init__(self, name, username, phone_number, password, confirmpassword):
        self.name = name
        self.username = username
        self.phone_number = phone_number
        self.password = password
        self.confirmpassword = confirmpassword

    def user_exist(self):
        db.cursor.execute(
            """
            SELECT * FROM users
            WHERE user_username = %s
            """,
            (self.username, )
        )
        
        users_info_fetched = db.cursor.fetchone()
        return users_info_fetched
       
        #     return {"message":"user already exists"}

    def confirm_password(self):
        """ensures user password and confirm password are same"""
        if self.password != self.confirmpassword:
            return {"message": "password and confirm password not the same"}
        else:
            self.password = generate_password_hash(self.password, method="sha256")

    def save_user(self):
        """save user to user_info"""
        db.cursor.execute(
            """
            INSERT INTO users(user_name, user_username, user_phone_number, user_password)
            VALUES(%s, %s, %s, %s)
            """,
            (self.name, self.username, self.phone_number, self.password)
        )
        db.commit()
        return {"message":"successfully signed up"}

    def checks_password(self):
        p_user = self.user_exist()
        password = p_user[-1]
      
        if check_password_hash(password, self.password):
            access_token = jwt.encode(
            {"username":self.username},
            "this is a secret"
            )
            return {"access_token": access_token.decode("UTF-8"),"message":"successfully logged in"}
        return{"message":"wrong password"}

    
class Driver(User):
    """Driver model class"""
    def __init__(self, name, username, phone_number, car, password, confirmpassword):
        super().__init__(name, username, phone_number, password, confirmpassword)
        self.car = car

    def save_driver(self):
        self.save_user()
        db.cursor(
            """
            UPDATE users
            SET user_car = %s
            WHERE user_username = %s
            """,
            (self.car, self.username)
        )
        db.commit()


def login_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        # empty access_token
        access_token = None

        if "x-access-token" in request.headers:
            access_token = request.headers["x-access-token"]

        if not access_token:
            return{"message" : "Please Login is "},401
        
        try:
            data = jwt.decode(access_token, "this is a secret")
            # get the user to whom the token belongs to
            data.user_exist()
        except:
            return{"message":"invalid token"}, 401

        return func(this_user,*args,**kwargs)
    return decorated 


