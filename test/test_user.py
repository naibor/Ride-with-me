"""test user signup and login"""
import unittest  
import os
import json
from Api import User
from Api import create_app
from test.test_base import TestBaseTest

class TestUserSignUp(TestBaseTest):
    """class for user sign up test case"""
#     def setUp(self):
#         """initialize app and define variables"""
#         self.app = create_app(config_name = "testing")
#         self.app.config["TESTING"]=True
#         self.client = self.app.test_client()

    # def test_user_sign_up(self):
    #     """test user can successfuly sign up"""
    #     response = self.client.post(
    #         "/api/v1/auth/signup",
    #         data = json.dumps(dict(
    #             name = "Naibor",
    #             username = "tisa",
    #             phone_number = "0707900000",
    #             password = "A123456789a#",
    #             confirmpassword = "A123456789a#"
    #         )),
    #         headers = {"content-type": "application/json"}
    #     )
    #     self.assertEqual(response.status_code,201)
    #     response_data = json.loads(response.data.decode())
    #     self.assertEqual(response_data["message"],"successfully signed up")
    
    # def test_user_login(self):
    #     """test user can successfuly login"""
    #     sign_up = self.client.post(
    #         "api/v1/auth/signup",
    #         data = json.dumps(dict(
    #             username = "Lisa",
    #             password = "A123456789a#"
               
    #         )),
    #         headers = {"content-type": "application/json"}
    #     )
    #     login = self.client.post(
    #         "/api/v1/auth/login",
    #         data = json.dumps(dict(
    #             username = "Lisa",
    #             password = "A123456789a#"
    #         )),
    #         headers = {"content-type": "application/json"}
    #     )
    #     self.assertEqual(sign_up.status_code,201)
    #     response = json.loads(login.data.decode())


if __name__== '__main__':
    unittest.main()