user_info={}


class User:
    def __init__(self,name,username,password,confirmpassword):
        self.name = name
        self.username = username
        self.password = password

class Driver:
    def __init__(self,name,username,car, phone_number, password,confirmpassword):
        self.name = name
        self.username = username
        self.phone_number = phone_number
        self.car = car

