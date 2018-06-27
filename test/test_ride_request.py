# """test ride requests"""
# import unittest
# import os
# import json
# from models import ride_models
# from Api import create_app

# class TestRideRequest(unittest.TestCase):
#     """class test ride requests"""
#     def setUp(self):
#         """initialize app and define variables"""
#         self.app = create_app(config_name="testing")
#         self.app.config["TESTING"]=True
#         self.client = self.app.test_client()

#     def test_post_ride_request(self):
#         """test user can create ride request """
#         response = self.client.post(
#             "api/v1/users/rides/id/requests",
#             data = json.dumps(dict
#                     (location = "Nairobi",
#                     destination = "Kisumu"
#                     )),
#                     headers = {"content-type": "application/json"}
#                     )
#         self.assertEqual(response.status_code,201)
    
#     def test_location_not_empty(self):
#         """Test field location not empty"""
#         response = self.client.post(
#             "api/v1/users/rides/id/requests",
#             data = json.dumps(dict
#                     (location = "",
#                     destination = "Kisumu"
#                     )),
#                     headers = {"content-type": "application/json"}
#                     )
#         self.assertEqual(response.status_code,400)

    # def test_destination_not_empty(self):
    #     """Test field destination not empty"""
    #     response = self.client.post(
    #         "/api/v1/users/rides/id/requests",
    #         data=json.dumps(dict
    #                 (location ="Nairobi",
    #                 destination =""
    #                 )),
    #                 headers = {"content-type": "application/json"}
    #                 )
    #     self.assertEqual(response.status_code,400)

    # def test_request_location_no_space_only(self):
    #     """test user enters no spaces in place of location"""
    #     response = self.client.post(
    #         "/api/v1/users/rides/id/requests",
    #         data = json.dumps(dict
    #                 (location = "      ",
    #                 destination = "Kisumu"
    #                 )),
    #                 headers = {"content-type": "application/json"}
    #                 )
    #     self.assertEqual(response.status_code,400)
        
    # def test_request_destination_no_space_only(self):
    #     """test user enters no spaces in place of destination"""
    #     response = self.client.post(
    #         "/api/v1/users/rides/id/requests",
    #         data = json.dumps(dict
    #                 (location = "Nairobi",
    #                 destination = "      "
    #                 )),
    #                 headers = {"content-type": "application/json"}
    #                 )
    #     self.assertEqual(response.status_code,400)