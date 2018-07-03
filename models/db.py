import psycopg2
from Instance.config import configdb

def connect():
    connection = None
    try:
        params = configdb()
        connection = psycopg2.connect(**params) 
        mycursor = connection.cursor()
        mycursor.execute('SELECT version()')
        db_version = mycursor.fetchone()
        print (db_version)
        mycursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connection is not None:
            connection.close()
            print("Database connection closed")



    def connects(self):
        pass

    def commit(self):
        pass
    def close(self):
        pass