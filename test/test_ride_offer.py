       
import unittest
import os
import json
from datetime import datetime, timedelta 
from models import ride_models

from Api import create_app
 
class TestRideOffer(unittest.TestCase):
    def setUp(self):
        """inititalize app and define variables"""
        self.app = create_app(config_name = "testing")
        # allows our test to mimic actual clients
        self.app.config["TESTING"]=True
        self.client = self.app.test_client()
        self.DTime = datetime.now() + timedelta(minutes=20)
                
    def test_get_ride_offers(self):
        """test user can view all ride offers"""
        response =self.client.post(
            "api/v1/user/create",
            data=json.dumps(dict(
                RideId= "1",
                location = "Nanyuki",
                destination = "kisumu",
                departure = str(self.DTime.time()),
                driver_details = (dict(
                    name = "kamau",
                    car = "toyoya"
                ))
            )),
            content_type = "application/json"
        )  

        self.assertEqual(response.status_code,201) 
        response = self.client.get('/api/v1/user/offer/<location>',content_type = "application/json")
        self.assertEqual(response.status_code,200 )

    def test_request_not_empty(self):
        pass

    def test_request_no_space(self):
        pass
    def tearDown(self):
        pass
