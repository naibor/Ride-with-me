"""ride models classes"""
from datetime import datetime, timedelta
from models.user_model import driver_detail
# import from user model
driver_info = []
# driver's information displayed to passanger in ride offer details
ride_Offers = []
# A list of ride offers
# departure time for the ride offer.
DTime = datetime.now() + timedelta(minutes=20)

class Rrequest:
    """User make request a ride"""
    def __init__ (self,location,destination):
        self.location = location
        self.destination = destination


class DriverOffer:
    """Driver offers ride"""
    def __init__(self,location,destination,driver_details):
        self.location = location
        self.destination = destination
        self.departure = str(DTime.time())
        self.ride_id = len(ride_Offers) + 1
        self.driver_details = driver_detail
