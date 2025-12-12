
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



# INSPIRATION FOR A LIST-ENDPOINT - Not necessary to use pydantic models, but we could to ascertain that we return the correct values
@app.get("/treatments/")
def read_treatment():
    treatments = get_treatments()
    return {"treatments": treatments}

@app.get("/treatments_categories/")
def read_treatment_categories():
    treatments_categories = get_treatment_categories()
    return {"treatment_categories": treatments_categories}


# INSPIRATION FOR A POST-ENDPOINT, uses a pydantic model to validate
@app.post("/treatments/")
def create_treatment(treatment: TreatmentsCreate):
    try:
        treatments = add_treatments(treatment)
        return {"treatments": treatments}
    except psycopg2.errors.ForeignKeyViolation:
        raise HTTPException(status_code=404, detail="Wrong id sucker")
    


@app.post("/treatment_categories/")
def create_treatment_categories(treatment_category: TreatmentCategoriesCreate):
    treatment_categories = add_treatment_categories(treatment_category)
    return {"treatments": treatment_categories}



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