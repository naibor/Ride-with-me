from flask_restful import Resource, Api


ride_offers = []
ride_Requests =[]
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
    
    class RideOffer(Resource):
        def post(self):
            #driver post ride offer data
            ride_offer = request.get_json()
            # validate it
            # empty field 
            if not ride_offer.get("location"):
                return{"message":"enter your location please"},401
            if not ride_offer.get("destination"):
                return{"message":"enter ride destination please"},401
            
            # space in input
            if ride_offer.get("location")==" ":
                return {"message":"spaces not allowed"},401
            if ride_offer.get("destination") == " ":
                return {"message":"spaces not allowed"},401
            
            #create a mock riderequest from class rideoffers 
            new_offer = RideOffer(new_offer.location,
                                  new_offer.destination  )

            # save the ride offer
            ride_offers.append{"location":new_offer.location,
                               "destination":new_offer.destination
                               }
            return{"message":"you have created a ride offer"}

        def get(self):
            return ride_offers

        def get(self,id):
            return 
