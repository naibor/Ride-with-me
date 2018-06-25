import json
from flask_restful import Resource, Api
from flask import request
from marshmallow import Schema, fields
# from User import driver_details
from Api.schema_v import rideschema
from models.ride_models import Rrequest, DriverOffer

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
        # validate using schema
        data,errors =rideschema.load(postRequest)
        if errors:
            return{"error":errors} 
        location = request_data.get("location")
        destination = request_data.get("destination")
        
        #an instance of class RideRequest
        new_request = Rrequest(location,destination)
        
        #request_details{} containing the ride requests of a user  
        request_details[request_data.get("location")]={
                                "location":request_data.get("location"),
                                "destination":request_data.get("destination")
                              }
        # save the new request to ride_request[]
        ride_Requests.append(request_details)

        return {"message":"Ride is being processed",
                "url":"/api/v1/user/offer/"+postRequest.get("location")},201

    def get(self,location):
        # passenger can get all ride offers within a particular location
        list_of_offers=[]
        if len(ride_Offers)<1:
            return {"message":"no offers made yet"}
        for offer in ride_Offers:
            if offer["location"] == location:
                list_of_offers.append(offer)
        return {"list of offers":list_of_offers},200
    
class DriverRideOffer(Resource):  
    def post(self):
        #driver post ride offer data
        postoffer = request.get_json()
        data,errors = rideschema.load(postoffer)
        if errors:
            return{'error':errors}
        #create an instance of class RideOffer

        new_offer = DriverOffer(postoffer.get("location"),
                                postoffer.get("destination")
                                )
        DT=json.dumps(new_offer.departure)        
                # save the new_offer to ride_offers[]

        ride_Offers.append({"id":new_offer.ride_id,
                            "location":new_offer.location,
                            "destination":new_offer.destination,
                            "departure":DT,
                            "driver details":new_offer.driver_detail
        })
        # import pdb;pdb.set_trace()
        return{"message":"you have created a ride offer"},201

    def get(self):
        # driver gets a list of ride requests made
        return{"ride requests":ride_Requests},200

        
class RideOffer(Resource):
    def get(self,id):
        # passanger can get specific ride offer
        for offer in ride_Offers:
            # ie every dict in the dictionary
            if id == offer["id"]:
                # if the id is a key in the dictionary
                return offer
        return{"message":"ride does not exist"}

