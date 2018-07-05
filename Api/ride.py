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
        if not this_user[3]:
            return {"message": "Regular users cannot offer rides"}, 403
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
        return ride, 201

    @login_required
    def get(this_user, self):
        """get all rides"""
        return DriverOffer.get_all(), 200

    
class RideRequest(Resource):
    """get ride requests by id"""
    @login_required
    def get(this_user, self,id):
        """get ride by id"""
        return DriverOffer.ride_by_id(id)
        

       
class SpecificRequest(Resource):
    """Post a request to a specific ride id"""
    @login_required
    # import pdb; pdb.set_trace()
    def post(this_user, self, id):
        postRequest = request.get_json()
        data,errors = requestschema.load(postRequest)
        if errors:
            return (errors),400
        new_request = Rrequest(
            this_user[0],
            data["phone_number"],id
            )
        
        user_request = new_request.save_request_ride()
        return {"message":"Request to join ride has been processed"}, 201

    def get(self):
        """user can get all requests"""
        response = Rrequest.get_requests_for_offer()
        return response
        import pdb; pdb.set_trace()



