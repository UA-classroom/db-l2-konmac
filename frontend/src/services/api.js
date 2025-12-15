import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Treatments
export const getTreatments = () => api.get('/treatments/');
export const createTreatment = (data) => api.post('/treatments/', data);
export const updateTreatment = (id, data) => api.put(`/treatments/${id}`, data);
export const deleteTreatment = (id) => api.delete(`/treatments/${id}`);

// Treatment Categories
export const getTreatmentCategories = () => api.get('/treatment_categories/');
export const createTreatmentCategory = (data) => api.post('/treatment_categories/', data);

// Users
export const getUsers = () => api.get('/users/');
export const getUserById = (id) => api.get(`/users/${id}`);
export const createUser = (data) => api.post('/users/', data);
export const updateUser = (id, data) => api.put(`/users/${id}`, data);
export const deleteUser = (id) => api.delete(`/users/${id}`);

// Customers
export const getCustomers = () => api.get('/customers/');
export const createCustomer = (data) => api.post('/customers/', data);
export const updateCustomer = (id, data) => api.put(`/customers/${id}`, data);
export const deleteCustomer = (id) => api.delete(`/customers/${id}`);

// Businesses
export const getBusinesses = () => api.get('/businesses/');
export const createBusiness = (data) => api.post('/businesses/', data);
export const updateBusiness = (id, data) => api.put(`/businesses/${id}`, data);

// Business Locations
export const getBusinessLocations = () => api.get('/business_locations/');
export const createBusinessLocation = (data) => api.post('/business_locations/', data);
export const updateBusinessLocation = (id, data) => api.put(`/business_locations/${id}`, data);

// Employees
export const getEmployees = () => api.get('/employees/');
export const createEmployee = (data) => api.post('/employees/', data);
export const deleteEmployee = (id) => api.delete(`/employees/${id}`);

// Owners
export const getOwners = () => api.get('/owners/');
export const createOwner = (data) => api.post('/owners/', data);

// Bookings
export const getBooking = (id) => api.get(`/bookings/${id}`);
export const createBooking = (data) => api.post('/bookings/', data);
export const updateBookingStatus = (id, status) => api.patch(`/bookings/${id}/status`, { booking_status: status });
export const deleteBooking = (id) => api.delete(`/bookings/${id}`);

// Booking Statuses
export const createBookingStatus = (data) => api.post('/booking_statuses/', data);

// Gender Types
export const createGenderType = (data) => api.post('/gender_types/', data);

export default api;