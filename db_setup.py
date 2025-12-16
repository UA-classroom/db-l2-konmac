import os  # Importing OS so I can read variables from my .env file where i store database login information

import psycopg2
from dotenv import (
    load_dotenv,  # Reads .env file and loads the values into environment variables
)

load_dotenv(override=True)

DATABASE_NAME = os.getenv("DATABASE_NAME")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")


if not DATABASE_NAME or not PASSWORD:
    raise ValueError("DATABASE_NAME and PASSWORD must be set in .env file")

def get_connection():
    
    """
    Function establishes a connection to the database on VG level
    Uses variables from env file to keep sensitive data private
    And makes the function reusable
    """

    connection = psycopg2.connect(
        dbname=DATABASE_NAME,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
)
    return connection 

def create_tables():
    """
    Creates database tables by running SQL commands from setup.sql file
    """
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            with open("setup.sql", "r", encoding="utf-8") as f:
                sql = f.read()
            cursor.execute(sql)
        print("Tables created successfully.")


if __name__ == "__main__":
    create_tables()

