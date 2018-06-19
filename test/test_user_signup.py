import unittest  
import os
import json

from Api import app
from Api.resource import create_app
# from Api import models

class UserSignUpTestCases(unittest.TestCase):
    """class for user sign up test case"""

    def setUp(self):
        """inititalize app and define variables"""
        self.app = create_app(config_name = "testing")
        # allows our test to mimic actual clients
        self.client = self.app.test_client()
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
        response_data = json.loads(response.data)
        self.assertIn("Lisa",user_info, msg="user does not exist")
        self.assertIn("Welcome, you have successfully signed up",(response.data))
    
    def test_user_login(self):
        """test user can successfuly login"""
        pass


    def tearDown(self):
        pass