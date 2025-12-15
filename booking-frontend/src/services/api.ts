import axios from 'axios';
import type {
  Treatment,
  TreatmentCategory,
  Business,
  BusinessLocation,
  User,
  Customer,
  Booking,
  Employee,
} from '../types';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Treatment Categories
export const getTreatmentCategories = () =>
  api.get<{ treatment_categories: TreatmentCategory[] }>('/treatment_categories/');

export const createTreatmentCategory = (data: Omit<TreatmentCategory, 'treatment_category_id'>) =>
  api.post<{ treatment_category: TreatmentCategory }>('/treatment_categories/', data);

// Treatments
export const getTreatments = () =>
  api.get<{ treatments: Treatment[] }>('/treatments/');

export const createTreatment = (data: Omit<Treatment, 'treatment_id'>) =>
  api.post<{ treatments: Treatment }>('/treatments/', data);

export const updateTreatment = (id: number, data: Omit<Treatment, 'treatment_id'>) =>
  api.put<Treatment>(`/treatments/${id}`, data);

export const deleteTreatment = (id: number) =>
  api.delete(`/treatments/${id}`);

// Businesses
export const getBusinesses = () =>
  api.get<{ businesses: Business[] }>('/businesses/');

export const createBusiness = (data: Omit<Business, 'business_id'>) =>
  api.post<{ businesses: Business }>('/businesses/', data);

export const updateBusiness = (id: number, data: Omit<Business, 'business_id'>) =>
  api.put<Business>(`/businesses/${id}`, data);

// Business Locations
export const getBusinessLocations = () =>
  api.get<{ business_locations: BusinessLocation[] }>('/business_locations/');

export const createBusinessLocation = (data: Omit<BusinessLocation, 'location_id'>) =>
  api.post<{ business_locations: BusinessLocation }>('/business_locations/', data);

export const updateBusinessLocation = (id: number, data: Omit<BusinessLocation, 'location_id'>) =>
  api.put<BusinessLocation>(`/business_locations/${id}`, data);

// Users
export const getUsers = () =>
  api.get<{ customers: User[] }>('/users/');

export const getUserById = (id: number) =>
  api.get<{ users: User }>(`/users/${id}`);

export const createUser = (data: Omit<User, 'user_id'>) =>
  api.post<{ users: User }>('/users/', data);

export const updateUser = (id: number, data: Omit<User, 'user_id'>) =>
  api.put<User>(`/users/${id}`, data);

export const deleteUser = (id: number) =>
  api.delete(`/users/${id}`);

// Customers
export const getCustomers = () =>
  api.get<{ customers: Customer[] }>('/customers/');

export const createCustomer = (data: Omit<Customer, 'customer_id'>) =>
  api.post<{ customer: Customer }>('/customers/', data);

export const updateCustomer = (id: number, data: Omit<Customer, 'customer_id'>) =>
  api.put<Customer>(`/customers/${id}`, data);

export const deleteCustomer = (id: number) =>
  api.delete(`/customers/${id}`);

// Bookings
export const getBooking = (id: number) =>
  api.get<{ bookings: Booking }>(`/bookings/${id}`);

export const createBooking = (data: Omit<Booking, 'booking_id'>) =>
  api.post<{ bookings: Booking }>('/bookings/', data);

export const deleteBooking = (id: number) =>
  api.delete(`/bookings/${id}`);

export const patchBookingStatus = (id: number, status: number) =>
  api.patch<Booking>(`/bookings/${id}/status`, { booking_status: status });

// Employees
export const getEmployees = () =>
  api.get<{ employees: Employee[] }>('/employees/');

export const createEmployee = (data: Omit<Employee, 'employee_id'>) =>
  api.post<{ employees: Employee }>('/employees/', data);

export const deleteEmployee = (id: number) =>
  api.delete(`/employees/${id}`);

export default api;
