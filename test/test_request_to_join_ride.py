# """test ride offers as a user"""
# """test user can make a request to join a ride"""
# import unittest
# import os
# import json
# from datetime import datetime, timedelta 
# from models.ride_models import Rrequest, DriverOffer
# from test.test_base import BaseTestCase, create_tables,drop_tables
# from models.db import db
# DTime = datetime.now() + timedelta(minutes=20)

# class TestRideOffer(BaseTestCase):
#     """test ride offers"""
                
#     def test_request_to_join_offer(self):
#         """test user can request to join ride offer"""
#         create_tables()
#         # register driver
#         register = self.client.post(
#             "/api/v1/auth/register",
#             data = json.dumps(dict(
#                 name = "kamau",
#                 username = "kanjoo",
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
#                 username = "kanjoo",
#                 password = "A123456789a#"
#             )),
#             headers = {"content-type": "application/json"}
#         )
#         self.assertEqual(login.status_code,200)
#         login_data = json.loads(login.data.decode())
#         driver_token = login_data['access_token']

#         # create offers
#         create = self.client.post(
#             "/api/v1/users/rides",
#             data = json.dumps(dict(
#                 RideId = "1",
#                 location = "Nanyuki",
#                 destination = "kisumu",
#                 departure = str(DTime.time())
#             )),
#             headers = {"content-type": "application/json",
#                          "Authorization":driver_token}
#         )  
#         self.assertEqual(create.status_code,201) 
#         create_data = json.loads(create.data.decode())
#         self.assertEqual(create_data["message"],"Successfully created a ride offer")
       
#         # signup a user
#         signup = self.client.post(
#             "/api/v1/auth/signup",
#             data = json.dumps(dict(
#                 name = "Naibor",
#                 username = "Visa",
#                 phone_number = "0707900000",
#                 password = "A123456789a#",
#                 confirmpassword = "A123456789a#"
#             )),
#             headers = {"content-type": "application/json"}
#         )
#         self.assertEqual(signup.status_code,201)

#         # login a user
#         user_login = self.client.post(
#             "/api/v1/auth/login",
#             data = json.dumps(dict(
#                 username = "Visa",
#                 password = "A123456789a#"
#             )),
#             headers = {"content-type": "application/json"}
#         )
#         self.assertEqual(user_login.status_code,200)
#         user_login_data = json.loads(user_login.data.decode())
#         token = user_login_data['access_token']
        
#         #user get one ride
#         response = self.client.get(
#             "api/v1/users/rides/1",
#             headers = {"content-type": "application/json",
#                        "Authorization":token}
#             ) 
#         self.assertEqual(response.status_code,200)   
        
    
#     #    make a request to join a ride offer
#         request = self.client.post(
#             "/api/v1/users/rides/1/requests",
#             headers = {"content-type": "application/json",
#                        "Authorization":token}
#                     )
#         import pdb; pdb.set_trace()
#         self.assertEqual(request.status_code,201)
#         self.assertEqual(create_data["message"],"Request to join ride has been processed")
        
#     def tearDown(self):
#         """Tears down test context"""
#         self.app = None        
#         drop_tables()

      
# if __name__== '__main__':
#     unittest.main()
        