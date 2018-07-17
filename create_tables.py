from models.db import Database

db = Database()


def create_tables():
    TABLES_SCHEMA = (
            """
            CREATE TABLE IF NOT EXISTS users(
                user_id SERIAL PRIMARY KEY,
                user_name VARCHAR(255) NOT NULL,
                user_username VARCHAR(255) NOT NULL,
                user_car BOOLEAN,
                user_phone_number VARCHAR(255) NOT NULL,
                user_password VARCHAR(450) NOT NULL
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS ride_offers(
                offer_id SERIAL PRIMARY KEY,
                user_offer_id INTEGER NOT NULL,
                offer_location VARCHAR(255) NOT NULL,
                offer_departure_time VARCHAR(255) NOT NULL,
                offer_destination VARCHAR(255)NOT NULL,
                FOREIGN KEY (user_offer_id)
                REFERENCES users (user_id)
                ON UPDATE CASCADE ON DELETE CASCADE
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS ride_requests(
                request_id SERIAL PRIMARY KEY,
                offer_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                request_accepted_reject BOOLEAN,
                FOREIGN KEY (user_id)
                    REFERENCES users (user_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (offer_id)
                    REFERENCES ride_offers (offer_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
            )
            """
        )

    for command in TABLES_SCHEMA:
        db.create_tables(command)

# if __name__== '__main__':
#     create_tables()