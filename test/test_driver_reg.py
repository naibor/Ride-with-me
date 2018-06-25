import unittest
import json
from Api import User
from Api import create_app

class TestDriverReg(unittest.TestCase):
    """class for driver registration test cases"""
    def setUp(self):
        """initialize app and define variables"""
        self.app = create_app(config_name= "testing")
        self.app.config["TESTING"]=True
        self.client = self.app.test_client()

    def test_driver_reg(self):
        """test driver can successfuly register"""
        registration = self.client.post(
            "api/v1/user/register",
            data=json.dumps(dict(
                name = "kamau",
                username = "kanjo",
                phone_number = "4678540",
                car = "toyota",
                password = "1234",
                confirmpassword = "1234"
            )),
            content_type = "application/json"
        )
        self.assertEqual(registration.status_code,201)
        response_data = json.loads(registration.data.decode())
        self.assertEqual(response_data["message"],"Welcome you have successfully registered as a driver")
     def test_request_not_empty(self):
            pass

    def test_request_no_space(self):
        pass

    def tearDown(self):
        pass     