from Api import create_app
import os

config_name = os.getenv("APP_SETTINGS", "development")
# flask instance

app = create_app(config_name)


if __name__=="__main__":
    app.run()