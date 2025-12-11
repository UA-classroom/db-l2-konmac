import os  # Importing OS so I can read variables from my .env file where i store database login information

import psycopg2  # Module that lets me connect to PostgreSQL database / run commands 
from dotenv import (
    load_dotenv,  # Reads .env file and loads the values into environment variables
)

load_dotenv(override=True)

DATABASE_NAME = os.getenv("DATABASE_NAME")
PASSWORD = os.getenv("PASSWORD")

if not DATABASE_NAME or not PASSWORD:
    raise ValueError("DATABASE_NAME and PASSWORD must be set in .env file")

def get_connection():
    """
    Function establishes a connection to the database
    Uses database_name and password from env variables
    Prints success/fail messages and returns None if connection has failed
    """
    try:
        connection = psycopg2.connect(
            dbname=DATABASE_NAME,
            user="postgres",
            password=PASSWORD,
            host="localhost",
            port="5432",
    )
        print("Database connection established successfully")
        return connection
    except Exception as e:
        print(f"Connection failed - {e}")
        return None

def create_tables():
    """
    Creates database tables by running SQL commands from setup.sql file
    Handles errors during table creation
    """
    connection = get_connection()
    if connection is None:
        print("Unable to connect to the database")
        return
    try:
        with connection:
            with connection.cursor() as cursor:
                with open("setup.sql", "r", encoding="utf-8") as f:
                    sql = f.read()
                cursor.execute(sql)
            print("Tables created successfully.")
    except Exception as e:
            print(f"Failed to create tables - {e}")


if __name__ == "__main__":
    create_tables()

