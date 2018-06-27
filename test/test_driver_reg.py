"""tests for driver registration"""
import unittest
import json
from Api import User
from Api import create_app

class TestDriverReg(unittest.TestCase):
    """class for driver registration test cases"""
    def setUp(self):
        """initialize app and define variables"""
        self.app = create_app(config_name="testing")
        self.app.config["TESTING"]=True
        self.client = self.app.test_client()


    # def test_driver_reg(self):
    #     """test driver can successfuly register"""
    #     registration = self.client.post(
    #         "api/v1/user/register",
    #         data = json.dumps(dict(
    #             name = "kamau",
    #             username = "kanjo",
    #             phone_number = "4654378540",
    #             car = "toyota",
    #             password = "A123456789a#",
    #             confirmpassword = "A123456789a#"
    #         )),
    #         headers = {"content-type": "application/json"}
    #     )
    #     self.assertEqual(registration.status_code,201)
    #     response_data = json.loads(registration.data.decode())
    #     self.assertEqual(response_data["message"],"Welcome you have successfully registered as a driver")

    def test_driver_name_empty(self):
        """test driver name not empty"""
        registration = self.client.post(
            "api/v1/user/register",
            data = json.dumps(dict(
                name = "",
                username = "kanjo",
                phone_number = "4654378540",
                car = "toyota",
                password = "A123456789a#",
                confirmpassword = "A123456789a#"
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(registration.status_code,400)

    def test_driver_username_empty(self):
        """test driver username not empty"""
        registration = self.client.post(
            "api/v1/user/register",
            data = json.dumps(dict(
                name = "kamau",
                username = "",
                phone_number = "4654378540",
                car = "toyota",
                password = "A123456789a#",
                confirmpassword = "A123456789a#"
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(registration.status_code,400)

    def test_driver_phonenumber_empty(self):
        """test driver phonenumber not empty"""
        registration = self.client.post(
            "api/v1/user/register",
            data = json.dumps(dict(
                name = "kamau",
                username = "kanjo",
                phone_number = "",
                car = "toyota",
                password = "A123456789a#",
                confirmpassword = "A123456789a#"
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(registration.status_code,400)

    def test_driver_car_empty(self):
        """test driver car not empty"""
        registration = self.client.post(
            "api/v1/user/register",
            data = json.dumps(dict(
                name = "kamau",
                username = "kanjo",
                phone_number = "4654378540",
                car = "",
                password = "A123456789a#",
                confirmpassword = "A123456789a#"
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(registration.status_code,400)

    def test_driver_password_empty(self):
        """test driver password not empty"""
        registration = self.client.post(
            "api/v1/user/register",
            data = json.dumps(dict(
                name = "kamau",
                username = "kanjo",
                phone_number = "4654378540",
                car = "toyota",
                password = "",
                confirmpassword = "A123456789a#"
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(registration.status_code,400)

    def test_driver_confirmpassword_empty(self):
        """test driver confirmpassword not empty"""
        registration = self.client.post(
            "api/v1/user/register",
            data = json.dumps(dict(
                name = "kamau",
                username = "kanjo",
                phone_number = "4654378540",
                car = "toyota",
                password = "A123456789a#",
                confirmpassword = ""
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(registration.status_code,400)

    def test_driver_name_with_space(self):
        """test driver name with spaces only"""
        registration = self.client.post(
            "api/v1/user/register",
            data = json.dumps(dict(
                name = "     ",
                username = "kanjo",
                phone_number = "4654378540",
                car = "toyota",
                password = "A123456789a#",
                confirmpassword = "A123456789a#"
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(registration.status_code,400)

    def test_driver_username_with_space(self):
        """test driver username with spaces only"""
        registration = self.client.post(
            "api/v1/user/register",
            data = json.dumps(dict(
                name = "kamau",
                username = "     ",
                phone_number = "4654378540",
                car = "toyota",
                password = "A123456789a#",
                confirmpassword = "A123456789a#"
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(registration.status_code,400)

    def test_driver_phone_number_with_space(self):
        """test driver phonenumber with spaces only"""
        registration = self.client.post(
            "api/v1/user/register",
            data = json.dumps(dict(
                name = "kamau",
                username = "kanjo",
                phone_number = "       ",
                car = "toyota",
                password = "A123456789a#",
                confirmpassword = "A123456789a#"
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(registration.status_code,400)

    def test_driver_car_with_space(self):
        """test driver car with spaces"""
        registration = self.client.post(
            "api/v1/user/register",
            data = json.dumps(dict(
                name = "kamau",
                username = "kanjo",
                phone_number = "4654378540",
                car = "     ",
                password = "A123456789a#",
                confirmpassword = "A123456789a#"
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(registration.status_code,400)

    def test_driver_password_short(self):
        """test driver password requied length"""
        registration = self.client.post(
            "api/v1/user/register",
            data = json.dumps(dict(
                name = "kamau",
                username = "kanjo",
                phone_number = "4654378540",
                car = "toyota",
                password = "A9a#",
                confirmpassword = "A123456789a#"
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(registration.status_code,400)


    def test_driver_confirmpassword_short(self):
        """test driver confirmpassword required length"""
        registration = self.client.post(
            "api/v1/user/register",
            data = json.dumps(dict(
                name = "kamau",
                username = "kanjo",
                phone_number = "4654378540",
                car = "toyota",
                password = "A123456789a#",
                confirmpassword = "A39a#"
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(registration.status_code,400)
