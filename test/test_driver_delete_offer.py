"""test for driver ride offer"""
import unittest
import os
import json
from datetime import datetime, timedelta 
from models import ride_models
from test.test_base import BaseTestCase
from models.db import db
DTime = datetime.now() + timedelta(minutes=20)

class TestDriverRideOffer(BaseTestCase):
    """test driver can offer rides"""
    
    def test_delete_ride_offer(self):
        """tests driver can delete ride offer"""
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
        token = login_data["access_token"]

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
                       "Authorization":token}
        )  
        self.assertEqual(create.status_code,201) 

    # get one offer
        response = self.client.get(
            "api/v1/users/rides/1",
            headers = {"content-type": "application/json",
                          "Authorization":token}
            ) 
        self.assertEqual(response.status_code,200)

    # delete an offer
   
        delete_offer = self.client.delete(
            "api/v1/users/rides/1",
            headers = {"content-type": "application/json",
                          "Authorization":token}
            ) 
        self.assertEqual(delete_offer.status_code,200)
        # self.assertEqual(response["message"],"ride delete")

  
if __name__== '__main__':
    unittest.main()