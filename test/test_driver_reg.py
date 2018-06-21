# import unittest
# import json

# class TestDriverReg(unittest.TestCase):
#     """class for driver registration test cases"""
#     def setup(self):
#         """initialize app and define variables"""
#         self.app = create_app(config_name= "testing")
#         self.app.config["TESTING"]=True
#         self.client = self.app.test_client()
#         self.reg = self.client.post(
#             "api/v1/user/register",
#             data = json.dumps(dict(
#                 firstname = 'kamau',
#                 lastname = "njoroge",
#                 username = "kanjo",
#                 password = "1234",
#                 confirmpassword = "1234"
#             )),content_type = "application/json"
#         )
#     def test_driver_reg(self):
#         """test driver can successfuly register"""
#         response = self.reg
#         self.assertEqual(response.status_code,201)
#         response_data = json.loads(response.data.decode())
#         self.assertEqual(response_data["message"],"Welcome you have successfully registered as a driver")
         