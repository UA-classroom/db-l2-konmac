
import psycopg2
from db import (
    add_treatment_categories,
    add_treatments,
    get_treatment_categories,
    get_treatments,
)
from fastapi import FastAPI, HTTPException
from schemas import TreatmentCategoriesCreate, TreatmentsCreate

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

### 1. Create a new treatment
@app.post("/treatments/")
def create_treatment(treatment: TreatmentsCreate):
    try:
        treatments = add_treatments(treatment)
        return {"treatments": treatments,
                "message": "Treatment added successfuly"}
    except psycopg2.errors.ForeignKeyViolation:
        raise HTTPException(status_code=400, detail="Invalid category ID")
    except psycopg2.errors.UniqueViolation:
        raise HTTPException(status_code=409, detail="Treatment already exists")
    except psycopg2.OperationalError: 
        raise HTTPException(status_code=503, detail="Database unavailable")
    except psycopg2.Error:
        raise HTTPException(status_code=500, detail="Database error occurred")


### 2. Create a new treatment category
@app.post("/treatment_categories/")
def create_treatment_categories(treatment_category: TreatmentCategoriesCreate):
    treatment_categories = add_treatment_categories(treatment_category)
    return {"treatments": treatment_categories,
            "message": "Treatment category created successfuly"}

### 3. Get all treatments
@app.get("/treatments/")
def read_treatment():
    treatments = get_treatments()
    return {"treatments": treatments}

### 4. Get all treatment categories
@app.get("/treatments_categories/")
def read_treatment_categories():
    treatments_categories = get_treatment_categories()
    return {"treatment_categories": treatments_categories}



#TODO: Endpoints: owners, location_treatments, bookings, users, businesses, customers

# 1.Treatments x
# 2.Treatment_categories x
# 3.Customers k
# 4.Bookings k 
# 5.Owners m
# 6.businesses m
# 7.location_treatments m
# 8.users k


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