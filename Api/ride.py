"""resources for rides """
import json
from flask_restful import Resource, Api
from flask import request
from Api.User import login_required
from marshmallow import Schema, fields
from models.ride_models import Rrequest, DriverOffer
from Api.schema_v import rideschema, requestschema


class RideOffer(Resource):  
    """Drivers resource class"""
    @login_required
    def post(this_user, self):
        print(this_user)
        postoffer = request.get_json()
        data, errors = rideschema.load(postoffer)
        if errors:
            return (errors),400

        new_offer = DriverOffer(
            this_user[0],
            data["location"],
            data["destination"]
        )
        
        rides = new_offer.save_ride_offer()
        return (rides), 201


    def get(self):
        """get all rides"""
        return DriverOffer.get_all(), 200

    
class RideRequest(Resource):
    """get ride requests by id"""
    @login_required
    def get(this_user, self, id):
        """get ride by id"""
        for offer in ride_offers:
            if offer["ID"] == id:
                return (offer),200

class SpecificRequest(Resource):
    """Post a request to a specific ride id"""
    @login_required
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

