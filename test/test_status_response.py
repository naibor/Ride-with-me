# """test for driver ride offer"""
# import unittest
# import os
# import json
# from datetime import datetime, timedelta 
# from models import ride_models
# from Api import create_app
# from test.test_base import TestBaseTest
# DTime = datetime.now() + timedelta(minutes=20)

# class TestDriverResponse(TestBaseTest):
#     """test driver can offer rides"""

#     def test_driver_response_to_ride_request(self):
#         """test driver can create ride offer"""
#     # register driver
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

#     # login driver
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

#     # create offer
#         create = self.client.post(
#             "/api/v1/users/rides",
#             data = json.dumps(dict(
#                 RideId = "1",
#                 location = "Nanyuki",
#                 destination = "kisumu",
#                 departure = str(DTime.time())
#             )),
#             headers = {"content-type": "application/json",
#                         "Authorization":"token"}
#         )  
#         self.assertEqual(response.status_code,201) 

#     # user login
#         login = self.client.post(
#             "/api/v1/auth/login",
#             data = json.dumps(dict(
#                 username = "Visa",
#                 password = "A123456789a#"
#             )),
#             headers = {"content-type": "application/json"}
#         )
#        self.assertEqual(login.status_code,201)
#        login_data = json.loads(login.data.decode())
#        token = login_data["access_token"]

#     # get one offer
#         response = self.client.get(
#             "api/v1/users/rides/1",
#             headers = {"content-type": "application/json"
#                        "Authorization":"token" }
#             ) 
#         self.assertEqual(response.status_code,200) 

#     # make request to an offer
#         request = self.client.post(
#             "/api/v1/users/rides/1/requests",
#             headers = {"content-type": "application/json",
#                       "Authorization":"token"}
#                     )
#         self.assertEqual(request.status_code,201)
  
#     # driver respond to ride request 
#         response = self.client.put(
#             "/api/v1/users/rides/1/requests/1",
#             data = json.dumps(dict(
#                 status = "True"
#             )),
#             headers = {"content-type": "application/json",
#                           "Authorization":"token"}
#         )
#         self.assertEqual(request.status_code,201)
#         self.assertEqual(create_data["message"],"Request updated successfully")

#     #validate response made by drive
#     def test_response_is_bool(self):
#         response = self.client.put(
#             "/api/v1/users/rides/1/requests/1",
#             data = json.dumps(dict(
#                 status = "12345"
#             )),
#             headers = {"content-type": "application/json",
#                          "Authorization":"token"}
#         )
#         self.assertEqual(response.status_code,400)
                


