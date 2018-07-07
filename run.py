from flask import make_response,jsonify
from Api import create_app
import os

config_name = os.getenv("APP_SETTINGS", "development")
# flask instance

app = create_app(config_name)

@app.errorhandler(404)
def resource_not_found(error):
    """
    handles 404 errors
    """
    return make_response(jsonify({"message": "requested URL was not found"}), 404)



if __name__=="__main__":
    app.run()