import os  # Importing OS so I can read variables from my .env file where i store database login information

import psycopg2  # Module that lets me connect to PostgreSQL database / run commands 
from dotenv import (
    load_dotenv,  # Reads .env file and loads the values into environment variables.
)

load_dotenv(override=True)

DATABASE_NAME = os.getenv("DATABASE_NAME")
PASSWORD = os.getenv("PASSWORD")


def get_connection():
    """
    Function that returns a single connection
    In reality, we might use a connection pool, since
    this way we'll start a new connection each time
    someone hits one of our endpoints, which isn't great for performance
    """
    try:
        connection = psycopg2.connect(
            dbname=DATABASE_NAME,
            user="postgres",  # change if needed
            password=PASSWORD,
            host="localhost",  # change if needed
            port="5432",  # change if needed
    )
        return connection
    except Exception as e:
        print(f"Connection failed - {e}")

def create_tables():
    """
    A function to create the necessary tables for the project.
    """
    connection = get_connection()
    if connection is None:
        print("Unable to connect to the database")
        return
    with connection:
        with connection.cursor() as cursor:
            with open("setup.sql", "r", encoding="utf-8") as f:
                sql = f.read()
                cursor.execute(sql)
    print("Tables created successfully.")


if __name__ == "__main__":
    # Only reason to execute this file would be to create new tables, meaning it serves a migration file
    create_tables()

