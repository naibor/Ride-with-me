"""test user signup and login"""
import unittest  
import os
import json
from Api import User
from Api import create_app
from test.test_base import BaseTestCase
from models.db import db


class TestUserLogin(BaseTestCase):
    """class for user sign up test case"""
    
    def test_user_login(self):
        """test user can successfuly login"""
        # sign up user
        sign_up = self.client.post(
            "api/v1/auth/signup",
            data = json.dumps(dict(
                name = "Naibor",
                username = "Bisa",
                phone_number = "0707900000",
                password = "A123456789a#",
                confirmpassword = "A123456789a#"
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(sign_up.status_code,201)
        # login user
        login = self.client.post(
            "/api/v1/auth/login",
            data = json.dumps(dict(
                username = "Bisa",
                password = "A123456789a#"
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(login.status_code,200)
        login_data = json.loads(login.data.decode())
        self.assertEqual(login_data["message"],"successfully logged in")

    
if __name__== '__main__':
    unittest.main()