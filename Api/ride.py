"""resources for rides """
import json
from flask_restful import Resource, Api
from flask import request
from marshmallow import Schema, fields
from models.ride_models import Rrequest, DriverOffer, ride_offers
from Api.schema_v import rideschema, requestschema

request_details = {}
# where passenger request details is stored
ride_Requests = []
# where passanger ride requests details is stored

class RideOffer(Resource):  
    """Drivers resource class"""
    def post(self):
        """driver post ride offer"""
        postoffer = request.get_json()
        # validate it
        data, errors = rideschema.load(postoffer)
        if errors:
            return (errors),400
        #create an instance of class RideOffer
        new_offer = DriverOffer(data["location"],
                                data["destination"],
                                # data["driver_details"]
                                )
        # save the new_offer to ride_offers[]
        ride = new_offer.save_ride_offer()
        return (ride), 201

    def get(self):
        """get all rides"""
        return (ride_offers), 200

    
class RideRequest(Resource):
    """get ride requests by id"""
    def get(self, id):
        """get ride by id"""
        for offer in ride_offers:
            if offer["ID"] == id:
                return (offer,
                # {"url":"/api/v1/users/rides/<ride_id>/requests"}
                ),200

class SpecificRequest(Resource):
    """Post a request to a specific ride id"""
    def post(self,id):
        """passanger posts a ride request""" 
        postRequest = request.get_json()
        data,errors = requestschema.load(postRequest)
        # import pdb; pdb.set_trace()
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

