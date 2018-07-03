from Api import create_app
from models.db import connect
import os

config_name = os.getenv("APP_SETTINGS")
# flask instance

app = create_app(config_name)


if __name__=="__main__":
    connect()
    app.run()