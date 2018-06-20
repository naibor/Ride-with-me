from datetime import datetime, timedelta

request_ride={
    "location":"nakuru",
    "destination":"kakamega",

}
driver_info={}
driver_detail={
    "name":"kamau",
    "car":"toyota"
}

ride_offers = []
DTime = datetime.now() + timedelta(minutes=20)
ride_detail = {"location":"Nairobi",
               "destination":"kisumu",
               "departure": DTime.time(),
               "driver_details":driver_detail
}

class 

