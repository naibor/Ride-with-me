"""User and driver models"""
from werkzeug.security import generate_password_hash, check_password_hash

user_info = []
driver_info = []

class User:
    """User model class"""
    def __init__(self,name,username,password,confirmpassword):
        self.name = name
        self.username = username
        self.password = password
        self.confirmpassword = confirmpassword

    def User_exist(self):
        if self.username in user_info:
            return {"message":"user already exists"}

    def confirm_password(self):
        """ensures user password and confirm password are same"""
        if self.password != self.confirmpassword:
            return {"message": "password and confirm password not the same"}
        else:
            self.password = generate_password_hash(self.password, method="sha256")

    def save_user(self):
        """save user to user_info"""
        new_user = {"name" : self.name,
            "username" : self.username,
            "password" : self.password
            }
        user_info.append(new_user)
        return{"message":"successfully signed up"}

   
            
class Driver(User):
    """Driver model class"""
    def __init__(self, name, username, phone_number, car, password, confirmpassword):
        User.__init__(self, name, username, password, confirmpassword)
        self.phone_number = phone_number
        self.car = car

    def driver_exist(self):
        for driver in driver_info:
            if driver["username"] == self.username:
                return {"message":"driver already exists"}

    def save_driver(self):
        new_driver = {"name":self.name,
                    "username":self.username,
                    "password":self.password
                     }
        driver_info.append(new_driver)
        return{"message":"successfully registered as a driver"},201 
        