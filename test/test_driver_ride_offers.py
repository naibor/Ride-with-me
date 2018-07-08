# """test for driver ride offer"""
# import unittest
# import os
# import json
# from datetime import datetime, timedelta 
# from models import ride_models
# from Api import create_app
# from test.test_base import TestBaseTest
# DTime = datetime.now() + timedelta(minutes=20)

# class TestDriverRideOffer(TestBaseTest):
#     """test driver can offer rides"""

#     def test_create_ride_offers(self):
#         """test driver can create ride offer"""
#      # register driver
#         register = self.client.post(
#             "/api/v1/auth/register",
#             data = json.dumps(dict(
#                 name = "kamau",
#                 username = "kanjo",
#                 phone_number = "0707981133",
#                 car = "True",
#                 password = "A123456789a#",
#                 confirmpassword = "A123456789a#",
#             )),
#             headers = {"content-type": "application/json"}
#         )
#         self.assertEqual(register.status_code,201)
#         # login driver
#         login = self.client.post(
#             "/api/v1/auth/login",
#             data = json.dumps(dict(
#                 username = "kanjo",
#                 password = "A123456789a#"
#             )),
#             headers = {"content-type": "application/json"}
#         )
#         self.assertEqual(login.status_code,201)
#         login_data = json.loads(login.data.decode())
#         token = login_data["access_token"]

#         # create offer
#         create = self.client.post(
#             "/api/v1/users/rides",
#             data = json.dumps(dict(
#                 RideId = "1",
#                 location = "Nanyuki",
#                 destination = "kisumu",
#                 departure = str(DTime.time())
#             )),
#             headers = {"content-type": "application/json",
#                        "Authorization":"token"}
#         )  
#         self.assertEqual(data.status_code,201) 

#          # get offers
#     def test_get_offers_made(self):
#         response = self.client.get(
#             '/api/v1/users/rides',
#             headers = {"content-type": "application/json"}
#         )
#         self.assertEqual(response.status_code,200 )

#     # get one offer
#     def test_get_one_offer(self):
#         """tests user can get one ride offer"""
#         response = self.client.get(
#             "api/v1/users/rides/1",
#             headers = {"content-type": "application/json"}
#             ) 
#         self.assertEqual(response.status_code,200)

#     # delete an offer
#     def test_get_one_offer(self):
#         """tests user can get one ride offer"""
#         response = self.client.delete(
#             "api/v1/users/rides/1",
#             headers = {"content-type": "application/json"}
#             ) 
#         self.assertEqual(response.status_code,200)
#         self.assertEqual(create_data["message"],"ride delete")  

# # test field validations

# #     def test_location_field_empty(self):
# #         """test ride offer fields are not empty"""
# #         response = self.client.post(
# #             "/api/v1/users/rides",
# #             data = json.dumps(dict(
# #                 RideId = "1",
# #                 location = "",
# #                 destination = "kisumu",
# #                 departure = str(DTime.time())
# #             )),
# #             headers = {"content-type": "application/json"}
# #         )  
# #         self.assertEqual(response.status_code,400)
        
# #     def test_destination_field_empty(self):
# #         """test destination field not empty"""
# #         response = self.client.post(
# #             "/api/v1/users/rides",
# #             data = json.dumps(dict(
# #                 RideId = "1",
# #                 location = "Naibor",
# #                 destination = "",
# #                 departure = str(DTime.time())
# #             )),
# #             headers = {"content-type": "application/json"}
# #         )
# #         self.assertEqual(response.status_code,400)
         
# #     def test_location_field_string(self):
# #         """test input fields are strings"""
# #         response = self.client.post(
# #             "/api/v1/users/rides",
# #             data = json.dumps(dict(
# #                 RideId = "1",
# #                 location = "5",
# #                 destination = "kisumu",
# #                 departure = str(DTime.time())
# #             )),
# #             headers = {"content-type": "application/json"}
# #         )
# #         self.assertEqual(response.status_code, 400)
    
# #     def test_destination_field_string(self):
# #         """test destiantion fields are strings"""
# #         response = self.client.post(
# #             "/api/v1/users/rides",
# #             data = json.dumps(dict(
# #                 RideId = "1",
# #                 location = "Nairobi",
# #                 destination = "10",
# #                 departure = str(DTime.time())
# #             )),
# #             headers = {"content-type": "application/json"}
# #         )
# #         self.assertEqual(response.status_code, 400)

# #     def test_location_field_with_space(self):
# #         """test location fields with spaces only"""
# #         response = self.client.post(
# #             "/api/v1/users/rides",
# #             data = json.dumps(dict(
# #                 RideId = "1",
# #                 location = "     ",
# #                 destination = "kisumu",
# #                 departure = str(DTime.time())
# #             )),
# #             headers = {"content-type": "application/json"}
# #         )
# #         self.assertEqual(response.status_code, 400)

# #     def test_destination_field_with_space(self):
# #         """test destination fields with spaces only"""
# #         response = self.client.post(
# #             "/api/v1/users/rides",
# #             data = json.dumps(dict(
# #                 RideId = "1",
# #                 location = "Nairobi",
# #                 destination = "     ",
# #                 departure = str(DTime.time())
# #             )),
# #             headers = {"content-type": "application/json"}
# #         )
# #         self.assertEqual(response.status_code, 400)

# #     def test_location_field_right_length(self):
# #         """test location field short """
# #         response = self.client.post(
# #             "/api/v1/users/rides",
# #             data = json.dumps(dict(
# #                 RideId = "1",
# #                 location = "Na",
# #                 destination = "kisumu",
# #                 departure = str(DTime.time())
# #             )),
# #             headers = {"content-type": "application/json"}
# #         )
# #         self.assertEqual(response.status_code, 400)

    