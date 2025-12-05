import psycopg2
from dotenv import load_dotenv

load_dotenv(override=True)

# DATABASE_NAME = os.getenv("Labb 2")
# PASSWORD = os.getenv("postgres")

DATABASE_NAME = "Labb 2"
PASSWORD = "postgres"


def get_connection():
    """
    Function that returns a single connection
    In reality, we might use a connection pool, since
    this way we'll start a new connection each time
    someone hits one of our endpoints, which isn't great for performance
    """
    return psycopg2.connect(
        dbname=DATABASE_NAME,
        user="postgres",  # change if needed
        password=PASSWORD,
        host="localhost",  # change if needed
        port="5432",  # change if needed
    )


def create_tables():
    """
    A function to create the necessary tables for the project.
    """
    connection = get_connection()
    with open("tables.sql", "r") as f:
        sql = f.read()
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(sql)

    # with connection:
    #     with connection.cursor() as cursor:
    #         # 1. USERS
    #         cursor.execute("""CREATE TABLE users (
    #             user_ID SERIAL PRIMARY KEY,
    #             email VARCHAR(255) NOT NULL UNIQUE,
    #             first_name VARCHAR(255),
    #             last_name VARCHAR(255),
    #             phone_number VARCHAR(255),
    #             date_of_birth DATE,
    #             gender VARCHAR(15) CHECK(gender IN ('Man', 'Kvinna', 'Icke-binär', 'Osäker', 'Vill ej svara', 'Annat')),
    #             profile_photo VARCHAR(255),
    #             balance INT NOT NULL DEFAULT 0,
    #             created_at TIMESTAMP NOT NULL DEFAULT NOW()
    #         );
    #     """)
    #         # 2
    # # Implement
    # pass


if __name__ == "__main__":
    # Only reason to execute this file would be to create new tables, meaning it serves a migration file
    create_tables()
    print("Tables created successfully.")
