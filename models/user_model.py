"""User and driver models"""
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from flask import request
from functools import wraps
from models.db import db  

class User():
    """User model class"""
    def __init__(self, name, username, phone_number, password, confirmpassword):
        self.name = name
        self.username = username
        self.phone_number = phone_number
        self.password = password
        self.confirmpassword = confirmpassword

    @staticmethod
    def user_exist(username):
        db.cursor.execute(
            """
            SELECT * FROM users
            WHERE user_username = %s
            """,
            (username, )
        )
        users_info_fetched = db.cursor.fetchone()
        return users_info_fetched

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

    @staticmethod
    def checks_password(username, password):
        
        db.cursor.execute(
            """
            SELECT * FROM users
            WHERE user_username = %s
            """,
            (username, )
        )

        user_details = db.cursor.fetchone()
        if user_details and check_password_hash(
            user_details[-1],
            password
        ):
            access_token = jwt.encode(
            {"id":user_details[0],
            "driver": user_details[3]},
            "this is a secret"
            )
            return {"access_token": access_token.decode("UTF-8"),
            "message":"successfully logged in"}
        return{"message":"wrong password"}

    
class Driver(User):
    """Driver model class"""
    def __init__(self, name, username, phone_number, car, password, confirmpassword):
        super().__init__(name, username, phone_number, password, confirmpassword)
        self.car = car

    def save_driver(self):
        self.save_user()
        db.cursor.execute(
            """
            UPDATE users
            SET user_car = %s
            WHERE user_username = %s
            """,
            (self.car, self.username)
        )
        db.commit()
        return {"message":"successfully signup as a driver"}


def login_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        access_token = None
        if "Authorization" in request.headers:
            access_token = request.headers["Authorization"]
        if not access_token:
            return {"message" : "Please Log in or provide access token"},401
        
        try:
            data = jwt.decode(access_token, "this is a secret")
            # get the user to whom the token belongs to
        except:
            return {"message": "invalid token"}, 401

        db.cursor.execute(
            """
            SELECT * FROM users
            WHERE user_id=%s
            """,
            (str(data["id"]), )
        )
        this_user = db.cursor.fetchone()
        return func(this_user, *args, **kwargs)
    return decorated 
