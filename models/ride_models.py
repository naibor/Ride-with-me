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
        
        return {"message":"Successfully created a ride offer"}

    @staticmethod
    def get_all():
        
        """get all ride offers"""  
        db.query_db(
            "SELECT * FROM ride_offers;"
        )
        ride_offers = db.cursor.fetchall()
        if not ride_offers:
            return{"message":"no ride offers yet, sorry"}, 404
        # else convert data to dict
        rides = []
        for item in ride_offers:
            ride_dict = {
                "ride_id":item[0],
                "driver_id":item[1],
                "location":item[2],
                "departure_time":item[3],
                "destination":item[4]
            }
            rides.append(ride_dict)
        return rides, 200

    
        
    @staticmethod
    def ride_by_id(offer_id):
        """gets ride by id""" 
        db.cursor.execute(
            """
            SELECT * FROM ride_offers
            where offer_id = (%s)
            """,
            (offer_id,)
        )
        offer = db.cursor.fetchone()
        the_offer = []
        if not offer:
            return {"message": "invalid offer id"}
        else:
                offer_dict = {
                    "offer_number":offer[0],
                    "location":offer[1],
                    "departure_time":offer[2],
                    "destination":offer[3]
                }
                the_offer.append(offer_dict)
        return the_offer
        

    @staticmethod
    def delete_ride_offer(offer_id):
        """gets ride by id"""          
        db.cursor.execute(
            """
            DELETE FROM ride_offers
            where offer_id = (%s)
            """,
            (offer_id,)
        )
        db.commit()
        return {"message": "ride deleted"}
 
       
class Rrequest(DriverOffer):
    """User make request to join a ride"""
    def __init__ (self, user_id, offer_id):
        self.user_id = user_id
        self.offer_id = offer_id
    

    def save_request_ride(self):
        """user can save ride requests"""
        db.cursor.execute(
            """
            INSERT INTO ride_requests(user_id, offer_id)
            VALUES(%s, %s)
            """,
            (self.user_id, self.offer_id)
        )
        db.commit()
        return

    @staticmethod   
    def get_requests_for_offer(id):
        """get all requests to a specific offer"""
        db.cursor.execute(
            """
            SELECT * FROM ride_requests
            WHERE offer_id = (%s)
            """,
            (id,)
        )
        the_requests = db.cursor.fetchall()
        request_list = []
        if not request_list:
            return{"message":"no ride requests to this offer"}, 400
        for request in the_requests:
            request_dict = {
               "request_number":request[0],
               "offer_number":request[1],
               "user_number":request[2],
               "status":request[3] 
            }
            request_list.append(request_dict)
        return request_list

    def update_request_status(accepted, offer_id, request_id):
        """updates request status for approval or rejection"""
        db.cursor.execute(
            """
            SELECT * FROM ride_requests
            WHERE offer_id = %s
            AND request_id = %s
            """,
            (offer_id, request_id)
        )
        request = db.cursor.fetchone()
        if not request:
            return {"message": "request does not exist"}
        db.cursor.execute(
            """
            UPDATE ride_requests
            SET request_accepted_reject = %s
            WHERE offer_id = %s
            AND request_id = %s
            """,
            (accepted, offer_id, request_id)
        )
        db.commit()
        return {"message": "Request updated successfully"}

