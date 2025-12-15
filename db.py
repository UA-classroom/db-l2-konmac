
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

from psycopg2.extras import RealDictCursor

from schemas import (
    BookingsCreate,
    BookingStatusesCreate,
    BusinessCreate,
    BusinessLocationsCreate,
    CustomersCreate,
    EmployeesCreate,
    GenderTypesCreate,
    OwnersCreate,
    TreatmentCategoriesCreate,
    TreatmentsCreate,
    UsersCreate,
)

"""
TREATMENTS
"""

### 1. Create a new treatment and return the created row

def add_treatments(conn, treatments: TreatmentsCreate):
    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                """
                INSERT INTO treatments (treatment_name, treatment_description, category_id, time_duration, last_min_deal)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING *; 
                """,
                (treatments.treatment_name, treatments.treatment_description, treatments.category_id, treatments.time_duration, treatments.last_min_deal),
            )
            inserted =  cur.fetchone()
        return inserted

### 2. Create a new treatment category and return the created row

def add_treatment_categories(conn, item: TreatmentCategoriesCreate):
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

### 3. Get all treatments

def get_treatments(conn):
    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM treatments;")
            treatments = cur.fetchall()
            if treatments is None:
                raise FileNotFoundError
        return treatments

# Delete a treatment

def delete_treatment(conn, treatment_id: int):
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

def get_treatment_categories(conn):
    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM treatment_categories;")
            treatment_categories = cur.fetchall()
        return treatment_categories

"""
OWNERS
"""
# Add a owner

def add_owners(conn, owner: OwnersCreate):
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

def get_owners(conn):
    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM owners;")
            owners = cur.fetchall()
        return owners

"""
EMPLOYEES
"""

def add_employees(conn, employee: EmployeesCreate):
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

def get_employees(conn):
    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM employees;")
            employees = cur.fetchall()
        return employees

def delete_employee(conn, employee_id: int):
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

def add_businesses(conn, business: BusinessCreate):
    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                """
            INSERT INTO businesses (business_name, email, phone_number, about_text)
            VALUES (%s, %s, %s, %s)
            RETURNING *;
            """,
            (business.business_name, business.email, business.phone_number, business.about_text)
            )
            inserted = cur.fetchone()
        return inserted

def get_businesses(conn):
    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM businesses;")
            businesses = cur.fetchall()
        return businesses

def update_business(conn, business_id: int, businesses: BusinessCreate):
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

"""
BUSINESS LOCATIONS
"""

def add_business_locations(conn, business_location: BusinessLocationsCreate):
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

def get_business_locations(conn):
    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM business_locations;")
            business_locations = cur.fetchall()
        return business_locations

# Update Business location

def update_business_location(conn, location_id: int, business_locations: BusinessLocationsCreate):
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


"""
USERS
"""

def add_users(conn, user: UsersCreate):
    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                """
                INSERT INTO users (email, password, first_name, last_name, phone_number, date_of_birth, gender_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                RETURNING user_id, email, first_name, last_name, phone_number, date_of_birth, gender_id, created_at; 
                """, # I dont return it all to hide the password but I accept it in insert
                (user.email, user.password, user.first_name, user.last_name, user.phone_number, user.date_of_birth, user.gender_id),
            )
            inserted = cur.fetchone()
        return inserted

def get_users(conn):
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

def delete_user(conn, user_id: int):
    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                """
                DELETE FROM users
                WHERE user_id = %s
                RETURNING user_id, email, first_name, last_name, created_at;
                """,
                (user_id,),
            )
            return cur.fetchone()

def get_user_by_id(conn, user_id: int):
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

def update_user(conn, user_id: int, item: UsersCreate):
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


"""
GENDER TYPES
"""

def add_gender_types(conn, item: GenderTypesCreate):
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

"""
CUSTOMERS
"""

def add_customers(conn, customer: CustomersCreate):
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

def get_customers(conn):
    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM customers;")
            customers = cur.fetchall()
        return customers

def delete_customer(conn, customer_id: int):
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

def update_customer(conn, customer_id :int, item: CustomersCreate):
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

"""
BOOKING STATUSES
"""

def add_booking_statuses(conn, booking_statuses: BookingStatusesCreate):
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

"""
BOOKINGS
"""

def add_bookings(conn, bookings: BookingsCreate):
    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                """
            INSERT INTO bookings (
            location_id,treatment_id,customer_id,employee_id,
            business_id,booked_date,time_start,time_stop,
            notes,booking_status,payment_confirmed)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING *;
            """,
            (bookings.location_id,bookings.treatment_id,bookings.customer_id,bookings.employee_id,
            bookings.business_id,bookings.booked_date,bookings.time_start, bookings.time_stop,
            bookings.notes, bookings.booking_status, bookings.payment_confirmed,)
            )
            inserted = cur.fetchone()
        return inserted

def get_bookings(conn, booking_id: int):
    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM bookings WHERE booking_id = %s;",
                (booking_id,))
            bookings = cur.fetchone()
        return bookings


def delete_booking(conn, booking_id: int):
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

def patch_booking_status(conn, booking_id: int, booking_status: int):
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

def update_treatment(conn, treatment_id: int, treatment: TreatmentsCreate):
    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                """
                UPDATE treatments
                SET
                    treatment_name = %s,
                    treatment_description = %s,
                    category_id = %s,
                    time_duration = %s,
                    last_min_deal = %s
                WHERE treatment_id = %s
                RETURNING 
                    treatment_name, treatment_description, category_id,
                    time_duration,last_min_deal;
                """,
                (
                treatment.treatment_name, treatment.treatment_description,
                treatment.category_id,treatment.time_duration,treatment.last_min_deal,treatment_id,
            )  
            )
            return cur.fetchone()