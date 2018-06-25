from datetime import datetime, timedelta
from Api.User import driver_details
# import from user model
driver_info=[]
driver_detail={}
# driver's information displayed to passanger in ride offer details
ride_Offers = []

DTime = datetime.now() + timedelta(minutes=20)


class RRequest:
    """User make request a ride"""
    def __init__ (self,location,destination):
        self.location = location
        self.destination = destination
        departure = DTime.time()
        ride_id = len(ride_offers)
        driver_details = driver_detail


class RideRequest:
    """User request a ride"""
    def __init__(self,location,destination):
        self.location = location
        self.destination = destination

        self.departure =str(DTime.time())
        self.ride_id = len(ride_Offers) + 1
        self.driver_detail = driver_details


