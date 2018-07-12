import psycopg2
import os

class Database:
    def __init__(self):
        self.connection = psycopg2.connect(
            host="localhost",
            user=os.getenv("DATABASE_USER","naibor"),
            dbname=os.getenv("DATABASE_NAME","Ride_with_me"),
            password=os.getenv("DATABASE_PASSWORD","lisanaibor")
        )
        self.cursor = self.connection.cursor()

    def commit(self):
      self.connection.commit()

    def query_db(self, query_string):
       self.cursor.execute(query_string)

    def create_tables(self, table):
        self.cursor.execute(table)
        self.commit()

    def drop_table(self,table_name):
        self.cursor.execute("DROP TABLE IF EXISTS " + table_name + ";") 
        self.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()

db = Database()
