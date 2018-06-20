user_info={}


class User:
    def __init__(self,firstname,lastname,username,password):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password

class Driver:
    def __init__(self, firstname, lastname, username, phone_number,car):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.phone_number = phone_number
        self.car = car

