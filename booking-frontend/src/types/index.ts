export interface Treatment {
  treatment_id: number;
  category_id: number;  // Backend uses category_id, not treatment_category_id
  treatment_name: string;
  treatment_description: string;  // Backend uses treatment_description
  time_duration: number;  // Backend uses time_duration
  image_id?: number;
  last_min_deal: boolean;
  created_at?: string;
}

export interface TreatmentCategory {
  category_id: number;  // Backend uses category_id, not treatment_category_id
  category_name: string;
  description?: string;
  image_url?: string;
}

export interface Business {
  business_id: number;
  business_name: string;
  about_text?: string;  // Backend uses about_text
  website?: string;
  phone_number?: string;
  email?: string;
}

export interface BusinessLocation {
  location_id: number;
  business_id: number;
  street_address: string;  // Backend uses street_address
  city: string;
  postal_code: string;
  country: string;
  phone_number?: string;
  email?: string;
  longitude?: number;
  latitude?: number;
}

export interface User {
  user_id: number;
  first_name: string;
  last_name: string;
  email: string;
  phone_number?: string;
  gender_id?: number;
  date_of_birth?: string;
  profile_photo?: string;
}

export interface Customer {
  customer_id: number;
  user_id: number;
  balance?: number;
}

export interface Booking {
  booking_id: number;
  location_id: number;
  treatment_id: number;
  customer_id: number;
  employee_id?: number;
  business_id: number;
  booked_date: string;
  time_start: string;
  time_stop: string;
  notes?: string;
  booking_status: number;
  payment_confirmed: boolean;
}

export interface Employee {
  employee_id: number;
  user_id: number;
  business_id: number;
  location_id?: number;
  rating?: number;
}
