
# import unittest  
# import os
# import json
# # from flask import Flask
# from Api import User
# from Api import create_app

# class TestUserSignUp(unittest.TestCase):
#     """class for user sign up test case"""
#     def setUp(self):
#         """initialize app and define variables"""
#         self.app = create_app(config_name = "testing")
#         # self.app = Flask(__name__)
#         # or the below whenyou are not using create_app funtion
#         self.app.config["TESTING"]=True
#         # a flask environmnet variable 
#         self.client = self.app.test_client()


#         # sign up a user
#     def test_user_sign_up(self):
#         """test user can successfuly sign up"""
#         response =self.client.post(
#             "api/v1/user/signup",
#             data=json.dumps(dict(
#                 name="Naibor",
#                 username="Lisa",
#                 password="12345",
#                 confirmpassword="12345"
#             )),
#             content_type=("application/json")
#         )
#         # assert response code is 201
#         self.assertEqual(response.status_code,201)
#         # deserialize response data
#         response_data = json.loads(response.data.decode())

#         self.assertEqual(response_data["message"],"Welcome you have successfully signed up")
    
#     def test_user_login(self):
#         """test user can successfuly login"""
#         signup =self.sign_up =self.client.post(
#             "api/v1/user/signup",
#             data=json.dumps(dict(
#                 name='Naib',
#                 username='Lis',
#                 password='12345',
#                 confirmpassword='12345'
#             )),
#             content_type=("application/json")
#         )

#         login = self.client.post(
#             "api/v1/user/auth",
#             data = json.dumps(dict(
#                 username = "Lis",
#                 password = "12345"
#             )),
#             content_type = "application/json"
#         )
#         # self.assertEqual(response.)
#         self.assertEqual(login.status_code,200)
#         response = json.loads(login.data.decode())
#         self.assertEqual(response["message"],"successfully logged in")


#     def tearDown(self):
#         pass

