
import psycopg2

class Database:
    def __init__(self):
        self.host = "",
        self.database = "Ride_with_me",
        self.user = "naibor",
        self.password = "lisanaibor",
        self.connection = psycopg2.connect(
            host="localhost",
            user="naibor",
            dbname="testdb",
            password="lisanaibor"
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
