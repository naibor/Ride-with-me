"""ride models classes"""
from datetime import datetime, timedelta
from models.user_model import driver_detail
# import from user model
driver_info = []
# driver's information displayed to passanger in ride offer details
ride_offers = []
# A list of ride offers
request_details = []
# where requests made my user are saved
DTime = datetime.now() + timedelta(minutes=45) #departure time after 45min

class DriverOffer:
    """Driver offers ride"""
    def __init__(self,location,destination ):
        self.location = location
        self.destination = destination
        self.departure = str(DTime.time())
        self.ride_id = len(ride_offers) + 1
        # self.driver_details = driver_detail
    
  
    def save_ride_offer(self):
        """save ride offer"""
        new_ride = {
            "ID":self.ride_id,
            "location":self.location,
            "destination":self.destination,
            "departure":self.departure,
            # "driver_details":self.driver_details
        }
        ride_offers.append(new_ride)
        return{"message":"ride offer successfully created "}

    def ride_by_id(self):
        """check if ride exists"""
        for offer in ride_offers:
            if offer["ID"] == self.ride_id:
                return offer
            else:
                return{"message":"ride does not exist"}


class Rrequest:
    """User make request a ride"""
    def __init__ (self,location,destination,phone_number):
        self.location = location
        self.destination = destination
        self.phone_number = phone_number

    def save_request_ride(self):
        """user can save ride requests"""
        new_request = {
            "location":self.location,
            "destination":self.destination,
            "phone_number":self.phone_number
        }
        request_details.append(new_request)
        return {"message":"Request to join ride is being processed"}
