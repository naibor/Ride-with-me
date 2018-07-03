def create_tables():
    commands = (
        """
        CREATE TABLE user(
            user_id SERIAL PRIMARY KEY,
            user_name VARCHAR(255) NOT NULL,
            user_username VARCHAR(255)NOT NULL,
            user_car VARCHAR(255),
            user_phone_number INT(255)NOT NULL,
            user_password VARCHAR(450)NOT NULL
        )
        """,
        """
        CREATE TABLE ride_request(
            request_id SERIAL PRIMARY KEY,
            request_location VARCHAR(255) NOT NULL,
            request_destination VARCHAR(255)NOT NULL,
            request_phone_number INT(255)
        )
        """,
        """
        CREATE TABLE ride_offer(
            offer_id SERIAL PRIMARY KEY,
            offer_location VARCHAR(255) NOT NULL,
            offer_departure_time VARCHAR(255) NOT NULL,
            offer_location INT(200) NOT NULL,
            offer_destination VARCHAR(255)NOT NULL,
            offer_phone_number INT(255)
        )
        """
    )