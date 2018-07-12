"""test user signup and login"""
import unittest  
import os
import json
from Api import User
from Api import create_app
from test.test_base import BaseTestCase, create_tables, drop_tables
from models.db import db


class TestUserSignUp(BaseTestCase):
    """class for user sign up test case"""

    def test_user_sign_up(self):
        """test user can successfuly sign up"""
        create_tables()
        signup = self.client.post(
         "/api/v1/auth/signup",
            data = json.dumps(dict(
                name = "Naibor",
                username = "Aisa",
                phone_number = "0707900000",
                password = "A123456789a#",
                confirmpassword = "A123456789a#"
            )),
            headers = {"content-type": "application/json"}
    )
        self.assertEqual(signup.status_code,201)
        signup_data = json.loads(signup.data.decode())
        self.assertEqual(signup_data["message"],"successfully signed up")

    
    def test_user_name_empty(self):
        """test user name not empty"""
        signup = self.client.post(
            "/api/v1/auth/register",
            data = json.dumps(dict(
                name = "",
                username = "Aisa",
                phone_number = "0707900000",
                password = "A123456789a#",
                confirmpassword = "A123456789a#"
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(signup.status_code,400)

    def test_user_username_empty(self):
        """test user username not empty"""
        signup = self.client.post(
            "/api/v1/auth/register",
            data = json.dumps(dict(
                name = "Naibor",
                username = "",
                phone_number = "0707900000",
                password = "A123456789a#",
                confirmpassword = "A123456789a#"
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(signup.status_code,400)

    def test_user_phonenumber_empty(self):
        """test user phonenumber not empty"""
        signup = self.client.post(
            "/api/v1/auth/register",
            data = json.dumps(dict(
                name = "Naibor",
                username = "Aisa",
                phone_number = "",
                password = "A123456789a#",
                confirmpassword = "A123456789a#"
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(signup.status_code,400)


    def test_user_password_empty(self):
        """test user password not empty"""
        signup = self.client.post(
            "/api/v1/auth/register",
            data = json.dumps(dict(
                name = "Naibor",
                username = "Aisa",
                phone_number = "0707900000",
                password = "",
                confirmpassword = "A123456789a#"
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(signup.status_code,400)

    def test_user_confirmpassword_empty(self):
        """test user confirmpassword not empty"""
        signup = self.client.post(
            "/api/v1/auth/register",
            data = json.dumps(dict(
                name = "Naibor",
                username = "Aisa",
                phone_number = "0707900000",
                password = "A123456789a#",
                confirmpassword = ""
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(signup.status_code,400)

    def test_user_name_with_space(self):
        """test user name with spaces only"""
        signup = self.client.post(
            "/api/v1/auth/register",
            data = json.dumps(dict(
                name = "     ",
                username = "Aisa",
                phone_number = "0707900000",
                password = "A123456789a#",
                confirmpassword = "A123456789a#"
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(signup.status_code,400)

    def test_user_username_with_space(self):
        """test user username with spaces only"""
        signup = self.client.post(
            "/api/v1/auth/register",
            data = json.dumps(dict(
                name = "Naibor",
                username = "     ",
                phone_number = "0707900000",
                password = "A123456789a#",
                confirmpassword = "A123456789a#"
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(signup.status_code,400)

    def test_user_phone_number_with_space(self):
        """test user phonenumber with spaces only"""
        signup = self.client.post(
            "/api/v1/auth/register",
            data = json.dumps(dict(
                name = "Naibor",
                username = "Aisa",
                phone_number = "       ",
                password = "A123456789a#",
                confirmpassword = "A123456789a#"
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(signup.status_code,400)


    def test_user_password_short(self):
        """test user password requied length"""
        signup = self.client.post(
            "/api/v1/auth/register",
            data = json.dumps(dict(
                name = "Naibor",
                username = "Aisa",
                phone_number = "0707900000",
                password = "A9a#",
                confirmpassword = "A123456789a#"
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(signup.status_code,400)

    def test_user_confirmpassword_short(self):
        """test user confirmpassword required length"""
        signup = self.client.post(
            "/api/v1/auth/register",
            data = json.dumps(dict(
                name = "Naibor",
                username = "Aisa",
                phone_number = "0707900000",
                password = "A123456789a#",
                confirmpassword = "A39a#"
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(signup.status_code,400)


    def tearDown(self):
        """Tears down test context"""
        self.app = None
        drop_tables()
    
if __name__== '__main__':
    unittest.main()