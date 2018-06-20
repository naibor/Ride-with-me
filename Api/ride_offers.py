from flask_restful import Resource, Api


ride_Offers = []
# where offers made by driver are stored
request_details = {}
# where passenger request details is stored
ride_Requests =[]
# where passanger ride requests details is stored
class RideRequest(Resource):
    # passanger posts a ride request
    def post(self):
        ride_request = request.get_json()
        # validate
        # empty field
        if not ride_request.get("location"):
            return {"message":"enter your location"},400
        if not ride_request.get("destination"):
            return{"message":"enter your destination"},400

        # empty string
        if ride_request.get("location") == " ":
            return {"message":"location can not be spaces"},400
        if ride_request.get("destination") == " ":
            return{"message":"destination can not be spaces"},400
        
        #an instance of class RideRequest
        new_request = RideRequest(ride_request.get("location"),
                                  ride_request.get("destination")
        )
        #request_details{} containing the ride requests of a user  
        ride_details[ride_request.get("location")]={
                                "location":ride_request.get("location"),
                                "destination":ride_request.get("destination")
                              }
        # save the new request to ride_request[]
        ride_Request.append(ride_details)

        return {"message":"Ride is being processed"},200
    
    class RideOffer(Resource):
        def post(self):
            #driver post ride offer data
            ride_offer = request.get_json()
            # validate it
            # empty field 
            if not ride_offer.get("location"):
                return{"message":"enter your location please"},400
            if not ride_offer.get("destination"):
                return{"message":"enter ride destination please"},400
            
            # space in input
            if ride_offer.get("location")==" ":
                return {"message":"spaces not allowed"},400
            if ride_offer.get("destination") == " ":
                return {"message":"spaces not allowed"},400
            
            #create an instance of class RideOffer
            new_offer = RideOffer(new_offer.location,
                                  new_offer.destination,
                                  new_offer.departure,
                                  new_0ffer.ride_id
                                 )

            # save the new_offer to ride_offers[]
            ride_Offers.append{"id":new_0ffer.ride_id,
                               "location":new_offer.location,
                               "destination":new_offer.destination,
                               "departure":new_offer.departure
                               }
            return{"message":"you have created a ride offer"}

        def get(self):
            # passenger can get all ride offers
            return ride_Offers

        def get(self,id):
            # passanger can get specific ride offer
            for offer in ride_Offers:
                # ie every dict in the dictionary
                if id == offer["id"]:
                    # if the id is a key in the dictionary
                    return offer
                return{"message":"ride does not exist"}
