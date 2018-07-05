# """test ride offers"""
# import unittest
# import os
# import json
# from datetime import datetime, timedelta 
# from models.ride_models import Rrequest, DriverOffer
# from Api import create_app
 
# class TestRideOffer(unittest.TestCase):
#     """test ride offers"""
#     def setUp(self):
#         """inititalize app and define variables"""
#         self.app = create_app(config_name = "testing")
#         self.app.config["TESTING"]=True
#         self.client = self.app.test_client()
#         self.DTime = datetime.now() + timedelta(minutes=20)
                
#     def test_get_ride_offers(self):
#         """test user can view all ride offers"""
#         create = self.client.post(
#             "/api/v1/users/rides",
#             data = json.dumps(dict(
#                 RideId = "1",
#                 location = "Nanyuki",
#                 destination = "kisumu",
#                 departure = str(self.DTime.time())
#             )),
#             headers = {"content-type": "application/json"}
#         )  

#         self.assertEqual(create.status_code,201) 
#         response = self.client.get(
#             '/api/v1/users/rides',
#             headers = {"content-type": "application/json"}
#         )
#         self.assertEqual(response.status_code,200 )

#     def test_empty_offer_location(self):
#         """tests user inputs location and destination"""
#         response = self.client.post(
#             "api/v1/users/rides",
#             data = json.dumps(dict(
#                 RideId = "1",
#                 location = "",
#                 destination = "kisumu",
#                 departure = str(self.DTime.time())
#             )),
#             headers = {"content-type": "application/json"}
#             ) 
#         self.assertEqual(response.status_code,400)  
        
#     def test_empty_offers_destination(self):
#         """test user can view all ride offers"""
#         response = self.client.post(
#             "api/v1/users/rides",
#             data = json.dumps(dict(
#                 RideId = "1",
#                 location = "Nanyuki",
#                 destination = "",
#                 departure = str(self.DTime.time())
#             )),
#             headers = {"content-type": "application/json"}
#         )  
#         self.assertEqual(response.status_code,400) 

#     def tests_spaces_only_offer_location(self):
#         """tests user inputs valid characters only"""
#         response = self.client.post(
#             "api/v1/users/rides",
#             data = json.dumps(dict(
#                 RideId = "1",
#                 location = "   ",
#                 destination = "kisumu",
#                 departure = str(self.DTime.time())
#             )),
#             headers = {"content-type": "application/json"}
#         ) 
#         self.assertEqual(response.status_code,400)  