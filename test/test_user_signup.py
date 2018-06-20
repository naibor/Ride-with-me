import unittest  
import os
import json

# from Api.resource import create_app
from Api import signup_info 

class UserSignUpTestCases(unittest.TestCase):
    """class for user sign up test case"""
    def setUp(self):
        """inititalize app and define variables"""
        # self.app = create_app(config_name = "testing")
        # or the below whenyou are not using create_app funtion
        self.app.config["TESTING"]=True
        # a flask environmnet variable 
        self.client = self.app.test_client()
        # allows our test to mimic actual clients
        self.sign_up =self.client.post(
            "api/v1/users",
            data = json.dumps(dict(
                first_name='Naibor',
                last_name='Leona',
                user_name='Lisa',
                password='12345',
                confirm_password='12345'
            )),
            content_type="application/json"
        )


        # sign up a user
    def test_user_sign_up(self):
        """test user can successfuly sign up"""
        response = self.sign_up
        # assert response code is 201
        self.assertEqual(response.status_code,201)
        # deserialize response data
        response_data = json.loads(response.data.decode())

        self.assertEqual(response_data["message"],"Welcome you have successfully signed up")
    
    def test_user_login(self):
        """test user can successfuly login"""
        pass


    def tearDown(self):
        pass