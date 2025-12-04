CREATE TABLE IF NOT EXISTS users (
    user_ID SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    phone_number VARCHAR(255),
    date_of_birth DATE,
    gender VARCHAR(15) CHECK(gender IN ('Man', 'Kvinna', 'Icke-binär', 'Osäker', 'Vill ej svara', 'Annat')),
    profile_photo VARCHAR(255),
    balance INT NOT NULL DEFAULT 0,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS business(
    business_id SERIAL PRIMARY KEY,
    business_name VARCHAR(50) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    phone_number VARCHAR(255),
    profile_pic_url VARCHAR(255),
    address VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    about_text TEXT,
    number_of_employees SMALLINT
);

CREATE TABLE IF NOT EXISTS treatment_categories(
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS employees(
    employee_id SERIAL PRIMARY KEY,
	business_id INT NOT NULL REFERENCES business(business_id),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    rating SMALLINT CHECK(rating BETWEEN 1 AND 5),
    email VARCHAR(255) UNIQUE
);

CREATE TABLE IF NOT EXISTS treatments(
    treatment_id SERIAL PRIMARY KEY,
    business_id INT NOT NULL REFERENCES business(business_id),
    category_id INT NOT NULL REFERENCES treatment_categories(category_id),
    treatment_name VARCHAR(255) NOT NULL,
    treatment_description VARCHAR(255),
    price NUMERIC(10,2) NOT NULL,
    time_duration INT NOT NULL,
    last_min_deal BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS bookings(
    booking_id SERIAL PRIMARY KEY,
    treatment_id INT NOT NULL REFERENCES treatments(treatment_id),
    user_id INT NOT NULL REFERENCES users(user_id),
    business_id INT NOT NULL REFERENCES business(business_id),
    booked_date TIMESTAMP NOT NULL DEFAULT NOW(),
    booking_status VARCHAR(20) CHECK (booking_status IN('Bokad', 'Avbokad', 'Genomförd')),
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS titles(
    title_id SERIAL PRIMARY KEY,
    title_name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS employee_title(
    employee_title_id SERIAL PRIMARY KEY,
    employee_id INT NOT NULL REFERENCES employees(employee_id),
    title_id INT NOT NULL REFERENCES titles(title_id)
);

CREATE TABLE IF NOT EXISTS payment_methods(
    payment_method_id SERIAL PRIMARY KEY,
    method_name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS payments(
    user_id SERIAL PRIMARY KEY,
    business_id INT NOT NULL REFERENCES business(business_id),
    treatment_id INT NOT NULL REFERENCES treatments(treatment_id),
    payment_method_id INT NOT NULL REFERENCES payment_methods(payment_method_id),
    payment_date TIMESTAMP DEFAULT NOW()
);


CREATE TABLE IF NOT EXISTS opening_hours(
    opening_hour_id SERIAL PRIMARY KEY,
    business_id INT NOT NULL REFERENCES business(business_id),
    day_of_week INT NOT NULL CHECK(day_of_week BETWEEN 1 AND 7),
    open_time TIME NOT NULL,
    close_time TIME NOT NULL
);

CREATE TABLE IF NOT EXISTS favorites(
    favorite_id SERIAL PRIMARY KEY,
    treatment_id INT NOT NULL REFERENCES treatments(treatment_id),
    user_id INT NOT NULL REFERENCES users(user_id),
    business_id INT NOT NULL REFERENCES business(business_id),
    created_at TIMESTAMP DEFAULT NOW(),

    CONSTRAINT one_per_user UNIQUE (user_id, treatment_id)
    --Make sure a user cant add same treatment more than once
);

CREATE TABLE IF NOT EXISTS reviews(
	review_id SERIAL PRIMARY KEY,
	user_id INT NOT NULL REFERENCES users(user_id),
	employee_id INT NOT NULL REFERENCES employees(employee_id),
	business_id INT NOT NULL REFERENCES business(business_id),
	treatment_id INT NOT NULL REFERENCES treatments(treatment_id),
	review_comment TEXT,
	rating INT NOT NULL,
	created_at TIMESTAMP
);



