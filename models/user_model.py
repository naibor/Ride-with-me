user_info={}
driver_detail={}


class User:
    def __init__(self,firstname,lastname,username,password,confirmpassword):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.confirmpassword = confirmpassword
class Driver:
    def __init__(self, firstname, lastname, username,car, phone_number, password,confirmpassword):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.phone_number = phone_number
        self.car = car
        self.password = password
        self.confirmpassword = confirmpassword

    def save_driver_details(self,username,phone_number, car):
        driver_detail = [self.username]= {"type_of_car":self.car,
                                        "phone_number":self.phone_number
                                        }