"""test for driver ride offer"""
import unittest
import os
import json
from Api import create_app
from datetime import datetime, timedelta 
from models import ride_models
from test.test_base import BaseTestCase, create_tables
from models.db import db
DTime = datetime.now() + timedelta(minutes=20)

class TestValidateRideOffer(BaseTestCase):
    """test validate ride offers"""
    def setUp(self):
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        create_tables()
        # register driver
        register = self.client.post(
            "/api/v1/auth/register",
            data = json.dumps(dict(
                name = "kulikua",
                username = "monday",
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
                username = "monday",
                password = "A123456789a#"
            )),
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(login.status_code,200)
        login_data = json.loads(login.data.decode())
        self.token = login_data["access_token"]

        # create offer
        create = self.client.post(
            "/api/v1/users/rides",
            data = json.dumps(dict(
                RideId = "1",
                location = "Nanyuki",
                destination = "kisumu",
                departure = str(DTime.time())
            )),
            headers = {"content-type": "application/json",
                       "Authorization":self.token}
        )  
        self.assertEqual(create.status_code,201) 
     

    # test field validations
    def test_location_field_empty(self):
        """test ride offer fields are not empty"""
        response = self.client.post(
            "/api/v1/users/rides",
            data = json.dumps(dict(
                RideId = "1",
                location = "",
                destination = "kisumu",
                departure = str(DTime.time())
            )),
            headers = {"content-type": "application/json",
                       "Authorization":self.token}
        )  
        self.assertEqual(response.status_code,400)
        
    def test_destination_field_empty(self):
        """test destination field not empty"""
        response = self.client.post(
            "/api/v1/users/rides",
            data = json.dumps(dict(
                RideId = "1",
                location = "Naibor",
                destination = "",
                departure = str(DTime.time())
            )),
            headers = {"content-type": "application/json",
                       "Authorization":self.token}
        )
        self.assertEqual(response.status_code,400)
         
    def test_location_field_string(self):
        """test input fields are strings"""
        response = self.client.post(
            "/api/v1/users/rides",
            data = json.dumps(dict(
                RideId = "1",
                location = "5",
                destination = "kisumu",
                departure = str(DTime.time())
            )),
            headers = {"content-type": "application/json",
                       "Authorization":self.token}
        )
        self.assertEqual(response.status_code, 400)
    
    def test_destination_field_string(self):
        """test destiantion fields are strings"""
        response = self.client.post(
            "/api/v1/users/rides",
            data = json.dumps(dict(
                RideId = "1",
                location = "Nairobi",
                destination = "10",
                departure = str(DTime.time())
            )),
            headers = {"content-type": "application/json",
                       "Authorization":self.token}
        )
        self.assertEqual(response.status_code, 400)

    def test_location_field_with_space(self):
        """test location fields with spaces only"""
        response = self.client.post(
            "/api/v1/users/rides",
            data = json.dumps(dict(
                RideId = "1",
                location = "     ",
                destination = "kisumu",
                departure = str(DTime.time())
            )),
            headers = {"content-type": "application/json",
                       "Authorization":self.token}
        )
        self.assertEqual(response.status_code, 400)

    def test_destination_field_with_space(self):
        """test destination fields with spaces only"""
        response = self.client.post(
            "/api/v1/users/rides",
            data = json.dumps(dict(
                RideId = "1",
                location = "Nairobi",
                destination = "     ",
                departure = str(DTime.time())
            )),
            headers = {"content-type": "application/json",
                       "Authorization":self.token}
        )
        self.assertEqual(response.status_code, 400)

    def test_location_field_right_length(self):
        """test location field short """
        response = self.client.post(
            "/api/v1/users/rides",
            data = json.dumps(dict(
                RideId = "1",
                location = "Na",
                destination = "kisumu",
                departure = str(DTime.time())
            )),
            headers = {"content-type": "application/json",
                       "Authorization":self.token}
        )
        self.assertEqual(response.status_code, 400)

if __name__== '__main__':
    unittest.main()

    
