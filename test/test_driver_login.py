"""test user signup and login"""
import unittest
import os
import json
from Api import User
from Api import create_app
from test.test_base import BaseTestCase
from models.db import db


class TestDriverLogin(BaseTestCase):
    """class for driver login test case"""

    def test_driver_login(self):
        """test driver can successfuly login"""
        # register a driver
        register = self.client.post(
            "/api/v1/auth/register",
            data = json.dumps(dict(
                name = "Laban",
                username = "Dennis",
                email="hello@gmail.com",
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
                username = "Dennis",
                password = "A123456789a#"
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(login.status_code,200)
        login_data = json.loads(login.data.decode())
        self.assertEqual(login_data["message"],"successfully logged in")

if __name__== '__main__':
    unittest.main()