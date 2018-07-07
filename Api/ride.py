"""resources for rides """
import json
from flask_restful import Resource, Api
from flask import request
from Api.User import login_required
from marshmallow import Schema, fields
from models.ride_models import Rrequest, DriverOffer
from Api.schema_v import rideschema


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
        # import pdb; pdb.set_trace()
        """get all rides"""
        return DriverOffer.get_all(), 200

    

    
class RideRequest(Resource):
    """get ride requests by id"""
    @login_required
    def get(this_user, self, id):
        """get ride by id"""
        response = DriverOffer.ride_by_id(id)
        if isinstance(response, str):
            return response, 400
        return response

    @login_required
    def delete(this_user, self, id):
        """deletes ride offer"""
        return DriverOffer.delete_ride_offer(id), 200

       
class SpecificRequest(Resource):
    """Post a request to a specific ride id"""
    @login_required
    def post(this_user, self, id):
        postRequest = request.get_json()
        new_request = Rrequest(
            this_user[0],
            id
        )
        user_request = new_request.save_request_ride()
        return {"message":"Request to join ride has been processed"}, 201

    @login_required
    def get(this_user, self, id):
        """user can get all requests"""
        response = Rrequest.get_requests_for_offer(id)
        return response

class AcceptRejectRequest(Resource):
    @login_required
    def put(this_user, self, offer_id, request_id):
        if not this_user[3]:
            return {"message": "Regular users cannot accept or reject ride requests"}, 403 
        update_request = request.get_json()
        response = Rrequest.update_request_status(update_request.get("status"), offer_id, request_id)
        if response["message"] == "request does not exist":
            return response, 400
        return response
