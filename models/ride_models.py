from datetime import datetime, timedelta

request_ride={
    "location":"nakuru",
    "destination":"kakamega",
}

ride_offers = []

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
class RideRequest(Resource):
    
    def post(self):
        ride_request = request.get_json()
        
        # validate it
        # empty field
        if not ride_request.get("location"):
            return {"message":"enter your location"},401
        if not ride_request.get("destination"):
            return{"message":"enter your destination"},401

        # empty string
        if ride_request.get("location"):
            return {"message":"enter your location not spaces"},401
        if ride_request.get("destination"):
            return{"message":"enter your destination not empty spaces"},401
        
        #an instance of class ride request
        new_request = RideRequest(request_ride.get("location"),
                                ride_request.get("destination")
                                ) 

        # save the ride request
        ride_Request.append("location":new_request.location,
                            "destination":new_request.destination
                            )

        return {"message":"Ride is being processed"},200

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




