# import unittest
# import os
# import json
# from datetime import datetime, timedelta 
# from models import ride_models

# from Api import create_app
 
# class TestDriverRideOffer(unittest.TestCase):
#     def setUp(self):
#         """inititalize app and define variables"""
#         self.app = create_app(config_name = "testing")
#         # allows our test to mimic actual clients
#         self.app.config["TESTING"]=True
#         self.client = self.app.test_client()
#         # departure time 20 minutes from current time 
#         self.DTime = datetime.now() + timedelta(minutes=20)
    
#     def test_create_ride_offers(self):
#         """test driver can create ride offer"""
#         response =self.client.post(
#             "api/v1/user/create",
#             data=json.dumps(dict(
#                 RideId= "1",
#                 location = "Nanyuki",
#                 destination = "kisumu",
#                 departure = str(self.DTime.time()),
#                 driver_details = (dict(
#                     name = "kamau",
#                     car = "toyoya"
#                 ))
#             )),
#             content_type = "application/json"
#         )  

#         self.assertEqual(response.status_code,201) 
#     def test_input_field_empty(self):
#         """test ride offer fields are not empty"""
#         response = self.client.post(
#             "api/v1/user/create",
#             data = json.dumps(dict(
#                 RideId= "1",
#                 location = "",
#                 destination = "kisumu",
#                 departure = str(self.DTime.time()),
#                 driver_details = (dict(
#                     name = "kamau",
#                     car = "toyoya"
#             ))
#             )),
#             content_type = "aplication/json"
#         )
        
#         self.assertEqual(response.status_code,400)
#         pass
    
#     def test_input_field_string(self):
#         """test input fields are strings"""
#         response = self.client.post(
#             "api/v1/user/create",
#             data = json.dumps(dict(
#                 RideId= "1",
#                 location = "5",
#                 destination = "kisumu",
#                 departure = str(self.DTime.time()),
#                 driver_details = (dict(
#                     name = "kamau",
#                     car = "toyoya"
#             ))
#             )),
#             content_type = "aplication/json"
#         )
#         pass
    
#     def tearDown(self):
#         pass

