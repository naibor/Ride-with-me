# """test user signup and login"""
# import unittest  
# import os
# import json
# from Api import User
# from Api import create_app
# from test.test_base import TestBaseTest
# from test.test_database import db

# # db.cursor.execute("DROP TABLE IF EXISTS " + users + ";")

# class TestUserSignUp(TestBaseTest):
#     """class for user sign up test case"""

#     def test_user_sign_up(self):
#         """test user can successfuly sign up"""
#         response = self.client.post(
#          "/api/v1/auth/signup",
#             data = json.dumps(dict(
#                 name = "Naibor",
#                 username = "Lisa",
#                 phone_number = "0707900000",
#                 password = "A123456789a#",
#                 confirmpassword = "A123456789a#"
#             )),
#             headers = {"content-type": "application/json"}
#     )
#         self.assertEqual(response.status_code,201)
#         response_data = json.loads(response.data.decode())
#         self.assertEqual(response_data["message"],"successfully signed up")
    
#     def test_user_login(self):
#         """test user can successfuly login"""
#         # sign up user
#         sign_up = self.client.post(
#             "api/v1/auth/signup",
#             data = json.dumps(dict(
#                 name = "Naibor",
#                 username = "Visa",
#                 phone_number = "0707900000",
#                 password = "A123456789a#",
#                 confirmpassword = "A123456789a#"
#             )),
#             headers = {"content-type": "application/json"}
#         )
#         self.assertEqual(sign_up.status_code,201)
#         # login user
#         login = self.client.post(
#             "/api/v1/auth/login",
#             data = json.dumps(dict(
#                 username = "Visa",
#                 password = "A123456789a#"
#             )),
#             headers = {"content-type": "application/json"}
#         )
#         self.assertEqual(login.status_code,201)
#         login_data = json.loads(login.data.decode())
#         self.assertEqual(login_data["message"],"login successful")

#     def test_driver_login(self):
#         """test driver can successfuly login"""
#         # register a driver
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
#         register_data = json.loads(register.data.decode())
#         self.assertEqual(register_data["message"],"successfully signup as a driver")
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
#         self.assertEqual(login_data["message"],"login successful ")
    
# if __name__== '__main__':
#     unittest.main()