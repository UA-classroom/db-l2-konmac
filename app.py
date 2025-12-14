
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
    get_user_by_id,
    update_user,
    add_gender_types,
    add_customers,
    get_customers,
    update_customer,
    add_booking_statuses,
    add_bookings,
    get_bookings,
    update_business,
    update_business_location

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
    GenderTypesCreate,
    CustomersCreate,
    BookingStatusesCreate,
    BookingsCreate
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


# Treatment categories

@app.post("/treatment_categories/", status_code=status.HTTP_201_CREATED)
def create_treatment_categories(treatment_category: TreatmentCategoriesCreate):
    try:
        treatment_categories = add_treatment_categories(treatment_category)
        if treatment_categories is None:
            raise HTTPException(status_code=503, detail="Database unavailable")
        #TODO: Vid närmare eftertanke känns denna felkoden fel. Databasen är avalieble, men inget värde har returnerats. Borde kanske vara 404 Not found?
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
    return {"customers": users}

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
        raise HTTPException(status_code=503, detail="Database unavailable")
    return {"customers": customers}

# Get a user by ID

@app.get("/users/{user_id}")
def read_user(user_id: int):
    user = get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=503, detail="Database unavailable")
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
    #TODO: Känns ologiskt även här då det är en update
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
    #TODO: "Already exists känns fel på en update, kolla detta"
    except psycopg2.OperationalError:
        raise HTTPException(status_code=503, detail="Database unavailable")
    except psycopg2.Error:
        raise HTTPException(status_code=500, detail="Database error occurred")

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
        raise HTTPException(status_code=503, detail="Database unavailable")
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
    
#TODO: Lägg till delete-endponts