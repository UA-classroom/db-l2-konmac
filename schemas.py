# Add Pydantic schemas here that you'll use in your routes / endpoints
# Pydantic schemas are used to validate data that you receive, or to make sure that whatever data
# you send back to the client follows a certain structure


from pydantic import BaseModel
from datetime import date, datetime


class TreatmentsCreate(BaseModel):
    treatment_name: str
    treatment_description: str | None = None
    category_id: int
    time_duration: int
    last_min_deal: bool

class TreatmentCategoriesCreate(BaseModel):
    category_name: str


class CustomersCreate(BaseModel):
    user_id: int
    balance: float | None = None

class BusinessCreate(BaseModel):
    business_name: str
    email: str
    phone_number: str | None = None
    about_text: str | None  = None
    # number_of_employees: int | None = None
    #TODO: Kanske ta bort number of employees då detta utvinnns från employees på samma business ändå.

class BusinessLocationsCreate(BaseModel):
    phone_number: str
    business_id: int
    email: str
    street_address: str
    city: str
    postal_code: str
    country: str
    longitude: float | None = None
    latitude: float | None = None

class OwnersCreate(BaseModel):
    business_id: int
    user_id: int

class EmployeesCreate(BaseModel):
    user_id: int
    business_id: int
    location_id: int
    rating: float | None = None

class UsersCreate(BaseModel):
    email: str
    password: str
    first_name: str | None = None
    last_name: str | None = None
    phone_number: str | None = None
    date_of_birth: date | None = None
    gender_id: int

class GenderTypesCreate(BaseModel):
    gender_types: str

class BookingStatusesCreate(BaseModel):
    status_name: str

class BookingsCreate(BaseModel):
    location_id: int
    treatment_id: int
    customer_id: int
    employee_id: int
    business_id: int
    booked_date: date
    time_start: datetime
    time_stop: datetime
    notes: str | None = None
    booking_status: int
    payment_confirmed: bool

class BookingStatusPatch(BaseModel):
    booking_status: int