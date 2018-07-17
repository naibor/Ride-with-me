"""test for driver ride offer"""
import unittest
import os
import json
from datetime import datetime, timedelta 
from models import ride_models
from Api import create_app
from test.test_base import BaseTestCase, create_tables, drop_tables
from models.db import db
DTime = datetime.now() + timedelta(minutes=20)

class TestDriverResponse(BaseTestCase):
    """test driver can offer rides"""

    def test_driver_response_to_ride_request(self):
        """test driver can create ride offer"""
    # register driver
        register = self.client.post(
            "/api/v1/auth/register",
            data = json.dumps(dict(
                name = "kamau",
                username = "kajoo",
                phone_number = "0707981133",
                car = "True",
                password = "A123456789a#",
                confirmpassword = "A123456789a#",
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(register.status_code,201)

    # login driver
        login = self.client.post(
            "/api/v1/auth/login",
            data = json.dumps(dict(
                username = "kajoo",
                password = "A123456789a#"
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(login.status_code,200)
        login_data = json.loads(login.data.decode())
        driver_token = login_data["access_token"]

    # create offer
        create = self.client.post(
            "/api/v1/rides",
            data = json.dumps(dict(
                RideId = "1",
                location = "Nanyuki",
                destination = "kisumu",
                departure = str(DTime.time())
            )),
            headers = {"content-type": "application/json",
                        "Authorization":driver_token}
        )  
        self.assertEqual(create.status_code,201) 

    # signup user
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
    # user login
        login = self.client.post(
            "/api/v1/auth/login",
            data = json.dumps(dict(
                username = "Aisa",
                password = "A123456789a#"
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(login.status_code,200)
        login_data = json.loads(login.data.decode())
        user_token = login_data["access_token"]

    # get one offer
        response = self.client.get(
            "api/v1/rides/1",
            headers = {"content-type": "application/json",
                       "Authorization":user_token}
            ) 
        self.assertEqual(response.status_code,200) 

    #    make a request to join a ride offer
        request = self.client.post(
            "/api/v1/rides/1/requests",
            data = json.dumps(dict()),
            headers = {"content-type": "application/json",
                       "Authorization":user_token}
                    )
        # import pdb; pdb.set_trace()
        self.assertEqual(request.status_code,201)
  
    # driver respond to ride request 
        response = self.client.put(
            "/api/v1/rides/1/requests/1",
            data = json.dumps(dict(
                status = "True"
            )),
            headers = {"content-type": "application/json",
                          "Authorization":driver_token}
        )
        self.assertEqual(request.status_code,201)
        responses = json.loads(response.data.decode())
        self.assertEqual(responses["message"],"Request updated successfully")
        drop_tables()
    # #validate response made by drive
    # def test_response_is_bool(self):
    #     """test status response is boolean"""
    #     response = self.client.put(
    #         "/api/v1/rides/1/requests/1",
    #         data = json.dumps(dict(
    #             status = "12345"
    #         )),
    #         headers = {"content-type": "application/json",
    #                      "Authorization":driver_token}
    #     )
    #     self.assertEqual(response.status_code,400)


if __name__== '__main__':
    unittest.main()
            


