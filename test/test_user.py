"""test user signup and login"""
import unittest  
import os
import json
from Api import User
from Api import create_app
from test.test_base import TestBaseTest
from test.test_database import db

# db.cursor.execute("DROP TABLE IF EXISTS users CASCADE ;")

class TestUserSignUp(TestBaseTest):
    """class for user sign up test case"""

    def test_user_sign_up(self):
        """test user can successfuly sign up"""
        signup = self.client.post(
         "/api/v1/auth/signup",
            data = json.dumps(dict(
                name = "Naibor",
                username = "Tisa",
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
                username = "Tisa",
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
                name = "kamau",
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
                name = "kamau",
                username = "kanjo",
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
                name = "kamau",
                username = "kanjo",
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
                name = "kamau",
                username = "kanjo",
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
                username = "kanjo",
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
                name = "kamau",
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
                name = "kamau",
                username = "kanjo",
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
                name = "kamau",
                username = "kanjo",
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
                name = "kamau",
                username = "kanjo",
                phone_number = "0707900000",
                password = "A123456789a#",
                confirmpassword = "A39a#"
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(signup.status_code,400)

    
    def test_user_login(self):
        """test user can successfuly login"""
        # sign up user
        sign_up = self.client.post(
            "api/v1/auth/signup",
            data = json.dumps(dict(
                name = "Naibor",
                username = "zisa",
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
                username = "zisa",
                password = "A123456789a#"
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(login.status_code,200)
        login_data = json.loads(login.data.decode())
        self.assertEqual(login_data["message"],"successfully logged in")

    def test_driver_login(self):
        """test driver can successfuly login"""
        # register a driver
        register = self.client.post(
            "/api/v1/auth/register",
            data = json.dumps(dict(
                name = "kamau",
                username = "kaajko",
                phone_number = "0707981133",
                car = "True",
                password = "A123456789a#",
                confirmpassword = "A123456789a#",
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(register.status_code,201)
        register_data = json.loads(register.data.decode())
        self.assertEqual(register_data["message"],"successfully signup as a driver")
        
        # login driver
        login = self.client.post(
            "/api/v1/auth/login",
            data = json.dumps(dict(
                username = "kaajko",
                password = "A123456789a#"
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(login.status_code,200)
        login_data = json.loads(login.data.decode())
        self.assertEqual(login_data["message"],"successfully logged in")

    def tearDown(self):
        """Tears down test context"""
        self.app = None
        db.cursor.execute("DROP TABLE IF EXISTS ride_requests;")
        db.cursor.execute("DROP TABLE IF EXISTS ride_offers;")
        db.cursor.execute("DROP TABLE IF EXISTS users;")
    
if __name__== '__main__':
    unittest.main()