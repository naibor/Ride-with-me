"""resources for rides """
import json
from flask_restful import Resource, Api
from flask import request
from Api.User import login_required
from marshmallow import Schema, fields
from models.ride_models import Rrequest, DriverOffer
from Api.schema_v import rideschema, requeststatus


class RideOffer(Resource):  
    """Drivers resource class"""
    @login_required
    def post(this_user,self):
        """
        create a ride offer
        ---
        tags:
            - Ride offers
        description: Drivers make Rides offers
        security:
            - access_token: []
        schema:
        $ref: '#/definitions/Ride_Offer'
        responses:
            201:
                description: all ride offers
            403:
                description: Regular users cannot offer rides
            400:
                description: Bad request
        """
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
        """
        view all ride offers
        ---
        tags:
            - Ride offers
        description: Rides offers made by drivers
        security:
            - access_token: []
        schema:
            $ref: '#/definitions/Ride_Offer'
        responses:
            200:
                description: all ride offers
            404:
                description: no ride offers yet, sorry
        """
        return DriverOffer.get_all()


class RideRequest(Resource):
    """get ride requests by id"""
    @login_required
    def get(this_user, self, id):
        """
        View a ride offer
        ---
        tags:
            - Ride offer
        description: A single rides offer
        security:
            - access_token: []
        schema:
            $ref: '#/definitions/Ride_request'
        responses:
            200:
                description: a single ride offers
            400:
                description: invalid offer id
            200:
                description: ride offer
        """
        response = DriverOffer.ride_by_id(id)
        if isinstance(response, str):
            return response, 400
        return response,200

    @login_required
    def delete(this_user, self, id):
        """
        delete ride offer
        ---
        tags:
            - Ride offer
        security:
            - Access_token: []
        schema:
            $ref: '#/definitions/Ride_Offer'
        responses:
            200:
                description: ride deleted
        
        """
        return DriverOffer.delete_ride_offer(id), 200

       
class SpecificRequest(Resource):
    """Post a request to a specific ride id"""
    @login_required
    def post(this_user, self, id):
        """
        request to join a ride 
        ---
        tags:
            - Requests
        security:
            - Access_token: []
        schema:
            $ref: '#/definitions/Ride_request'
        responses:
            201:
                description: Request to join ride has been processed
            400:
                description: bad request

        """
        postRequest = request.get_json()
        new_request = Rrequest(
            this_user[0],
            id
        )
        user_request = new_request.save_request_ride()
        return {"message":"Request to join ride has been processed"}, 201

    @login_required
    def get(this_user, self, id):
        """
        View all requests for a ride offer
        ---
        tags:
            - Ride request
        description: ride requests to a ride offer
        security:
            - access_token: []
         schema:
        $ref: '#/definitions/User_login'
        responses:
            200:
                description: ride requests for a particular offer
                schema:
                    user details:
                    ride id:
            400:
                description: no ride requests to this offer
            200:
                description: a list of ride requests
            
            """
        response = Rrequest.get_requests_for_offer(id)
        return response,201

class AcceptRejectRequest(Resource):
    @login_required
    def put(this_user, self, offer_id, request_id):
        """
        Update ride request
        ---
        tags:
            - Request
        description: Update the status of a ride request
        security:
            - Access_token: []
        parameters:
            - name: ride_status
              in: path
              type: Boolean
              description: Status of ride to update
            - name: ride
              in: body
            
        schema:
            $ref: '#/definitions/User_login'
    
        responses:
            200:
                description: Request updated successfully
            401:
                description: Regular users cannot accept or reject ride requests
            400:
                description: Bad request
        """
        if not this_user[3]:
            return {"message": "Regular users cannot accept or reject ride requests"}, 403 
        update_request = request.get_json()
        data, errors = requeststatus.load(update_request)
        if errors:
            return (errors),400
        response = Rrequest.update_request_status(data.get("status"), offer_id, request_id)
        if response["message"] == "request does not exist":
            return response, 400
        return response, 200
