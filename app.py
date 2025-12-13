
import psycopg2
from db import (
    add_treatment_categories,
    add_treatments,
    get_treatment_categories,
    get_treatments,
    add_owners,
    get_owners,
    add_employees,
    get_employees,
    add_businesses,
    get_businesses,
    add_business_locations,
    get_business_locations,
    add_users,
    get_users,
    add_gender_types
)
from fastapi import FastAPI, HTTPException, status
from schemas import(
    TreatmentCategoriesCreate,
    TreatmentsCreate,
    OwnersCreate,
    EmployeesCreate,
    BusinessLocationsCreate,
    BusinessCreate,
    UsersCreate,
    GenderTypesCreate
)

app = FastAPI()


"""
ADD ENDPOINTS FOR FASTAPI HERE
Make sure to do the following:
- Use the correct HTTP method (e.g get, post, put, delete)
- Use correct STATUS CODES, e.g 200, 400, 401 etc. when returning a result to the user
- Use pydantic models whenever you receive user data and need to validate the structure and data types (VG)
This means you need some error handling that determine what should be returned to the user
Read more: https://www.geeksforgeeks.org/10-most-common-http-status-codes/
- Use correct URL paths the resource, e.g some endpoints should be located at the exact same URL, 
but will have different HTTP-verbs.
"""

# except psycopg2.IntegrityError as e:

# IntegrityError is raised when a database constraint is violated, such as:

# ❌ foreign key violation

# ❌ unique constraint violation

# ❌ NOT NULL violation

# ❌ check constraint violation

# Example causes:

# invalid category_id (FK)

# duplicate email

# missing required column

# negative value blocked by CHECK


# Treatment categories

@app.post("/treatment_categories/", status_code=status.HTTP_201_CREATED)
def create_treatment_categories(treatment_category: TreatmentCategoriesCreate):
    try:
        treatment_categories = add_treatment_categories(treatment_category)
        if treatment_categories is None:
            raise HTTPException(status_code=503, detail="Database unavailable")
        return {"treatment_category": treatment_categories,
                "message": "Treatment category created successfully"}
    except psycopg2.errors.UniqueViolation:
        raise HTTPException(status_code=409, detail="Treatment already exists")
    except psycopg2.OperationalError: 
        raise HTTPException(status_code=503, detail="Database unavailable")
    except psycopg2.Error:
        raise HTTPException(status_code=500, detail="Database error occurred")
    
@app.get("/treatment_categories/")
def read_treatment_categories():
    treatment_categories = get_treatment_categories()
    if treatment_categories is None:
        raise HTTPException(status_code=503, detail="Database unavailable")
    return {"treatment_categories": treatment_categories}

#Treatments

@app.post("/treatments/", status_code=status.HTTP_201_CREATED)
def create_treatment(treatment: TreatmentsCreate):
    try:
        treatments = add_treatments(treatment)
        if treatments is None:
            raise HTTPException(status_code=503, detail="Database unavailable")
        return {"treatments": treatments,
                "message": "Treatment added successfully"}
    except psycopg2.errors.ForeignKeyViolation:
        raise HTTPException(status_code=400, detail="Invalid category ID")
    except psycopg2.errors.UniqueViolation:
        raise HTTPException(status_code=409, detail="Treatment already exists")
    except psycopg2.OperationalError: 
        raise HTTPException(status_code=503, detail="Database unavailable")
    except psycopg2.Error:
        raise HTTPException(status_code=500, detail="Database error occurred")

@app.get("/treatments/")
def read_treatments():
    treatments = get_treatments()
    if treatments is None:
        raise HTTPException(status_code=503, detail="Database unavailable")
    return {"treatments": treatments}

# Owners

@app.post("/owners/", status_code=status.HTTP_201_CREATED)
def create_owners(owner: OwnersCreate):
    try:
        owners = add_owners(owner)
        if owners is None:
            raise HTTPException(status_code=503, detail="Database unavailable")
        return {"owners": owners,
                "message": "Owner added successfully"}
    except psycopg2.errors.ForeignKeyViolation:
        raise HTTPException(status_code=400, detail="Invalid ID")
    except psycopg2.errors.UniqueViolation:
        raise HTTPException(status_code=409, detail="Owner already exists")
    except psycopg2.OperationalError: 
        raise HTTPException(status_code=503, detail="Database unavailable")
    except psycopg2.Error:
        raise HTTPException(status_code=500, detail="Database error occurred")

@app.get("/owners/")
def read_owners():
    owners = get_owners()
    if owners is None:
        raise HTTPException(status_code=503, detail="Database unavailable")
    return {"owners": owners}


# Employees

@app.post("/employees/", status_code=status.HTTP_201_CREATED)
def create_employees(employee: EmployeesCreate):
    try:
        employees = add_employees(employee)
        if employees is None:
            raise HTTPException(status_code=503, detail="Database unavailable")
        return {"employees": employees,
                "message": "Employee added successfully!"}
    except psycopg2.errors.ForeignKeyViolation:
        raise HTTPException(status_code=400, detail="Invalid ID")
    except psycopg2.errors.UniqueViolation:
        raise HTTPException(status_code=409, detail="Employee already exists")
    except psycopg2.OperationalError: 
        raise HTTPException(status_code=503, detail="Database unavailable")
    except psycopg2.Error:
        raise HTTPException(status_code=500, detail="Database error occurred")

@app.get("/employees/")
def read_employees():
    employees = get_employees()
    if employees is None:
        raise HTTPException(status_code=503, detail="Database unavailable")
    return {"employees": employees}


# Businesses

@app.post("/businesses/", status_code=status.HTTP_201_CREATED)
def create_business(business: BusinessCreate):
    try:
        businesses = add_businesses(business)
        if businesses is None:
            raise HTTPException(status_code=503, detail="Database unavailable")
        return {"businesses": businesses,
                "message": "Business added successfully!"}
    except psycopg2.errors.UniqueViolation:
        raise HTTPException(status_code=409, detail="Business already exists")
    except psycopg2.OperationalError: 
        raise HTTPException(status_code=503, detail="Database unavailable")
    except psycopg2.Error:
        raise HTTPException(status_code=500, detail="Database error occurred")

@app.get("/businesses/")
def read_business():
    businesses = get_businesses()
    if businesses is None:
        raise HTTPException(status_code=503, detail="Database unavailable")
    return {"businesses": businesses}


# Business locations

@app.post("/business_locations/", status_code=status.HTTP_201_CREATED)
def create_business_location(business_location: BusinessLocationsCreate):
    try:
        business_locations = add_business_locations(business_location)
        if business_locations is None:
            raise HTTPException(status_code=503, detail="Database unavailable")
        return {"business_locations": business_locations,
                "message": "Business location added successfully!"}
    except psycopg2.errors.ForeignKeyViolation:
        raise HTTPException(status_code=400, detail="Invalid ID")
    except psycopg2.errors.UniqueViolation:
        raise HTTPException(status_code=409, detail="Business location already exists")
    except psycopg2.OperationalError: 
        raise HTTPException(status_code=503, detail="Database unavailable")
    except psycopg2.Error:
        raise HTTPException(status_code=500, detail="Database error occurred")

@app.get("/business_locations/")
def read_business_locations():
    business_locations = get_business_locations()
    if business_locations is None:
        raise HTTPException(status_code=503, detail="Database unavailable")
    return {"business_locations": business_locations}

# Create a new user

@app.post("/users/", status_code=status.HTTP_201_CREATED)
def create_users(user: UsersCreate):
    try:
        created_user = add_users(user)
        if created_user is None:
            raise HTTPException(status_code=503, detail="Database unavailable")
        return {"users": created_user,
                "message": "User added successfully!"}
    except psycopg2.errors.ForeignKeyViolation:
        raise HTTPException(status_code=400, detail="Invalid gender ID")
    except psycopg2.errors.UniqueViolation:
        raise HTTPException(status_code=409, detail="User already exists")
    except psycopg2.OperationalError: 
        raise HTTPException(status_code=503, detail="Database unavailable")
    except psycopg2.Error:
        raise HTTPException(status_code=500, detail="Database error occurred")
    
# Read users

@app.get("/users/")
def read_users():
    users = get_users()
    if users is None:
        raise HTTPException(status_code=503, detail="Database unavailable")
    return users

# Create new gender type

@app.post("/gender_types/", status_code=status.HTTP_201_CREATED)
def create_gender_types(item: GenderTypesCreate):
    try:
        created = add_gender_types(item)
        if created is None:
            raise HTTPException(status_code=503, detail="Database unavailable")
        return {"gender_types": created,
                "message": "Gender type added successfully"}
    except psycopg2.errors.UniqueViolation: #
        raise HTTPException(status_code=409, detail="Gender type already exists")
    except psycopg2.OperationalError: 
        raise HTTPException(status_code=503, detail="Database unavailable")
    except psycopg2.Error:
        raise HTTPException(status_code=500, detail="Database error occurred")

# 3.Customers k
# 4.Bookings k 
# 8.users k

#TODO: Endpoints: owners, location_treatments, bookings, users, businesses, customers

# 1.Treatments x
# 2.Treatment_categories x
# 3.Customers k
# 4.Bookings k 
# 5.Owners m
# 6.businesses m
# 7.business locations m
# 8.users k

# la till: employees m


# GET / POST 





# IMPLEMENT THE ACTUAL ENDPOINTS! Feel free to remove


# @app.get("/treatments")
# def read_treatments():
#     treatments = get_treatments()  # Funktionen hanterar connection internt
#     return {"treatments": treatments}  # Observera plural

## AI-exempel ##

# # I din db.py
# def get_all_treatments():
#     conn = get_connection()
#     if conn is None:
#         raise DatabaseConnectionError("Kunde inte ansluta till databasen")
    
#     try:
#         with conn:
#             with conn.cursor(cursor_factory=RealDictCursor) as cur:
#                 cur.execute("SELECT * FROM treatments")
#                 return cur.fetchall()  # fetchall() för alla treatments
#     except Exception as e:
#         raise DatabaseError(f"Kunde inte hämta behandlingar: {e}")

# @app.get("/treatments")
# def read_treatments():
#     conn = get_connection()
#     if conn is None:
#         raise HTTPException(status_code=500, detail="Database connection failed")
    
#     try:
#         treatments = get_all_treatments(conn)
#         return {"treatments": treatments}
#     finally:
#         conn.close()  # Viktigt att stänga!