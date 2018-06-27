"""resources for rides """
import json
from flask_restful import Resource, Api
from flask import request
from marshmallow import Schema, fields
from models.ride_models import Rrequest, DriverOffer, ride_offers
from Api.schema_v import rideschema


# ride_offers = []
# where offers made by driver are stored
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
            return {errors}
        #create an instance of class RideOffer
        new_offer = DriverOffer(data["location"],
                                data["destination"],
                                # data["driver_details"]
                                )
        # save the new_offer to ride_offers[]
        ride = new_offer.save_ride_offer()
        # import pdb; pdb.set_trace()
        return ride, 201

    def get(self):
        """get ride by id"""
        return ride_offers, 200

                



class RideRequest(Resource):
    def get(self, id):
        """get ride by id"""
        for offer in ride_offers:
            if offer["ID"] == id:
                return offer,200
    
#     """passanger posts a ride request""" 
#     def post(self):
#         postRequest = request.get_json()
#         # validate using schema
#         data,errors = rideschema.load(postRequest)
#         if errors:
#             return {errors}

#         new_request = Rrequest(
#             data["location"],
#             data["destination"],
#             data["phone_number"]
#         )
#         A_request = new_request.save_request_ride()

#         # return A_request.update({
#         #     "url":"/api/v1/user/offer/"+postRequest.get("location")
#         # }),201

#     def get(self,location):
#         # passenger can get all ride offers within a particular location
#         list_of_offers = []
#         if len(ride_Offers)<1:
#             return {"message":"no offers made yet"}
#         for offer in ride_Offers:
#             if offer["location"] == location:
#                 list_of_offers.append(offer)
#             return {"list of offers":list_of_offers},200
    
# class MakeRequest(Resource):
#     def post (self):
#         make_request_post = request.get_json()
