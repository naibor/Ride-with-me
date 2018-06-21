# import unittest
# import os
# import json
# from datetime import datetime, timedelta 
# from models import ride_models

# from Api import create_app
 
# class TestRideOffers(unittest.TestCase):
#     def setUp(self):
#         """inititalize app and define variables"""
#         self.app = create_app(config_name = "testing")
#         # allows our test to mimic actual clients
#         self.app.config["TESTING"]=True
#         self.client = self.app.test_client()
#         # departure time 20 minutes from current time 
#         DTime = datetime.now() + timedelta(minutes=20)
#         self.sign_up =self.client.post(
#             "api/v1/users",
#             data=json.dumps(dict(
#                 RideId= "1",
#                 location = "Nanyuki",
#                 destination = "kisumu",
#                 departure = str(DTime.time()),
#                 driver_details = (dict(
#                     name = "kamau",
#                     car = "toyoya"
#                 ))
#             )),
#             content_type = "application/json"
#         )  
#     def test_create_ride_offers(self):
#         """test driver can create ride offer"""
#         self.assertEqual(response.status_code,201) 
        
#     def test_get_ride_offers(self):
#         """test user can view all ride offers"""
#         response = self.client.get("api/v1/ride",content_type = "application/json")
#         self.assertEqual(response.status_code,200 )

#     def tearDown(self):
#         pass

