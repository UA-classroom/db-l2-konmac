
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
    BusinessLocationsCreate,
    UsersCreate,
    GenderTypesCreate,
    CustomersCreate,
    BookingStatusesCreate,
    BookingsCreate
)

"""
TREATMENTS
"""

### 1. Create a new treatment and return the created row
def add_treatments(item: TreatmentsCreate):
    conn = get_connection()
    if conn is None:
        return None
    try:
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
    finally:
        conn.close()

### 2. Create a new treatment category and return the created row
def add_treatment_categories(item: TreatmentCategoriesCreate):
    conn = get_connection()
    if conn is None:
        return None
    try:
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
    finally:
        conn.close()

### 3. Get all treatments
def get_treatments():
    conn = get_connection()
    if conn is None:
        return None
    try:
        with conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("SELECT * FROM treatments;")
                treatments = cur.fetchall()
            return treatments
    finally:
        conn.close()

def delete_treatment(treatment_id: int):
    conn = get_connection()
    if conn is None:
        return None

    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                """
                DELETE FROM treatments
                WHERE treatment_id = %s
                RETURNING *;
                """,
                (treatment_id,),
            )
            deleted = cur.fetchone()
            return deleted

"""
TREATMENT CATEGORIES
"""

### 4. Get all treatment categories
def get_treatment_categories():
    conn = get_connection()
    if conn is None:
        return None
    try:
        with conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("SELECT * FROM treatment_categories;")
                treatment_categories = cur.fetchall()
            return treatment_categories
    finally:
        conn.close()

"""
OWNERS
"""

def add_owners(owner: OwnersCreate):
    conn = get_connection()
    if conn is None:
        return None
    try:
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
    finally:
        conn.close()

def get_owners():
    conn = get_connection()
    if conn is None:
        return None
    try:
        with conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("SELECT * FROM owners;")
                owners = cur.fetchall()
            return owners
    finally:
        conn.close()

"""
EMPLOYEES
"""

def add_employees(employee: EmployeesCreate):
    conn = get_connection()
    if conn is None:
        return None
    try:
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
    finally:
        conn.close()

def get_employees():
    conn = get_connection()
    if conn is None:
        return None
    try:
        with conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("SELECT * FROM employees;")
                employees = cur.fetchall()
            return employees
    finally:
        conn.close()

def delete_employee(employee_id: int):
    conn = get_connection()
    if conn is None:
        return None

    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                """
                DELETE FROM employees
                WHERE employee_id = %s
                RETURNING *;
                """,
                (employee_id,),
            )
            deleted = cur.fetchone()
            return deleted


"""
BUSINESSES
"""

def add_businesses(business: BusinessCreate):
    conn = get_connection()
    if conn is None:
        return None
    try:
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
    finally:
        conn.close()

def get_businesses():
    conn = get_connection()
    if conn is None:
        return None
    try:
        with conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("SELECT * FROM businesses;")
                businesses = cur.fetchall()
            return businesses
    finally:
        conn.close()

def update_business(business_id: int, businesses: BusinessCreate):
    conn = get_connection()
    if conn is None:
        return None
    try:
        with conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    """
                    UPDATE businesses
                    SET
                        business_name = %s,
                        email = %s,
                        phone_number = %s,
                        about_text = %s
                    WHERE business_id = %s
                    RETURNING *;
                    """,
                    (businesses.business_name, businesses.email,
                    businesses.phone_number,businesses.about_text, business_id),
                )
                return cur.fetchone()
    finally:
        conn.close()

"""
BUSINESS LOCATIONS
"""

def add_business_locations(business_location: BusinessLocationsCreate):
    conn = get_connection()
    if conn is None:
        return None
    try:
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
    finally:
        conn.close()

def get_business_locations():
    conn = get_connection()
    if conn is None:
        return None
    try:
        with conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("SELECT * FROM business_locations;")
                business_locations = cur.fetchall()
            return business_locations
    finally:
        conn.close()

# Update Business location
def update_business_location(location_id: int, business_locations: BusinessLocationsCreate):
    conn = get_connection()
    if conn is None:
        return None
    try:
        with conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    """
                    UPDATE business_locations
                    SET
                        phone_number = %s,
                        business_id = %s,
                        email = %s,
                        street_address = %s,
                        city = %s,
                        postal_code = %s,
                        country = %s,
                        longitude = %s,
                        latitude = %s
                    WHERE location_id = %s
                    RETURNING *;
                    """,
                    (business_locations.phone_number, business_locations.business_id,
                    business_locations.email, business_locations.street_address, business_locations.city,
                    business_locations.postal_code, business_locations.country, business_locations.longitude,
                    business_locations.latitude, location_id),
                )
                return cur.fetchone()
    finally:
        conn.close()


"""
USERS
"""

def add_users(item: UsersCreate):
    conn = get_connection()
    if conn is None:
        return None
    try:
        with conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    """
                    INSERT INTO users (email, password, first_name, last_name, phone_number, date_of_birth, gender_id)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    RETURNING user_id, email, first_name, last_name, phone_number, date_of_birth, gender_id, created_at; 
                    """, # I dont return it all to hide the password but I accept it in insert
                    (item.email, item.password, item.first_name, item.last_name, item.phone_number, item.date_of_birth, item.gender_id),
                )
                inserted = cur.fetchone()
            return inserted
    finally:
        conn.close()

def get_users():
    conn = get_connection()
    if conn is None:
        return None
    try:
        with conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("""
                    SELECT
                        user_id,
                        email,
                        first_name,
                        last_name,
                        phone_number,
                        date_of_birth,
                        gender_id,
                        created_at
                    FROM users;
                    """) # Skipping password to protect it
                users = cur.fetchall()
            return users
    finally:
        conn.close()

def delete_user(user_id: int):
    conn = get_connection()
    if conn is None:
        return None
    try:
        with conn:
            with conn.curson(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    """
                    DELETE FROM users
                    WHERE user_id = %s
                    RETURNING user_id, email, first_name, last_name, created_at;
                    """,
                    (user_id,),
                )
                return cur.fetchone()
    finally:
        conn.close()

def get_user_by_id(user_id: int):
    conn = get_connection()
    if conn is None:
        return None
    try:
        with conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    """
                    SELECT
                        user_id,
                        email,
                        first_name,
                        last_name,
                        phone_number,
                        date_of_birth,
                        gender_id,
                        created_at
                    FROM users
                    WHERE user_id = %s;
                    """,
                    (user_id,),
                )
                return cur.fetchone()
    finally:
        conn.close()

def update_user(user_id: int, item: UsersCreate):
    conn = get_connection()
    if conn is None:
        return None
    try:
        with conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    """
                    UPDATE users
                    SET
                        email = %s,
                        password = %s,
                        first_name = %s,
                        last_name = %s,
                        phone_number = %s,
                        date_of_birth = %s,
                        gender_id = %s
                    WHERE user_id = %s
                    RETURNING
                        user_id, email, first_name, last_name,
                        phone_number, date_of_birth, gender_id, created_at;
                    """,
                    (
                        item.email, 
                        item.password, 
                        item.first_name, 
                        item.last_name, 
                        item.phone_number, 
                        item.date_of_birth, 
                        item.gender_id, 
                        user_id,
                    ),
                )
                return cur.fetchone()
    finally:
        conn.close()


"""
GENDER TYPES
"""

def add_gender_types(item: GenderTypesCreate):
    conn = get_connection()
    if conn is None:
        return None
    try:
        with conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    """
                    INSERT INTO gender_types(gender_types)
                    VALUES (%s)
                    RETURNING *;
                    """,
                    (item.gender_types,),
                )
                inserted = cur.fetchone()
            return inserted
    finally:
        conn.close()

"""
CUSTOMERS
"""

def add_customers(customer: CustomersCreate):
    conn = get_connection()
    if conn is None:
        return None
    try:
        with conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    """
                INSERT INTO customers (user_id, balance)
                VALUES (%s, %s)
                RETURNING *;
                """,
                (customer.user_id, customer.balance)
                )
                inserted = cur.fetchone()
            return inserted
    finally:
        conn.close()

def get_customers():
    conn = get_connection()
    if conn is None:
        return None
    try:
        with conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("SELECT * FROM customers;")
                customers = cur.fetchall()
            return customers
    finally:
        conn.close()

def delete_customer(customer_id: int):
    conn = get_connection()
    if conn is None:
        return None
    try:
        with conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    """
                    DELETE FROM customers
                    WHERE customer_id = %s
                    RETURNING customer_id, user_id, balance;
                    """,
                    (customer_id,),
                )
                return cur.fetchone()
    finally:
        conn.close()


def update_customer(customer_id :int, item: CustomersCreate):
    conn = get_connection()
    if conn is None:
        return None
    try:
        with conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    """
                    UPDATE customers
                    SET
                        user_id = %s,
                        balance = %s
                    WHERE customer_id = %s
                    RETURNING 
                        customer_id, user_id, balance;
                    """,
                    (
                        item.user_id,
                        item.balance,
                        customer_id,
                    ),     
                )
                return cur.fetchone()
    finally:
        conn.close()

"""
BOOKING STATUSES
"""

def add_booking_statuses(booking_statuses: BookingStatusesCreate):
    conn = get_connection()
    if conn is None:
        return None
    try:
        with conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    """
                INSERT INTO booking_statuses (status_name)
                VALUES (%s)
                RETURNING *;
                """,
                (booking_statuses.status_name,)
                )
                inserted = cur.fetchone()
            return inserted
    finally:
        conn.close()

"""
BOOKINGS
"""

def add_bookings(bookings: BookingsCreate):
    conn = get_connection()
    if conn is None:
        return None
    try:
        with conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    """
                INSERT INTO businesses (
                location_id,treatment_id,customer_id,employee_id,
                business_id,booked_date,time_start,time_stop,
                notes,booking_status,payment_confirmed)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,)
                RETURNING *;
                """,
                (bookings.location_id,bookings.treatment_id,bookings.customer_id,bookings.employee_id,
                bookings.business_id,bookings.booked_date,bookings.time_start, bookings.time_stop,
                bookings.notes, bookings.booking_status, bookings.payment_confirmed,)
                )
                inserted = cur.fetchone()
            return inserted
    finally:
        conn.close()

def get_bookings(booking_id: int):
    conn = get_connection()
    if conn is None:
        return None
    try:
        with conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("SELECT * FROM bookings WHERE booking_id = %s;",
                    (booking_id,))
                bookings = cur.fetchone()
            return bookings
    finally:
        conn.close()


def delete_booking(booking_id: int):
    conn = get_connection()
    if conn is None:
        return None

    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                """
                DELETE FROM bookings
                WHERE booking_id = %s
                RETURNING *;
                """,
                (booking_id,),
            )
            deleted = cur.fetchone()
            return deleted

def patch_booking_status(booking_id: int, booking_status: int):
    conn = get_connection()
    if conn is None:
        return None

    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                """
                UPDATE bookings
                SET booking_status = %s
                WHERE booking_id = %s
                RETURNING *;
                """,
                (booking_status, booking_id),
            )
            return cur.fetchone()