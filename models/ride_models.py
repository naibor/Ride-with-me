from datetime import datetime, timedelta

request_ride={
    "location":"nakuru",
    "destination":"kakamega",
<<<<<<< HEAD
}

ride_offers = []

=======

}
>>>>>>> ft-get-ride-offers-api-158423117
driver_info={}
driver_detail={
    "name":"kamau",
    "car":"toyota"
}


DTime = datetime.now() + timedelta(minutes=20)
ride_detail = {"location":"Nairobi",
               "destination":"kisumu",
               "departure": DTime.time(),
               "driver_details":driver_detail
}


class RideOffer:
    """Driver offers ride"""
    def __init__(self,location,destination,):
        self.location = location
        self.destination = destination
        departure = DTime.time()
        ride_id = len(ride_offers)
        driver_details = driver_detail


class RideRequest:
    """User request a ride"""
    def __init__(self,location,destination):
        self.location = location
        self.destination = destination




