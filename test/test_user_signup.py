import unittest  
import os
import json

from Api import app
from Api.resource import create_app

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
    def test_user_not_already_signed_up(self):
        """test user is not already signed in"""
        self.sign_up =self.client.post(
            "api/v1/users",
            data = json.dumps(dict(
                first_name = 'Naibor',
                last_name = 'Leona',
                user_name = 'Lisa',
                password = '12345',
                confirm_password = '12345'
            )),
            content_type = "applicatio/json"
        )

        self.assertIn("Lisa",user_info, msg="user does not exist")
        self.assertIn("Welcome, you have successfully signed up",(response.data))
    
    # empty first name
    def test_user_sign_up_empty_first_name(self):
        """test user can't input empty string"""
        self.sign_up =self.client.post(
            "api/v1/users",
            data = json.dumps(dict(
                first_name='',
                last_name='Leona',
                user_name='Lisa',
                password='12345',
                confirm_password='12345'
            )),
            content_type="application/json"
        )
        self.assertEqual(response.status_code,401)
        response_data = json.loads(response.data)
        self.assertIn("Enter first name",str(response))

    # empty last name 
    def test_user_sign_up_empty_last_name(self):
        """test user can't input empty string"""
        self.sign_up =self.client.post(
            "api/v1/users",
            data = json.dumps(dict(
                first_name='Naibor',
                last_name=' ',
                user_name='Lisa',
                password='12345',
                confirm_password='12345'
            )),
            content_type="application/json"
        )
        self.assertEqual(response.status_code,401)
        response_data = json.loads(response.data)
        self.assertIn("Enter Last name",str(response))

    # empty username
    def test_user_sign_up_empty_user_name(self):
        """test user can't input empty string"""
        response = self.client.post(
            "api/v1/users",
            data = json.dumps(dict(
                first_name='Naibor',
                last_name='Leona',
                user_name='',
                password='12345',
                confirm_password='12345'
            )),
            content_type="application/json"
        )
        self.assertEqual(response.status_code,401)
        response_data = json.loads(response.data.decode())
        self.assertIn("Enter username",str(response))

    # empty password
    def test_user_sign_up_empty_password(self):
        """test user enters password"""
        response = self.client.post(
            "api/v1/users",
            data = json.dumps(dict(
                first_name='Naibor',
                last_name='Leona',
                user_name='Lisa',
                password='',
                confirm_password='12345'
            )),
            content_type="application/json"
        )
        self.assertEqual(response.status_code,401)
        response_data = json.loads(response.data.decode)
        self.assertIn("Enter password",str(response))
    # empty confirm password
    def test_user_sign_up_empty_confirm_password(self):
        """test user confirms password"""
        response =self.client.post(
            "api/v1/users",
            data = json.dumps(dict(
                first_name='',
                last_name='Leona',
                user_name='Lisa',
                password='12345',
                confirm_password='12345'
            )),
            content_type="application/json"
        )
        self.assertEqual(response.status_code,401)
        response_data = json.loads(response.data.decode)
        self.assertIn("please confirm password",str(response))
    # same confirm password and password 
    def test_user_sign_up_confirm_password_is_password(self):
        """test user password and confirm password are the same"""
        respose = self.sign_up
        self.assertEqual(response.status_code,201)
        response2 = self.client.post(
            "api/v1/users",
            data = json.dumps(dict(
                first_name='',
                last_name='Leona',
                user_name='Lisa',
                password='12345',
                confirm_password='16345'
            )),
            content_type="application/json"
        )
        self.assertEqual(response2.status_code,401)
        response_data = json.loads(response.data.decode)
        self.assertIn("password and confirm password not the same",str(response))
    # save user 
    def test_user_sign_in_info_saved(self):
        """test user infomation is saved"""
        response =self.client.post(
            "api/v1/users",
            data = json.dumps(dict(
                first_name='',
                last_name='Leona',
                user_name='Lisa',
                password='12345',
                confirm_password='12345'
            )),
            content_type="application/json"
        )
        self.assertEqual(response.status_code,201)
        response_data = json.loads(response.data)
        self.assertIn("Enter first name",str(response))

    # reset password
    def test_user_reset_password(self):
        """test user can reset password"""
        self.sign_up =self.client.post(
            "api/v1/users",
            data = json.dumps(dict(
                first_name='',
                last_name='Leona',
                user_name='Lisa',
                password='12345',
                confirm_password='12345'
            )),
            content_type="application/json"
        )
        self.assertEqual(response.status_code,401)
        response_data = json.loads(response.data)
        self.assertIn("Enter first name",str(response))

    def tearDown(self):
        pass