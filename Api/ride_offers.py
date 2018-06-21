from flask_restful import Resource, Api
from flask import request
from models.ride_models import RRequest,DriverOffer


ride_Offers = []
# where offers made by driver are stored
request_details = {}
# where passenger request details is stored
ride_Requests =[]
# where passanger ride requests details is stored
class RideRequest(Resource):
    # passanger posts a ride request
    def post(self):
        postRequest = request.get_json()
        # validate
        # empty field
        if not postRequest.get("location"):
            return {"message":"enter your location"},400
        if not postRequest.get("destination"):
            return{"message":"enter your destination"},400

        # empty string
        if  postRequest.get("location") == "  ":
            return {"message":"location can not be spaces"},400
        if postRequest.get("destination") == "  ":
            return{"message":"destination can not be spaces"},400

        location = postRequest.get("location")
        destination = postRequest.get("destination")
        
        #an instance of class RideRequest
        new_request = RRequest(location,destination)
        # import pdb;pdb.set_trace()
        
        #request_details{} containing the ride requests of a user  
        request_details[postRequest.get("location")]={
                                "location":postRequest.get("location"),
                                "destination":postRequest.get("destination")
                              }
        # save the new request to ride_request[]
        ride_Requests.append(request_details)

        return {"message":"Ride is being processed",
                "url":"/api/v1/user/offer/"+postRequest.get("location")},200
    
class DriverRideOffer(Resource):  
    def post(self):
        #driver post ride offer data
        postoffer = request.get_json()
        # validate it
        # empty field 
        if not postoffer.get("location"):
            return{"message":"enter your location please"},400
        if not postoffer.get("destination"):
            return{"message":"enter ride destination please"},400
        
        # space in input
        if postoffer.get("location")==" ":
            return {"message":"spaces not allowed"},400
        if postoffer.get("destination") == " ":
            return {"message":"spaces not allowed"},400
        
        #create an instance of class RideOffer
        new_offer = DriverOffer(postoffer.get("location"),
                                postoffer.get("destination")
                                )

        # save the new_offer to ride_offers[]
        ride_Offers.append({"id":new_offer.ride_id,
                            "location":new_offer.location,
                            "destination":new_offer.destination,
                            "departure":new_offer.departure
        })
        return{"message":"you have created a ride offer"}
class RideOffer(Resource):
    def get(self,id):
        # passanger can get specific ride offer
        for offer in ride_Offers:
            # ie every dict in the dictionary
            if id == offer["id"]:
                # if the id is a key in the dictionary
                return offer
        return{"message":"ride does not exist"}

    def get(self,location):
        # passenger can get all ride offers within a particular location
        list_of_offers=[]
        if len(ride_Offers)<1:
            return {"message":"no offers made yet"}
        for offer in ride_Offers:
            if offer["location"] == location:
                list_of_offers.append(offer)
        return list_of_offers