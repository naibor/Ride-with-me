user_info={}


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

