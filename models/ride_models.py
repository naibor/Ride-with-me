"""ride models classes"""
from datetime import datetime, timedelta
from models.db import db

driver_info = []
# driver's information displayed to passanger in ride offer details
ride_offers = []
# A list of ride offers
request_details = []
# requests saved
DTime = datetime.now() + timedelta(minutes=45) #departure time after 45min


class DriverOffer:
    """Driver offers ride"""
    def __init__(self,location,destination ):
        self.location = location
        self.destination = destination
        self.departure = str(DTime.time())
 
    def save_ride_offer(self):
        """save ride offer"""
        new_ride = {
            "location":self.location,
            "destination":self.destination,
            "departure":self.departure
                }
        db.cursor.execute(
            """
            INSERT INTO ride_offers (user_id, offer_location, offer_destination)
            VALUES (%d, %s, %s)
            """,
            (1, self.location, self.destination)
        )
        offer = db.cursor.fetchall()
        return offer
    @staticmethod
    def get_all():
        """get all ride offers"""
    # getting all rides  
        db.query_db(
            "SELECT * FROM ride_offers;"
        )
        ride_offers = db.cursor.fetchall()
        return ride_offers
        



    def ride_by_id(self):
        """check if ride exists"""
        for offer in ride_offers:
            if offer["ID"] == self.ride_id:
                return offer
            else:
                return{"message":"ride does not exist"}
    # getting a specific id
        db.cursor.execute(
        """
        SELECT ride_offers.offer_id,
        ride_offers.offer_location,
        ride_offers.offer_destination,
        ride_offers.offer_departure_time,
        users.user_username,
        users.user_car,
        users.user_phone_number
        FROM ride_offers, users
        WHERE ride_offers.user_id = users.user_id
        AND ride_offers.offer_id =%d
        """
        (id,)
        )
        a_ride = db.cursor.fetchall()
        return a_ride
       
class Rrequest(DriverOffer):
    """User make request a ride"""
    def __init__ (self,location,destination,phone_number):
        DriverOffer.__init__(self,location,destination)
        self.phone_number = phone_number

    def save_request_ride(self):
        """user can save ride requests"""
        new_request = {
            "location":self.location,
            "destination":self.destination,
            "phone_number":self.phone_number
        }
        # request_details.append(new_request)
        # return {"message":"Request to join ride is being processed"}

# create a ride request
        db.cursor.execute(
            """
            INSERT INTO ride_requests(request_location,request_destination,request_phone_number)
            VALUE(%s, %s, %d)
            """
            (self.location, self.destination, self.phone_number)
        )
        made_request = db.cursor.fetchall()
        return made_request

    def get_requests_for_offer(self):
        """get all requests to a specific offer"""
# all requests to a specific ride offer
        db.cursor.execute(
            """
            SELECT *FROM ride_requests
            WHERE offer_id = %d
            """
            (id,)
        )
        the_requests = db.cursor.fetchall()
        return the_requests