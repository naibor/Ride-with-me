"""resources for rides """
import json
from flask_restful import Resource, Api
from flask import request
from marshmallow import Schema, fields
from models.ride_models import Rrequest, DriverOffer, ride_offers
from Api.schema_v import rideschema, requestschema

request_details = {}
# passenger request details stored
ride_Requests = []
# passanger ride requests details stored

class RideOffer(Resource):  
    """Drivers resource class"""
    def post(self):
        postoffer = request.get_json()
        data, errors = rideschema.load(postoffer)
        if errors:
            return (errors),400

        new_offer = DriverOffer(data["location"],
                                data["destination"]
                                )
        
        # ride = new_offer.save_ride_offer()
        # return (ride), 201
        return new_offer.save_ride_offer()

    def get(self):
        """get all rides"""
        # SELECT * FROM ride_offer
        return DriverOffer.get_all(), 200

    
class RideRequest(Resource):
    """get ride requests by id"""
    def get(self, id):
        """get ride by id"""
        for offer in ride_offers:
            if offer["ID"] == id:
                return (offer),200

class SpecificRequest(Resource):
    """Post a request to a specific ride id"""
    def post(self,id):
        postRequest = request.get_json()
        data,errors = requestschema.load(postRequest)
        if errors:
            return (errors),400
        for ride in ride_offers:
            if ride["ID"] == id:
                new_request = Rrequest(
                    data["location"],
                    data["destination"],
                    data["phone_number"]
                    )
                A_request = new_request.save_request_ride()
                return {"message":"You have successfully requested to join. Driver will call"}, 201
        return{"message":"Requested ride does not exist"}, 401

