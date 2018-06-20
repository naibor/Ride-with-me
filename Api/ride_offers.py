from flask_restful import Resource, Api


ride_offers = []
ride_Requests =[]

    
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
