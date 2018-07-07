from test.test_db import Database

db = Database()

TABLES_SCHEMA = (
        """
        DROP TABLE IF EXISTS users CASCADE;
        CREATE TABLE users(
            user_id SERIAL PRIMARY KEY,
            user_name VARCHAR(255) NOT NULL,
            user_username VARCHAR(255) NOT NULL,
            user_car BOOLEAN,
            user_phone_number VARCHAR(255) NOT NULL,
            user_password VARCHAR(450) NOT NULL
        )
        """,
        """
        DROP TABLE IF EXISTS ride_offers CASCADE;
        CREATE TABLE ride_offers(
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
        DROP TABLE IF EXISTS ride_request CASCADE;
        CREATE TABLE ride_requests(
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

# def create_tables():
#     for command in TABLES_SCHEMA:
#         db.create_tables(command)

if __name__== '__main__':
    create_tables()