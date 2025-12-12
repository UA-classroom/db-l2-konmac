
"""
This file is responsible for making database queries, which your fastapi endpoints/routes can use.
The reason we split them up is to avoid clutter in the endpoints, so that the endpoints might focus on other tasks 

- Try to return results with cursor.fetchall() or cursor.fetchone() when possible
- Make sure you always give the user response if something went right or wrong, sometimes 
you might need to use the RETURNING keyword to garantuee that something went right / wrong
e.g when making DELETE or UPDATE queries
- No need to use a class here
- Try to raise exceptions to make them more reusable and work a lot with returns
- You will need to decide which parameters each function should receive. All functions 
start with a connection parameter.
- Below, a few inspirational functions exist - feel free to completely ignore how they are structured
- E.g, if you decide to use psycopg3, you'd be able to directly use pydantic models with the cursor, these examples are however using psycopg2 and RealDictCursor
"""


from db_setup import get_connection
from psycopg2.extras import RealDictCursor
from schemas import (
    TreatmentCategoriesCreate,
    TreatmentsCreate,
    OwnersCreate,
    EmployeesCreate,
    BusinessCreate,
    BusinessLocationsCreate
)


### 1. Create a new treatment and return the created row
def add_treatment(item: TreatmentsCreate):
    conn = get_connection()
    if conn is None:
        return None
    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                """
                INSERT INTO treatments (treatment_name, treatment_description, category_id, time_duration, last_min_deal)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING *; 
                """,
                (item.treatment_name, item.treatment_description, item.category_id, item.time_duration, item.last_min_deal),
            )
            inserted =  cur.fetchone()
            return inserted

### 2. Create a new treatment category and return the created row
def add_treatment_categories(item: TreatmentCategoriesCreate):
    conn = get_connection()
    if conn is None:
        return None
    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                """
                INSERT INTO treatment_categories (category_name)
                VALUES (%s)
                RETURNING *; 
                """,
                (item.category_name,),
            )
            inserted = cur.fetchone()
            return inserted

### 3. Get all categories
def get_treatment():
    conn = get_connection()
    if conn is None:
        return None
    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM treatments;")
            treatments = cur.fetchall()
    return treatments

### 4. Get all treatment categories
def get_treatment_categories():
    conn = get_connection()
    if conn is None:
        return None
    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM treatment_categories;")
            treatment_categories = cur.fetchall()
    return treatment_categories

# Owners

def add_owner(owner: OwnersCreate):
    conn = get_connection()
    if conn is None:
        return None
    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                """
                INSERT INTO owners (business_id, user_id)
                VALUES (%s, %s)
                RETURNING *;
                """,
                (owner.business_id, owner.user_id)
            )
            inserted = cur.fetchone()
            return inserted
        

def get_owners():
    conn = get_connection()
    if conn is None:
        return None
    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM owners;")
            owners = cur.fetchall()
    return owners

# Employees

def add_employee(employee: EmployeesCreate):
    conn = get_connection()
    if conn is None:
        return None
    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                """
            INSERT INTO employees (user_id, business_id, location_id, rating)
            VALUES (%s, %s, %s, %s)
            RETURNING *;
            """,
            (employee.user_id, employee.business_id, employee.location_id, employee.rating)
            )
            inserted = cur.fetchone()
            return inserted

def get_employees():
    conn = get_connection()
    if conn is None:
        return None
    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM employees;")
            employees = cur.fetchall()
    return employees

# Businesses

def add_business(business: BusinessCreate):
    conn = get_connection()
    if conn is None:
        return None
    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                """
            INSERT INTO businesses (business_name, email, phone_number, about_text, number_of_employees)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING *;
            """,
            (business.business_name, business.email, business.phone_number, business.about_text, business.number_of_employees)
            )
            inserted = cur.fetchone()
            return inserted

def get_businesses():
    conn = get_connection()
    if conn is None:
        return None
    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM businesses;")
            businesses = cur.fetchall()
    return businesses

# Business locations

def add_business_location(business_location: BusinessLocationsCreate):
    conn = get_connection()
    if conn is None:
        return None
    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                """
            INSERT INTO business_locations (business_id, phone_number, email, street_address, city, postal_code, country, longitude, latitude)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING *;
            """,
            (business_location.business_id,
            business_location.phone_number,
            business_location.email,
            business_location.street_address,
            business_location.city,
            business_location.postal_code,
            business_location.country,
            business_location.longitude,
            business_location.latitude)
            )
            inserted = cur.fetchone()
            return inserted

def get_business_locations():
    conn = get_connection()
    if conn is None:
        return None
    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM business_locations;")
            business_locations = cur.fetchall()
    return business_locations





### THIS IS JUST INSPIRATION FOR A DETAIL OPERATION (FETCHING ONE ENTRY)
# def get_treatment(con, item_id):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             cursor.execute("""SELECT * FROM items WHERE id = %s""", (item_id,))
#             item = cursor.fetchone()
#             return item


### THIS IS JUST INSPIRATION FOR A CREATE-OPERATION
# def add_item(con, title, description):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             cursor.execute(
#                 "INSERT INTO items (title, description) VALUES (%s, %s) RETURNING id;",
#                 (title, description),
#             )
#             item_id = cursor.fetchone()["id"]
#     return item_id
