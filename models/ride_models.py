"""ride models classes"""
from datetime import datetime, timedelta
from models.db import db

DTime = datetime.now() + timedelta(minutes=45) 


class DriverOffer:
    """Driver offers ride"""
    def __init__(self, user_id, location, destination ):
        self.user_id = user_id
        self.location = location
        self.destination = destination
        self.departure = str(DTime.time())
      
 
    def save_ride_offer(self):
        """save ride offer"""
        # create an offer
        db.cursor.execute(
            """
            INSERT INTO ride_offers (user_offer_id, offer_location, offer_destination, offer_departure_time)
            VALUES (%s, %s, %s, %s)
            """,
            (self.user_id, self.location, self.destination, self.departure)
        )
        db.commit()
        db.cursor.execute(
            """
            SELECT * FROM ride_offers
            WHERE user_offer_id = %s
            """,
            (self.user_id, )
        )
        offers = db.cursor.fetchall()
        return offers
    @staticmethod
    def get_all():
        """get all ride offers"""
    # getting all rides  
        db.query_db(
            "SELECT * FROM ride_offers;"
        )
        ride_offers = db.cursor.fetchall()
        print(ride_offers)
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


# create a ride request
        db.cursor.execute(
            """
            INSERT INTO ride_requests(request_location,request_destination,request_phone_number)
            VALUE(%s, %s, %d)
            """
            (self.location, self.destination, self.phone_number)
        )
        made_request = db.cursor.fetchall()
        return {"message":"Request to join ride is being processed"}

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