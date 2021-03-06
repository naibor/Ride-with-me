"""
templates
"""

TEMPLATE ={
    "swagger":"2.0",
    "info":{
        "title":"Ride_With_Me",
        "description":"A carpooling application \
        that provides drivers with the ability to create ride offers \
        and passengers to join available ride offers."

    },
    "securityDefinitions":{
        "TokenHeader":{
            "type":"apiKey",
            "name":"Authorization",
            "in":"header"

        }
    },
    "definitions":{
        "Passenger_sign_up":{
            "type":"object",
            "properties":{
                "name":{
                    "type":"string"
                },
                "username":{
                    "type":"string"
                },
                "phone_number":{
                    "type":"string"
                },
                "password":{
                    "type":"string"
                },
                "confirmpassword":{
                    "type":"string"  
                }
            }
        },
        "Driver_register":{
            "type":"object",
            "properties":{
                "name":{
                    "type":"string"
                },
                "username":{
                    "type":"string"
                },
                "phone_number":{
                    "type":"string"
                },
                "car":{
                    "type":"string"
                },
                "password":{
                    "type":"string"
                },
                "confirmpassword":{
                    "type":"string"  
                }
            }
        },
        "User_login":{
            "type":"object",
            "properties":{
                "username":{
                    "type":"string"
                },
                "password":{
                    "type":"string"
                }
                
            }
        },
        "Ride_Offer":{
            "type":"object",
            "properties":{
                "location":{
                    "type":"string"                    
                },
                "destination":{
                    "type":"string"
                },
                "status":{
                    "type":"string"
                }
                
            }
        },
        "Ride_request":{
            "type":"object",
            "properties":{
                "phone_number":{
                    "type":"string"
                }
            }
        }
    }

}
