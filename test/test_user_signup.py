"""test user signup and login"""
import unittest
import os
import json
from test.test_base import BaseTestCase


class TestUserSignUp(BaseTestCase):
    """class for user sign up test case"""

    def test_user_sign_up(self):
        """test user can successfuly sign up"""
        signup = self.client.post(
         "/api/v1/auth/signup",
            data = json.dumps(dict(
                name = "Naibor",
                username = "Aisa",
                email="hello@gmail.com",
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
                email="hello@gmail.com",
                phone_number = "0707900000",
                password = "A123456789a#",
                confirmpassword = "A123456789a#"
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(signup.status_code,400)

    def test_user_email_empty(self):
        """test user email not empty"""
        signup = self.client.post(
            "/api/v1/auth/register",
            data = json.dumps(dict(
                name = "Naibor",
                username = "Aisa",
                email="",
                phone_number = "0707900000",
                password = "A123456789a#",
                confirmpassword = "A123456789a#"
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(signup.status_code,400)

    def test_user_email_with_space(self):
        """test user email with spaces"""
        signup = self.client.post(
            "/api/v1/auth/register",
            data = json.dumps(dict(
                name = "Naibor",
                username = "Aisa",
                email="      ",
                phone_number = "0707900000",
                password = "A123456789a#",
                confirmpassword = "A123456789a#"
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(signup.status_code,400)

    def test_user_email_too_short(self):
        """test user name not empty"""
        signup = self.client.post(
            "/api/v1/auth/register",
            data = json.dumps(dict(
                name = "Naibor",
                username = "Aisa",
                email="hello",
                phone_number = "0707900000",
                password = "A123456789a#",
                confirmpassword = "A123456789a#"
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(signup.status_code,400)

    def test_user_email_wrong_format(self):
        """test user name not empty"""
        signup = self.client.post(
            "/api/v1/auth/register",
            data = json.dumps(dict(
                name = "Naibor",
                username = "Aisa",
                email="hellogmailcom",
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
                email="hello@gmail.com",
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
                email="hello@gmail.com",
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
                email="hello@gmail.com",
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
                email="hello@gmail.com",
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
                email="hello@gmail.com",
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
                email="hello@gmail.com",
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
                email="hello@gmail.com",
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
                email="hello@gmail.com",
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
                email="hello@gmail.com",
                phone_number = "0707900000",
                password = "A123456789a#",
                confirmpassword = "A39a#"
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(signup.status_code,400)


if __name__== '__main__':
    unittest.main()