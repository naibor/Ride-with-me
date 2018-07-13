import unittest
from models.db import db
from Api import create_app




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
    );
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
    );
    """,
    """
    DROP TABLE IF EXISTS ride_requests;
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
    );
    """
)

def create_tables():
    """creates tables"""
    for command in TABLES_SCHEMA:
        db.create_tables(command)
        db.commit()

def drop_tables():
    """drops table"""
    table_reverse = ["ride_requests", "ride_offers", "users"]
    for table in table_reverse:
        db.drop_table(table)
        db.commit()

class BaseTestCase(unittest.TestCase):
    """class base test cases"""
       
    def setUp(self):
        """initialize app and define variables"""
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        create_tables()

    
    def tearDown(self):
        """Tears down test context"""
        self.app = None
        drop_tables()

if __name__== '__main__':
    unittest.main()