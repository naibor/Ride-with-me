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
#     create_tables()
                
#     def test_get_ride_offers(self):
#         """test user can view all ride offers"""
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
#                 username = "kanjo",
#                 password = "A123456789a#"
#             )),
#             headers = {"content-type": "application/json"}
#         )
#         import pdb; pdb.set_trace()
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
#                          "Authorization":"driver_token"}
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
#             headers = {"content-type": "application/json",
#                           "Authorization":"token"}
#         )
#         self.assertEqual(signup.data.status_code,201)

#         # login a user
#         login = self.client.post(
#             "/api/v1/auth/login",
#             data = json.dumps(dict(
#                 username = "Visa",
#                 password = "A123456789a#"
#             )),
#             headers = {"content-type": "application/json"}
#         )
#         self.assertEqual(login.status_code,200)
#         login_data = json.loads(login.data.decode())
#         user_token = login_data["access_token"]

#     # get offers
#         response = self.client.get(
#             '/api/v1/users/rides',
#             headers = {"content-type": "application/json",
#                        "Authorization":"user_token"}
#         )
#         self.assertEqual(response.status_code,200 )

    # # get one offer
    # def test_get_one_offer(self):
    #     """tests user can get one ride offer"""
    #     response = self.client.get(
    #         "api/v1/users/rides/1",
    #         headers = {"content-type": "application/json",
    #                    "Authorization":"user_token"}
    #         ) 
    #     self.assertEqual(response.status_code,200)  

    # # make a request to join a ride offer
    # def test_request_to_join_offer(self):
    #     """test user can request to join ride offer"""
    #     request = self.client.post(
    #         "/api/v1/users/rides/1/requests",
    #         headers = {"content-type": "application/json",
    #                    "Authorization":"user_token"}
    #                 )
    #     drop_tables()
    #     self.assertEqual(request.status_code,201)
    #     self.assertEqual(create_data["message"],"Request to join ride has been processed")
    
    def tearDown(self):
        """Tears down test context"""
        self.app = None
        # db.cursor.execute("DROP TABLE IF EXISTS ride_requests;")
        # db.cursor.execute("DROP TABLE IF EXISTS ride_offers;")
        # db.cursor.execute("DROP TABLE IF EXISTS users;")
        
  
if __name__== '__main__':
    unittest.main()