"""User and driver models"""
user_info = {}
driver_detail = {}


class User:
    """User model class"""
    def __init__(self,name,username,password,confirmpassword):
        self.name = name
        self.username = username
        self.password = password
        self.confirmpassword = confirmpassword
class Driver:
    """Driver model class"""
    def __init__(self,name,username,car, phone_number, password,confirmpassword):
        self.name = name
        self.username = username
        self.phone_number = phone_number
        self.car = car
        self.password = password
        self.confirmpassword = confirmpassword

    def save_driver_details(self,username,phone_number, car):
        driver_detail = [self.username] = {"type_of_car":self.car,
                                        "phone_number":self.phone_number
                                        }