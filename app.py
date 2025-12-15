
import psycopg2
from db import (
    add_booking_statuses,
    add_bookings,
    add_business_locations,
    add_businesses,
    add_customers,
    add_employees,
    add_gender_types,
    add_owners,
    add_treatment_categories,
    add_treatments,
    add_users,
    delete_booking,
    delete_customer,
    delete_employee,
    delete_treatment,
    delete_user,
    get_bookings,
    get_business_locations,
    get_businesses,
    get_customers,
    get_employees,
    get_owners,
    get_treatment_categories,
    get_treatments,
    get_user_by_id,
    get_users,
    patch_booking_status,
    update_business,
    update_business_location,
    update_customer,
    update_user,
    update_treatment
)
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from schemas import (
    BookingsCreate,
    BookingStatusesCreate,
    BookingStatusPatch,
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

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
        raise HTTPException(status_code=409, detail="Treatment category already exists")
    except psycopg2.OperationalError: 
        raise HTTPException(status_code=503, detail="Database unavailable")
    except psycopg2.Error:
        raise HTTPException(status_code=500, detail="Database error occurred")
    
@app.get("/treatment_categories/")
def read_treatment_categories():
    treatment_categories = get_treatment_categories()
    if treatment_categories is None:
        raise HTTPException(status_code=404, detail="No treatment categories found")
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
    #TODO: Kolla upp hanteringen av error här. Detta är alternativ två.
    try:
        treatments = get_treatments()
        # if treatments is None:
            # raise HTTPException(status_code=404, detail="No treatments found")
        return {"treatments": treatments}
    except ConnectionError:
        raise HTTPException(status_code=503, detail="Database unavailable")
    except FileNotFoundError:
        HTTPException(status_code=404, detail="No treatments found")

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
    return {"customers": users}

@app.delete("/users/{user_id}")
def remove_user(user_id: int):
    try:
        deleted = delete_user(user_id)
        if deleted is None:
            raise HTTPException(status_code=404, detail="User not found")
        return {"deleted_user": deleted, "message": "User deleted successfully"}
    except psycopg2.errors.ForeignKeyViolation:
        raise HTTPException(status_code=409, detail="Cannot delete user because it is referenced by another table")
    except psycopg2.OperationalError:
        raise HTTPException(status_code=503, detail="Database unavailable")
    except psycopg2.Error:
        raise HTTPException(status_code=500, detail="Database error occurred")

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

# Create a new customer

@app.post("/customers/", status_code=status.HTTP_201_CREATED)
def create_customers(customer: CustomersCreate):
    try:
        created_customer = add_customers(customer)
        if created_customer is None:
            raise HTTPException(status_code=503, detail="Database unavailable")
        return {"customer": created_customer,
                "message": "Customer added successfully!"}
    except psycopg2.errors.ForeignKeyViolation:
        raise HTTPException(status_code=400, detail="Invalid user ID")
    except psycopg2.errors.UniqueViolation:
        raise HTTPException(status_code=409, detail="Customer already exists")
    except psycopg2.OperationalError: 
        raise HTTPException(status_code=503, detail="Database unavailable")
    except psycopg2.Error:
        raise HTTPException(status_code=500, detail="Database error occurred")
    
# Get a customer

@app.get("/customers/")
def read_customers():
    customers = get_customers()
    if customers is None:
        raise HTTPException(status_code=404, detail="User no found")
    return {"customers": customers}

# Get a user by ID

@app.get("/users/{user_id}")
def read_user(user_id: int):
    user = get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="No user found with this ID")
    return {"users": user}

# Update user

@app.put("/users/{user_id}")
def put_user(user_id: int, user: UsersCreate):
    try:
        updated = update_user(user_id, user)
        if updated is None:
            raise HTTPException(status_code=404, detail="User not found")
        return updated
    except psycopg2.errors.ForeignKeyViolation:
        raise HTTPException(status_code=400, detail="Invalid gender ID")
    except psycopg2.errors.UniqueViolation:
        raise HTTPException(status_code=409, detail="Email already exists")
    except psycopg2.OperationalError:
        raise HTTPException(status_code=503, detail="Database unavailable")
    except psycopg2.Error:
        raise HTTPException(status_code=500, detail="Database error occurred")

# Update customer

@app.put("/customers/{customer_id}")
def put_customer(customer_id: int, customer: CustomersCreate):
    try:
        updated = update_customer(customer_id, customer)
        if updated is None:
            raise HTTPException(status_code=404, detail="Customer not found")
        return updated
    except psycopg2.errors.ForeignKeyViolation:
        raise HTTPException(status_code=400, detail="Invalid user ID")
    except psycopg2.errors.UniqueViolation:
        raise HTTPException(status_code=409, detail="Customer already exists for this user")
    except psycopg2.errors.NumericValueOutOfRange:
        raise HTTPException(status_code=400, detail="Balance value is too large")
    except psycopg2.OperationalError:
        raise HTTPException(status_code=503, detail="Database unavailable")

# Add Booking Status
#TODO: Kanske att denna ska hardcodeas? Ska man behöva lägga till statusar? Sqamma med blad annat genders, Kika detta

@app.post("/booking_statuses/", status_code=status.HTTP_201_CREATED)
def create_booking_status(booking_status: BookingStatusesCreate,
):
    try:
        booking_statuses = add_booking_statuses(booking_status)
        if booking_statuses is None:
            raise HTTPException(status_code=503, detail="Database unavailable")
        return {"booking_statuses": booking_statuses,
                "message": "Booking status added successfully!"}
    except psycopg2.errors.ForeignKeyViolation:
        raise HTTPException(status_code=400, detail="Invalid ID")
    except psycopg2.errors.UniqueViolation:
        raise HTTPException(status_code=409, detail="Booking status already exists")
    except psycopg2.OperationalError: 
        raise HTTPException(status_code=503, detail="Database unavailable")
    except psycopg2.Error:
        raise HTTPException(status_code=500, detail="Database error occurred")

# Add Booking

@app.post("/bookings/", status_code=status.HTTP_201_CREATED)
def create_booking(booking: BookingsCreate):
    try:
        bookings = add_bookings(booking)
        if bookings is None:
            raise HTTPException(status_code=503, detail="Database unavailable")
        return {"bookings": bookings,
                "message": "Booking added successfully!"}
    except psycopg2.errors.ForeignKeyViolation:
        raise HTTPException(status_code=400, detail="Invalid ID")
    except psycopg2.errors.UniqueViolation:
        raise HTTPException(status_code=409, detail="Booking already exists")
    except psycopg2.OperationalError: 
        raise HTTPException(status_code=503, detail="Database unavailable")
    except psycopg2.Error:
        raise HTTPException(status_code=500, detail="Database error occurred")


# Get a booking by booking id

@app.get("/bookings/{booking_id}")
def read_booking(booking_id: int):
    bookings = get_bookings(booking_id)
    if bookings is None:
        raise HTTPException(status_code=404, detail="No booking found for this ID")
    return {"bookings": bookings}

#Update Business bu id

@app.put("/businesses/{business_id}")
def put_business(business_id: int,businesses: BusinessCreate):
    try:
        updated = update_business(business_id, businesses)
        if updated is None:
            raise HTTPException(status_code=404, detail="Business not found")
        return updated
    except psycopg2.errors.ForeignKeyViolation:
        raise HTTPException(status_code=400, detail="Invalid business ID")
    except psycopg2.OperationalError:
        raise HTTPException(status_code=503, detail="Database unavailable")
    except psycopg2.errors.UniqueViolation:
        raise HTTPException(status_code=409, detail="Business already exists")
    except psycopg2.Error:
        raise HTTPException(status_code=500, detail="Database error occurred")

# Update business location

@app.put("/business_locations/{location_id}")
def put_business_locations(location_id: int,business_locations: BusinessLocationsCreate):
    try:
        updated = update_business_location(location_id, business_locations)
        if updated is None:
            raise HTTPException(status_code=404, detail="Business location not found")
        return updated
    except psycopg2.errors.ForeignKeyViolation:
        raise HTTPException(status_code=400, detail="Invalid ID")
    except psycopg2.OperationalError:
        raise HTTPException(status_code=503, detail="Database unavailable")
    except psycopg2.Error:
        raise HTTPException(status_code=500, detail="Database error occurred")


@app.delete("/customers/{customer_id}")
def remove_customer(customer_id: int):
    try:
        deleted = delete_customer(customer_id)
        if deleted is None:
            raise HTTPException(status_code=404, detail="Customer not found")
        return {
            "deleted_customer": deleted,
            "message": "Customer deleted successfully"
        }
    except psycopg2.errors.ForeignKeyViolation:
        raise HTTPException(
            status_code=409,
            detail="Cannot delete customer because it is referenced by another table"
        )
    except psycopg2.OperationalError:
        raise HTTPException(status_code=503, detail="Database unavailable")
    except psycopg2.Error:
        raise HTTPException(status_code=500, detail="Database error occurred")
    
@app.delete("/treatments/{treatment_id}")
def delete_treatment_endpoint(treatment_id: int):
    try:
        deleted = delete_treatment(treatment_id)
        if deleted is None:
            raise HTTPException(status_code=404, detail="Treatment not found")
        return deleted
    except psycopg2.errors.ForeignKeyViolation:
        raise HTTPException(status_code=409, detail="Cannot delete treatment because it is referenced by other records")
    except psycopg2.OperationalError:
        raise HTTPException(status_code=503, detail="Database unavailable")
    except psycopg2.Error:
        raise HTTPException(status_code=500, detail="Database error occurred")
    
@app.delete("/bookings/{booking_id}")
def delete_booking_endpoint(booking_id: int):
    try:
        deleted = delete_booking(booking_id)
        if deleted is None:
            raise HTTPException(status_code=404, detail="Booking not found")
        return deleted
    except psycopg2.errors.ForeignKeyViolation:
        raise HTTPException(status_code=409, detail="Cannot delete booking because it is referenced")
    except psycopg2.OperationalError:
        raise HTTPException(status_code=503, detail="Database unavailable")
    except psycopg2.Error:
        raise HTTPException(status_code=500, detail="Database error occurred")
    
@app.delete("/employees/{employee_id}")
def delete_employee_endpoint(employee_id: int):
    try:
        deleted = delete_employee(employee_id)
        if deleted is None:
            raise HTTPException(status_code=404, detail="Employee not found")
        return deleted
    except psycopg2.errors.ForeignKeyViolation:
        raise HTTPException(status_code=409, detail="Cannot delete employee because it is referenced")
    except psycopg2.OperationalError:
        raise HTTPException(status_code=503, detail="Database unavailable")
    except psycopg2.Error:
        raise HTTPException(status_code=500, detail="Database error occurred")
    
@app.patch("/bookings/{booking_id}/status")
def patch_booking_status_endpoint(booking_id: int, status: BookingStatusPatch):
    try:
        updated = patch_booking_status(booking_id, status.booking_status)
        if updated is None:
            raise HTTPException(status_code=404, detail="Booking not found")
        return updated
    except psycopg2.errors.ForeignKeyViolation:
        raise HTTPException(status_code=400, detail="Invalid booking status")
    except psycopg2.OperationalError:
        raise HTTPException(status_code=503, detail="Database unavailable")

@app.put("/treatments/{treatment_id}")
def put_treatments(treatment_id: int,treatment: TreatmentsCreate):
    try:
        updated = update_treatment(treatment_id, treatment)
        if updated is None:
            raise HTTPException(status_code=404, detail="Treatment not found")
        return updated
    except psycopg2.errors.ForeignKeyViolation:
        raise HTTPException(status_code=400, detail="Invalid business ID")
    except psycopg2.OperationalError:
        raise HTTPException(status_code=503, detail="Database unavailable")
    except psycopg2.errors.UniqueViolation:
        raise HTTPException(status_code=409, detail="Treatment already exists")
    except psycopg2.Error:
        raise HTTPException(status_code=500, detail="Database error occurred")