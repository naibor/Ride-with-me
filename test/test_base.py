import unittest
from test.test_database import db
from Api import create_app
# from Api import User
# db = Database()



class TestBaseTest(unittest.TestCase):
    """class base test cases"""
       
    def setUp(self):
        """initialize app and define variables"""
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        self.TABLES_SCHEMA = (
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
            );
            """
        )

        def create_tables():
    
            for command in TABLES_SCHEMA:
                db.create_tables(command)
                db.cursor.execute()
                db.commit()
       

    
    def tearDown(self):
        """Tears down test context"""
        self.app = None
        db.cursor.execute("DROP TABLE IF EXISTS ride_requests;") 
        db.cursor.execute("DROP TABLE IF EXISTS ride_offers;")
        db.cursor.execute("DROP TABLE IF EXISTS users;")
        


if __name__== '__main__':
    unittest.main()