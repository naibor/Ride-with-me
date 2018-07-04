"""User and driver models"""
from werkzeug.security import generate_password_hash, check_password_hash
from models.db import db   

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
        if db.cursor.fetchone():
            return {"message":"user already exists"}

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
            INSERT INTO user(user_name, user_username, user_phone_number, user_password)
            VALUES(%s, %s, %s, %s)
            """,
            (self.name, self.username, self.phone_number, self.password)
        )
        db.commit()
        return {"message":"successfully signed up"}

   
            
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
