# Add Pydantic schemas here that you'll use in your routes / endpoints
# Pydantic schemas are used to validate data that you receive, or to make sure that whatever data
# you send back to the client follows a certain structure


from pydantic import BaseModel


class TreatmentsCreate(BaseModel):
    treatment_name: str
    treatment_description: str | None = None
    category_id: int
    time_duration: int
    last_min_deal: bool

class TreatmentCategoriesCreate(BaseModel):
    category_name: str

class ImagesCreate(BaseModel):
    pass

class BookingsCreate(BaseModel):
    pass

class UsersCreate(BaseModel):
    email: str
    password: str
    first_name: str | None = None
    last_name: str | None = None
    phone_number: str | None = None
    date_of_birth: str | None = None
    created_at: str


class Customer(BaseModel):
    balance: float | None = None

class BusinessCreate(BaseModel):
    business_name: str
    email: str
    phone_number: str | None = None
    about_text: str | None  = None
    number_of_employees: int | None = None

class BusinessLocationsCreate(BaseModel):
    phone_number: str
    email: str
    street_address: str
    city: str
    postal_code: str
    country: str
    longitude: float
    latitude: float

