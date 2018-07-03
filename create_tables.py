from models.db import Database

db = Database()
def create_tables():
    commands = (
        """
        CREATE TABLE users(
            user_id SERIAL PRIMARY KEY,
            user_name VARCHAR(255) NOT NULL,
            user_username VARCHAR(255) NOT NULL,
            user_car VARCHAR(255),
            user_phone_number INT NOT NULL,
            user_password VARCHAR(450) NOT NULL
        )
        """,
        """
        CREATE TABLE ride_offers(
            offer_id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL,
            offer_location VARCHAR(255) NOT NULL,
            offer_departure_time VARCHAR(255) NOT NULL,
            offer_destination VARCHAR(255)NOT NULL,
            FOREIGN KEY (user_id)
            REFERENCES users (user_id)
            ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE ride_requests(
            offer_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            PRIMARY KEY (offer_id, user_id),
            request_location VARCHAR(255) NOT NULL,
            request_destination VARCHAR(255)NOT NULL,
            request_phone_number INT NOT NULL,
            FOREIGN KEY (user_id)
                REFERENCES users (user_id)
                ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (offer_id)
                REFERENCES ride_offers (offer_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """
    )

    for command in commands:
        db.create_tables(command)

if __name__== '__main__':
    create_tables()