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
    def post(this_user,self):
        postoffer = request.get_json()	
        data, errors = rideschema.load(postoffer)
        if errors:
            return (errors),400
        new_offer = DriverOffer(
            this_user[0],
            data['location'],
            data["destination"]
    )
        ride = new_offer.save_ride_offer()
        return ride

    def get(self):
        """get all rides"""
        return DriverOffer.get_all(), 200

    
class RideRequest(Resource):
    """get ride requests by id"""
    def get(self,id):
        """get ride by id"""
        return DriverOffer.ride_by_id(id)
        

       
class SpecificRequest(Resource):
    """Post a request to a specific ride id"""
    # @login_required
    def post(self,id):
        postRequest = request.get_json()
        data,errors = requestschema.load(postRequest)
        if errors:
            return (errors),400
        new_request = Rrequest(
            # offer_id
            # this_user[0],
            data["location"],
            data["destination"],
            data["phone_number"]
        )
        import pdb; pdb.set_trace()
        user_request = new_request.save_request_ride()

        # for ride in ride_offers:
        #     if ride["ID"] == id:
        #         new_request = Rrequest(
        #             data["location"],
        #             data["destination"],
        #             data["phone_number"]
        #             )
        #         A_request = new_request.save_request_ride()
        #         return {"message":"You have successfully requested to join. Driver will call"}, 201
        # return{"message":"Requested ride does not exist"}, 401

