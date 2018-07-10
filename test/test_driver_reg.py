# """tests for driver registration"""
# import unittest
# import json
# import psycopg2
# from Api import User
# from models.db import db
# from test.test_base import BaseTestCase

# class TestDriverReg(BaseTestCase):
#     """test driver is registered"""
#     def test_driver_reg(self):
#         """test driver can successfuly register"""
#         registration = self.client.post(
#             "/api/v1/auth/register",
#             data = json.dumps(dict(
#                 name = "kamau",
#                 username = "kazu",
#                 phone_number = "0707981133",
#                 car = "True",
#                 password = "A123456789a#",
#                 confirmpassword = "A123456789a#",
#             )),
#             headers = {"content-type": "application/json"}
#         )
#         self.assertEqual(registration.status_code,201)
#         response_data = json.loads(registration.data.decode())
#         self.assertEqual(response_data["message"],"successfully signup as a driver")
   
#     def test_driver_name_empty(self):
#         """test driver name not empty"""
#         registration = self.client.post(
#             "/api/v1/auth/register",
#             data = json.dumps(dict(
#                 name = "",
#                 username = "kanjo",
#                 phone_number = "4654378540",
#                 car = "True",
#                 password = "A123456789a#",
#                 confirmpassword = "A123456789a#"
#             )),
#             headers = {"content-type": "application/json"}
#         )
#         self.assertEqual(registration.status_code,400)

#     def test_driver_username_empty(self):
#         """test driver username not empty"""
#         registration = self.client.post(
#             "/api/v1/auth/register",
#             data = json.dumps(dict(
#                 name = "kamau",
#                 username = "",
#                 phone_number = "4654378540",
#                 car = "True",
#                 password = "A123456789a#",
#                 confirmpassword = "A123456789a#"
#             )),
#             headers = {"content-type": "application/json"}
#         )
#         self.assertEqual(registration.status_code,400)

#     def test_driver_phonenumber_empty(self):
#         """test driver phonenumber not empty"""
#         registration = self.client.post(
#             "/api/v1/auth/register",
#             data = json.dumps(dict(
#                 name = "kamau",
#                 username = "kanjo",
#                 phone_number = "",
#                 car = "True",
#                 password = "A123456789a#",
#                 confirmpassword = "A123456789a#"
#             )),
#             headers = {"content-type": "application/json"}
#         )
#         self.assertEqual(registration.status_code,400)

#     def test_driver_car_empty(self):
#         """test driver car not empty"""
#         registration = self.client.post(
#             "/api/v1/auth/register",
#             data = json.dumps(dict(
#                 name = "kamau",
#                 username = "kanjo",
#                 phone_number = "4654378540",
#                 car = "",
#                 password = "A123456789a#",
#                 confirmpassword = "A123456789a#"
#             )),
#             headers = {"content-type": "application/json"}
#         )
#         self.assertEqual(registration.status_code,400)

#     def test_driver_password_empty(self):
#         """test driver password not empty"""
#         registration = self.client.post(
#             "/api/v1/auth/register",
#             data = json.dumps(dict(
#                 name = "kamau",
#                 username = "kanjo",
#                 phone_number = "4654378540",
#                 car = "True",
#                 password = "",
#                 confirmpassword = "A123456789a#"
#             )),
#             headers = {"content-type": "application/json"}
#         )
#         self.assertEqual(registration.status_code,400)

#     def test_driver_confirmpassword_empty(self):
#         """test driver confirmpassword not empty"""
#         registration = self.client.post(
#             "/api/v1/auth/register",
#             data = json.dumps(dict(
#                 name = "kamau",
#                 username = "kanjo",
#                 phone_number = "4654378540",
#                 car = "True",
#                 password = "A123456789a#",
#                 confirmpassword = ""
#             )),
#             headers = {"content-type": "application/json"}
#         )
#         self.assertEqual(registration.status_code,400)

#     def test_driver_name_with_space(self):
#         """test driver name with spaces only"""
#         registration = self.client.post(
#             "/api/v1/auth/register",
#             data = json.dumps(dict(
#                 name = "     ",
#                 username = "kanjo",
#                 phone_number = "4654378540",
#                 car = "True",
#                 password = "A123456789a#",
#                 confirmpassword = "A123456789a#"
#             )),
#             headers = {"content-type": "application/json"}
#         )
#         self.assertEqual(registration.status_code,400)

#     def test_driver_username_with_space(self):
#         """test driver username with spaces only"""
#         registration = self.client.post(
#             "/api/v1/auth/register",
#             data = json.dumps(dict(
#                 name = "kamau",
#                 username = "     ",
#                 phone_number = "4654378540",
#                 car = "True",
#                 password = "A123456789a#",
#                 confirmpassword = "A123456789a#"
#             )),
#             headers = {"content-type": "application/json"}
#         )
#         self.assertEqual(registration.status_code,400)

#     def test_driver_phone_number_with_space(self):
#         """test driver phonenumber with spaces only"""
#         registration = self.client.post(
#             "/api/v1/auth/register",
#             data = json.dumps(dict(
#                 name = "kamau",
#                 username = "kanjo",
#                 phone_number = "       ",
#                 car = "True",
#                 password = "A123456789a#",
#                 confirmpassword = "A123456789a#"
#             )),
#             headers = {"content-type": "application/json"}
#         )
#         self.assertEqual(registration.status_code,400)

#     def test_driver_car_with_space(self):
#         """test driver car with spaces"""
#         registration = self.client.post(
#             "/api/v1/auth/register",
#             data = json.dumps(dict(
#                 name = "kamau",
#                 username = "kanjo",
#                 phone_number = "4654378540",
#                 car = "     ",
#                 password = "A123456789a#",
#                 confirmpassword = "A123456789a#"
#             )),
#             headers = {"content-type": "application/json"}
#         )
#         self.assertEqual(registration.status_code,400)

#     def test_driver_password_short(self):
#         """test driver password requied length"""
#         registration = self.client.post(
#             "/api/v1/auth/register",
#             data = json.dumps(dict(
#                 name = "kamau",
#                 username = "kanjo",
#                 phone_number = "4654378540",
#                 car = "True",
#                 password = "A9a#",
#                 confirmpassword = "A123456789a#"
#             )),
#             headers = {"content-type": "application/json"}
#         )
#         self.assertEqual(registration.status_code,400)

#     def test_driver_confirmpassword_short(self):
#         """test driver confirmpassword required length"""
#         registration = self.client.post(
#             "/api/v1/auth/register",
#             data = json.dumps(dict(
#                 name = "kamau",
#                 username = "kanjo",
#                 phone_number = "4654378540",
#                 car = "True",
#                 password = "A123456789a#",
#                 confirmpassword = "A39a#"
#             )),
#             headers = {"content-type": "application/json"}
#         )
#         self.assertEqual(registration.status_code,400)

#     def tearDown(self):
#         """Tears down test context"""
#         self.app = None
#         # db.cursor.execute("DROP TABLE IF EXISTS ride_requests;")
#         # db.cursor.execute("DROP TABLE IF EXISTS ride_offers;")
#         # db.cursor.execute("DROP TABLE IF EXISTS users;")
        
# if __name__== '__main__':
#     unittest.main()