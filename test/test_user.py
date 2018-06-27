"""test user signup and login"""
import unittest  
import os
import json
from Api import User
from Api import create_app

class TestUserSignUp(unittest.TestCase):
    """class for user sign up test case"""
    def setUp(self):
        """initialize app and define variables"""
        self.app = create_app(config_name = "testing")
        # or the below whenyou are not using create_app funtion
        self.app.config["TESTING"]=True
        # a flask environmnet variable 
        self.client = self.app.test_client()

        # sign up a user
    def test_user_sign_up(self):
        """test user can successfuly sign up"""
        response = self.client.post(
            "/api/v1/auth/signup",
            data = json.dumps(dict(
                name = "Naibor",
                username = "Lisa",
                password = "A123456789a#",
                confirmpassword = "A123456789a#"
            )),
            headers = {"content-type": "application/json"}
        )
        # assert response code is 201
        self.assertEqual(response.status_code,201)
        # deserialize response data
        response_data = json.loads(response.data.decode())

        self.assertEqual(response_data["message"],"successfully signed up")
    
    def test_user_login(self):
        """test user can successfuly login"""
        sign_up = self.client.post(
            "api/v1/auth/signup",
            data = json.dumps(dict(
                name = 'Melvin',
                username = 'Atis',
                password = 'A123456789a#',
                confirmpassword = 'A123456789a#'
            )),
            headers = {"content-type": "application/json"}
        )
        login = self.client.post(
            "/api/v1/auth/login",
            data = json.dumps(dict(
                username = "Atis",
                password = "A123456789a#"
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(sign_up.status_code,201)
        response = json.loads(login.data.decode())
        # self.assertEqual(response["message"],"successfully logged in")
