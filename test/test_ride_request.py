# import unittest
# import os
# import json

# from models import ride_models
# from Api import create_app

# class TestRideRequest(unittest.TestCase):
#     def setUp(self):
#         """initialize app and define variables"""
#         self.app = create_app(config_name="testing")
#         self.app.config["TESTING"]=True
#         self.client = self.app.test_client()
#         self.request  = self.client.post(
#             "api/v1/user/signup",
#             data=json.dumps(dict(
#                 "Nairobi"(dict(location="Nairobi",
#                            destination="Kisumu"
#                         ))
#                     )),content_type = "application/json"
#                     )

#     def test_post_ride_request(self):
#         """test usesr can create ride request """
#         self.assertEqual(response.status_code,200)
    
#     def tearDown(self):
#         pass