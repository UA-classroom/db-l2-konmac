DROP TABLE IF EXISTS employee_pricing CASCADE;
DROP TABLE IF EXISTS employee_time_slots CASCADE;
DROP TABLE IF EXISTS employee_specializations CASCADE;
DROP TABLE IF EXISTS locations_employees CASCADE;
DROP TABLE IF EXISTS opening_hours CASCADE;
DROP TABLE IF EXISTS business_service_categories CASCADE;
DROP TABLE IF EXISTS owners CASCADE;
DROP TABLE IF EXISTS employee_treatments CASCADE;
DROP TABLE IF EXISTS location_treatments CASCADE;
DROP TABLE IF EXISTS ticket_attachment CASCADE;
DROP TABLE IF EXISTS support_messages CASCADE;
DROP TABLE IF EXISTS support_tickets CASCADE;
DROP TABLE IF EXISTS support_agents CASCADE;
DROP TABLE IF EXISTS notifications CASCADE;
DROP TABLE IF EXISTS payment_attempts CASCADE;
DROP TABLE IF EXISTS refunds CASCADE;
DROP TABLE IF EXISTS payments CASCADE;
DROP TABLE IF EXISTS gift_cards CASCADE;
DROP TABLE IF EXISTS favorites CASCADE;
DROP TABLE IF EXISTS reviews CASCADE;
DROP TABLE IF EXISTS bookings CASCADE;
DROP TABLE IF EXISTS treatments CASCADE;
DROP TABLE IF EXISTS images CASCADE;
DROP TABLE IF EXISTS employees CASCADE;
DROP TABLE IF EXISTS business_locations CASCADE;
DROP TABLE IF EXISTS specializations CASCADE;
DROP TABLE IF EXISTS service_categories CASCADE;
DROP TABLE IF EXISTS sender_types CASCADE;
DROP TABLE IF EXISTS support_ticket_statuses CASCADE;
DROP TABLE IF EXISTS failed_statuses CASCADE;
DROP TABLE IF EXISTS payment_methods CASCADE;
DROP TABLE IF EXISTS payment_statuses CASCADE;
DROP TABLE IF EXISTS refund_statuses CASCADE;
DROP TABLE IF EXISTS booking_statuses CASCADE;
DROP TABLE IF EXISTS customers CASCADE;
DROP TABLE IF EXISTS treatment_categories CASCADE;
DROP TABLE IF EXISTS businesses CASCADE;
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS gender_types CASCADE;

CREATE TABLE gender_types (
    gender_id SERIAL PRIMARY KEY,
    gender_types VARCHAR(255)
);

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    phone_number VARCHAR(20),
    date_of_birth DATE,
    gender_id INT NOT NULL REFERENCES gender_types(gender_id),
    profile_photo VARCHAR(200),
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);


CREATE TABLE businesses(
    business_id SERIAL PRIMARY KEY,
    business_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone_number VARCHAR(30),
    about_text TEXT,
    number_of_employees SMALLINT
);

CREATE TABLE treatment_categories (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users(user_id),
    balance NUMERIC(10,2) NOT NULL DEFAULT 0
);

CREATE TABLE booking_statuses (
    booking_status_id SERIAL PRIMARY KEY,
    status_name VARCHAR(20) UNIQUE NOT NULL
);

CREATE TABLE refund_statuses (
    refund_status_id SERIAL PRIMARY KEY,
    status VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE payment_statuses (
    payment_status_id SERIAL PRIMARY KEY,
    status_name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE payment_methods (
    payment_method_id SERIAL PRIMARY KEY,
    method_name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE failed_statuses (
    failed_status_id SERIAL PRIMARY KEY,
    status_name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE support_ticket_statuses (
    status_id SERIAL PRIMARY KEY,
    status_name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE sender_types (
    sender_type_id SERIAL PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL UNIQUE,
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE service_categories(
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(255) NOT NULL
);

CREATE TABLE specializations(
    specialization_id SERIAL PRIMARY KEY,
    specialization_name VARCHAR(250) NOT NULL
);

CREATE TABLE business_locations(
    location_id SERIAL PRIMARY KEY,
    business_id INT NOT NULL,
    phone_number VARCHAR(30) NOT NULL,
    email VARCHAR(100) NOT NULL,
    street_address VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    postal_code VARCHAR(10) NOT NULL,
    country VARCHAR(50) NOT NULL,
    longitude DECIMAL(10,8),
    latitude DECIMAL(10,8),
    FOREIGN KEY (business_id) REFERENCES businesses(business_id)
);

CREATE TABLE employees(
    employee_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users(user_id),
    business_id INT NOT NULL REFERENCES businesses(business_id),
    location_id INT NOT NULL REFERENCES business_locations(location_id),
    rating SMALLINT CHECK (rating BETWEEN 1 AND 5)
);

CREATE TABLE images (
    image_id SERIAL PRIMARY KEY,
    business_id INT REFERENCES businesses(business_id),
    employee_id INT REFERENCES employees(employee_id),
    location_id INT REFERENCES business_locations(location_id),
    image_url VARCHAR(255) NOT NULL
);

CREATE TABLE treatments (
    treatment_id SERIAL PRIMARY KEY,
    treatment_name VARCHAR(255) NOT NULL,
    treatment_description TEXT,
    category_id INT REFERENCES treatment_categories(category_id),
    image_id INT REFERENCES images(image_id),
    time_duration INT NOT NULL,
    last_min_deal BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE bookings (
    booking_id SERIAL PRIMARY KEY,
    location_id INT NOT NULL REFERENCES business_locations(location_id),
    treatment_id INT NOT NULL REFERENCES treatments(treatment_id),
    customer_id INT NOT NULL REFERENCES customers(customer_id),
    employee_id INT NOT NULL REFERENCES employees(employee_id),
    business_id INT NOT NULL REFERENCES businesses(business_id),
    booked_date DATE NOT NULL,
    time_start TIME NOT NULL,
    time_stop TIME NOT NULL,
    notes TEXT,
    booking_status INT NOT NULL REFERENCES booking_statuses(booking_status_id),
    payment_confirmed BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY,
    booking_id INT NOT NULL REFERENCES bookings(booking_id),
    customer_id INT NOT NULL REFERENCES customers(customer_id),
    employee_id INT REFERENCES employees(employee_id),
    location_id INT NOT NULL REFERENCES business_locations(location_id),
    treatment_id INT REFERENCES treatments(treatment_id),
    overall_rating INT CHECK (overall_rating BETWEEN 1 AND 5),
    location_rating INT CHECK (location_rating BETWEEN 1 AND 5),
    employee_rating INT CHECK (employee_rating BETWEEN 1 AND 5),
    treatment_rating INT CHECK (treatment_rating BETWEEN 1 AND 5),
    review_comment TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    UNIQUE (booking_id, customer_id)
);

CREATE TABLE favorites (
    favorite_id SERIAL PRIMARY KEY,
    treatment_id INT REFERENCES treatments(treatment_id),
    customer_id INT NOT NULL REFERENCES customers(customer_id),
    location_id INT REFERENCES business_locations(location_id),
    employee_id INT REFERENCES employees(employee_id),
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE gift_cards (
    gift_card_id SERIAL PRIMARY KEY,
    gift_card_code VARCHAR(50) UNIQUE NOT NULL,
    purchaser_id INT NOT NULL REFERENCES customers(customer_id),
    gift_card_amount NUMERIC(6,2) NOT NULL,
    remaining_balance NUMERIC(6,2) NOT NULL,
    purchase_date TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL REFERENCES customers(customer_id),
    location_id INT NOT NULL REFERENCES business_locations(location_id),
    booking_id INT NOT NULL REFERENCES bookings(booking_id),
    payment_method_id INT NOT NULL REFERENCES payment_methods(payment_method_id),
    amount NUMERIC(10,2) NOT NULL,
    payment_status_id INT NOT NULL REFERENCES payment_statuses(payment_status_id),
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    UNIQUE (booking_id, payment_method_id)
);

CREATE TABLE refunds (
    refund_id SERIAL PRIMARY KEY,
    payment_id INT NOT NULL REFERENCES payments(payment_id),
    amount NUMERIC(10,2) NOT NULL,
    reason TEXT,
    refund_status_id INT NOT NULL REFERENCES refund_statuses(refund_status_id),
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE payment_attempts (
    attempt_id SERIAL PRIMARY KEY,
    booking_id INT NOT NULL REFERENCES bookings(booking_id),
    customer_id INT NOT NULL REFERENCES customers(customer_id),
    amount NUMERIC(10,2) NOT NULL,
    payment_method_id INT NOT NULL REFERENCES payment_methods(payment_method_id),
    failed_attempt_status_id INT NOT NULL REFERENCES failed_statuses(failed_status_id),
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE notifications (
    notification_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    business_id INT REFERENCES businesses(business_id),
    employee_id INT REFERENCES employees(employee_id),
    notification_type VARCHAR(50) NOT NULL,
    title VARCHAR(255),
    message TEXT,
    is_read BOOLEAN NOT NULL DEFAULT FALSE,
    read_at TIMESTAMP,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE support_agents (
    agent_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users(user_id),
    department VARCHAR(50)
);

CREATE TABLE support_tickets (
    ticket_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL REFERENCES customers(customer_id),
    agent_id INT REFERENCES support_agents(agent_id),
    status_id INT NOT NULL REFERENCES support_ticket_statuses(status_id),
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE support_messages (
    message_id SERIAL PRIMARY KEY,
    ticket_id INT NOT NULL REFERENCES support_tickets(ticket_id),
    sender_id INT NOT NULL REFERENCES users(user_id),
    sender_type_id INT NOT NULL REFERENCES sender_types(sender_type_id),
    message TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE ticket_attachment (
    attachment_id SERIAL PRIMARY KEY,
    message_id INT NOT NULL REFERENCES support_messages(message_id),
    file_url VARCHAR(255) NOT NULL,
    uploaded_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE location_treatments(
    location_id INT NOT NULL REFERENCES business_locations(location_id),
    treatment_id INT NOT NULL REFERENCES treatments(treatment_id)
);

CREATE TABLE employee_treatments(
    employee_treatment_id SERIAL PRIMARY KEY,
    treatment_id INT NOT NULL REFERENCES treatments(treatment_id),
    employee_id INT NOT NULL REFERENCES employees(employee_id)
);

CREATE TABLE owners(
    owner_id SERIAL PRIMARY KEY,
    business_id INT NOT NULL REFERENCES businesses(business_id),
    user_id INT NOT NULL REFERENCES users(user_id)
);

CREATE TABLE business_service_categories(
    business_id INT NOT NULL REFERENCES businesses(business_id),
    category_id INT NOT NULL REFERENCES service_categories(category_id)
);

CREATE TABLE opening_hours(
    opening_hour_id SERIAL PRIMARY KEY,
    location_id INT NOT NULL REFERENCES business_locations(location_id),
    day_of_week INT NOT NULL,
    open_time TIME NOT NULL,
    close_time TIME NOT NULL
);

CREATE TABLE locations_employees(
    employee_id INT NOT NULL REFERENCES employees(employee_id),
    location_id INT NOT NULL REFERENCES business_locations(location_id)
);

CREATE TABLE employee_specializations(
    employee_id INT NOT NULL REFERENCES employees(employee_id),
    specialization_id INT NOT NULL REFERENCES specializations(specialization_id)
);

CREATE TABLE employee_time_slots(
    timeslot_id SERIAL PRIMARY KEY,
    employee_id INT NOT NULL REFERENCES employees(employee_id),
    slot_day DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    is_booked BOOLEAN
);

CREATE TABLE employee_pricing(
    pricing_id SERIAL PRIMARY KEY,
    employee_id INT NOT NULL REFERENCES employees(employee_id),
    treatment_id INT NOT NULL REFERENCES treatments(treatment_id),
    location_id INT NOT NULL REFERENCES business_locations(location_id),
    price_per_hour numeric(10,2) NOT NULL,
    UNIQUE (employee_id, treatment_id, location_id)
);