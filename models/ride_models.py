"""ride models classes"""
from datetime import datetime, timedelta
from models.db import db

DTime = datetime.now() + timedelta(minutes=45) 


class DriverOffer:
    """Driver offers ride"""
    def __init__(self, user_offer_id, location, destination):
        self.user_offer_id = user_offer_id
        self.location = location
        self.destination = destination
        self.departure = str(DTime.time())
      
 
    def save_ride_offer(self):
        """save ride offer"""
        db.cursor.execute(
            """
            INSERT INTO ride_offers (user_offer_id, offer_location, offer_destination, offer_departure_time)
            VALUES (%s, %s, %s, %s)
            """,
            (self.user_offer_id, self.location, self.destination, self.departure)
        )
        db.commit()
        db.cursor.execute(
            """
            SELECT * FROM ride_offers
            WHERE user_offer_id = %s
            """,
            (self.user_offer_id, )
        )
        offers = db.cursor.fetchone()
        return offers
    @staticmethod
    def get_all():
        """get all ride offers"""
    # getting all rides  
        db.query_db(
            "SELECT * FROM ride_offers;"
        )
        ride_offers = db.cursor.fetchall()
        return ride_offers
        
    @staticmethod
    def ride_by_id(offer_id):
        """gets ride by id"""          
    # getting a specific id
        db.cursor.execute(
            """
            SELECT * FROM ride_offers
            where offer_id = (%s)
            """,
            (offer_id,)
        )
        offer = db.cursor.fetchall()
        return (offer)
 
       
class Rrequest(DriverOffer):
    """User make request a ride"""
    def __init__ (self, user_id, phone_number, offer_id, user_offer_id, location, destination, departure_time):
        DriverOffer.__init__(self, offer_id, user_offer_id, location, destination, departure_time)
        self.phone_number = phone_number
        self.user_id = user_id

    def save_request_ride(self):
        """user can save ride requests"""
# create a ride request
        db.cursor.execute(
            """
            INSERT INTO ride_requests(offer_id, user_id, request_location, request_destination, request_phone_number)
            VALUE(%s, %s, %s, %s, %s)
            """
            (self.offer_id, self.user_id, self.location, self.destination, self.phone_number)
        )
        return {"message":"Request to join ride is being processed"}

    def get_requests_for_offer(self):
        """get all requests to a specific offer"""
# all requests to a specific ride offer
        db.cursor.execute(
            """
            SELECT *FROM ride_requests
            WHERE offer_id = (%s),
            """
            (self.offer_id,)
        )
        the_requests = db.cursor.fetchall()
        return the_requests
    