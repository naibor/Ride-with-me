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
        

#     def test_post_ride_request(self):
#         """test usesr can create ride request """
#         response = self.client.post(
#             "api/v1/user/request",
#             data=json.dumps(dict
#                     (location="Nairobi",
#                     destination="Kisumu"
#                     )),
#                     content_type = "application/json"
#                     )
#         self.assertEqual(response.status_code,201)
    
#     def tearDown(self):
#         pass