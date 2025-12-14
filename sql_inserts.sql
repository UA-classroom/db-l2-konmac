-- =========================
-- LOOKUP / REFERENSTABELLER
-- =========================

INSERT INTO gender_types (gender_types) VALUES
  ('Male'),
  ('Female'),
  ('Other'),
  ('Prefer not to say'),
  ('Non-binary');

INSERT INTO booking_statuses (status_name) VALUES
  ('pending'),
  ('confirmed'),
  ('cancelled'),
  ('completed'),
  ('no_show');

INSERT INTO refund_statuses (status) VALUES
  ('requested'),
  ('approved'),
  ('rejected');

INSERT INTO payment_statuses (status_name) VALUES
  ('pending'),
  ('paid'),
  ('failed'),
  ('refunded');

INSERT INTO payment_methods (method_name) VALUES
  ('card'),
  ('cash'),
  ('bank_transfer'),
  ('wallet');

INSERT INTO failed_statuses (status_name) VALUES
  ('insufficient_funds'),
  ('provider_error'),
  ('invalid_method');

INSERT INTO support_ticket_statuses (status_name) VALUES
  ('open'),
  ('in_progress'),
  ('closed');

INSERT INTO sender_types (type_name, is_active) VALUES
  ('customer', TRUE),
  ('agent', TRUE),
  ('system', TRUE);

INSERT INTO service_categories (category_name) VALUES
  ('Hair'),
  ('Nails'),
  ('Massage');

INSERT INTO specializations (specialization_name) VALUES
  ('Haircut'),
  ('Coloring'),
  ('Thai massage');

INSERT INTO treatment_categories (category_name) VALUES
  ('Haircuts'),
  ('Coloring'),
  ('Massage'),
  ('Nails'),
  ('Skincare'),
  ('Brows & Lashes');

-- =========================
-- KÄRNTABELLER (5–10 rader)
-- =========================

-- USERS (10)
INSERT INTO users (email, password, first_name, last_name, phone_number, date_of_birth, gender_id, profile_photo, created_at) VALUES
  ('alice@example.com',  'hashed_pw_1', 'Alice',  'Ng',      '+66-801-111-111', '1997-02-11', 2, NULL, NOW()),
  ('bob@example.com',    'hashed_pw_2', 'Bob',    'Kowalski','+66-802-222-222', '1995-08-20', 1, NULL, NOW()),
  ('carla@example.com',  'hashed_pw_3', 'Carla',  'Svensson','+66-803-333-333', '1999-01-05', 2, NULL, NOW()),
  ('david@example.com',  'hashed_pw_4', 'David',  'Chen',   '+66-804-444-444', '1992-11-30', 1, NULL, NOW()),
  ('emma@example.com',   'hashed_pw_5', 'Emma',   'Nowak',  '+66-805-555-555', '2000-06-17', 2, NULL, NOW()),
  ('frank@example.com',  'hashed_pw_6', 'Frank',  'Larsson','+66-806-666-666', '1991-03-22', 1, NULL, NOW()),
  ('gina@example.com',   'hashed_pw_7', 'Gina',   'Patel',  '+66-807-777-777', '1996-10-09', 2, NULL, NOW()),
  ('henry@example.com',  'hashed_pw_8', 'Henry',  'Smith',  '+66-808-888-888', '1993-12-14', 1, NULL, NOW()),
  ('irene@example.com',  'hashed_pw_9', 'Irene',  'Lee',    '+66-809-999-999', '1998-04-03', 2, NULL, NOW()),
  ('jack@example.com',   'hashed_pw_10','Jack',   'Brown',  '+66-810-000-000', '1990-09-27', 1, NULL, NOW());

-- BUSINESSES (5)
INSERT INTO businesses (business_name, email, phone_number, about_text) VALUES
  ('Glow Studio',     'contact@glowstudio.com',   '+66-900-100-100', 'Beauty studio focused on hair and nails.'),
  ('Krabi Massage',   'hello@krabimassage.com',   '+66-900-200-200', 'Traditional and oil massage specialists.'),
  ('Nordic Cuts',     'info@nordiccuts.com',      '+66-900-300-300', 'Scandinavian-style haircuts and coloring.'),
  ('Silk Nails',      'support@silknails.com',    '+66-900-400-400', 'Manicure, pedicure, gel and design.'),
  ('Calm Skin Lab',   'team@calmskinlab.com',     '+66-900-500-500', 'Facials and skincare treatments.');

-- BUSINESS LOCATIONS (6)
-- Nu måste vi använda business_id från föregående INSERT
INSERT INTO business_locations (business_id, phone_number, email, street_address, city, postal_code, country, longitude, latitude) VALUES
  (1, '+66-901-111-111', 'ao-nang@glowstudio.com',   '123 Beach Rd',     'Ao Nang', '81000', 'Thailand', 98.82310000, 8.03450000),
  (1, '+66-901-222-222', 'krabi@glowstudio.com',    '88 City Center',   'Krabi',   '81000', 'Thailand', 98.91020000, 8.08600000),
  (2, '+66-902-111-111', 'ao-nang@krabimassage.com','55 Relax St',      'Ao Nang', '81000', 'Thailand', 98.82000000, 8.03620000),
  (3, '+66-903-111-111', 'ao-nang@nordiccuts.com',  '9 Nordic Lane',    'Ao Nang', '81000', 'Thailand', 98.82550000, 8.03220000),
  (4, '+66-904-111-111', 'krabi@silknails.com',     '17 Nail Ave',      'Krabi',   '81000', 'Thailand', 98.91200000, 8.08400000),
  (5, '+66-905-111-111', 'krabi@calmskinlab.com',   '200 Wellness Blvd','Krabi',   '81000', 'Thailand', 98.91500000, 8.08200000);

-- EMPLOYEES (8)
INSERT INTO employees (user_id, business_id, location_id, rating) VALUES
  (3, 1, 1, 5),
  (4, 1, 2, 4),
  (6, 2, 3, 5),
  (7, 3, 4, 4),
  (8, 3, 4, 5),
  (9, 4, 5, 4),
  (10,5, 6, 5),
  (1, 1, 1, 4);

-- CUSTOMERS (6)
INSERT INTO customers (user_id, balance) VALUES
  (1,  0.00),
  (2, 25.00),
  (5,  5.50),
  (8,  0.00),
  (9, 12.00),
  (10,0.00);

-- SUPPORT AGENTS (2–3)
INSERT INTO support_agents (user_id, department) VALUES
  (6, 'billing'),
  (7, 'technical'),
  (4, 'general');

-- IMAGES (8)
-- OBS: För image_id behöver vi hålla koll på vilka ID:n som skapas om treatments refererar till dem
-- Lösning: Använd RETURNING eller lägg in images EFTER treatments
INSERT INTO images (business_id, employee_id, location_id, image_url) VALUES
  (1, NULL, 1, 'https://img.example.com/glow/location1.jpg'),
  (1, 1,    1, 'https://img.example.com/glow/employee1.jpg'),
  (2, NULL, 3, 'https://img.example.com/massage/location3.jpg'),
  (2, 3,    3, 'https://img.example.com/massage/employee3.jpg'),
  (3, 4,    4, 'https://img.example.com/nordic/employee4.jpg'),
  (3, NULL, 4, 'https://img.example.com/nordic/location4.jpg'),
  (4, 6,    5, 'https://img.example.com/silk/employee6.jpg'),
  (5, 7,    6, 'https://img.example.com/calm/location6.jpg');

-- TREATMENTS (10)
-- OBS: image_id-referenserna måste uppdateras baserat på faktiska ID:n
-- Alternativ: Sätt image_id till NULL initialt, uppdatera senare
INSERT INTO treatments (treatment_name, treatment_description, category_id, image_id, time_duration, last_min_deal, created_at) VALUES
  ('Classic Haircut',        'Wash + cut + style',                 1, 2, 45, FALSE, NOW()),
  ('Fade Haircut',           'Skin fade option included',          1, 5, 60, TRUE,  NOW()),
  ('Full Coloring',          'Single-process full head coloring',  2, 5, 120,FALSE, NOW()),
  ('Root Touch-up',          'Roots only, quick refresh',          2, NULL,75, TRUE,  NOW()),
  ('Thai Massage 60',        'Traditional Thai massage',           3, 4, 60, FALSE, NOW()),
  ('Oil Massage 90',         'Relaxing oil massage',               3, 3, 90, TRUE,  NOW()),
  ('Gel Manicure',           'Gel polish manicure',                4, 7, 60, FALSE, NOW()),
  ('Pedicure',               'Foot care + polish',                 4, NULL,60, FALSE, NOW()),
  ('Deep Cleansing Facial',  'Cleanse + exfoliate + mask',         5, 8, 75, TRUE,  NOW()),
  ('Brow Shaping',           'Shaping + tidy',                     6, NULL,30, FALSE, NOW());

-- =========================
-- RELATIONER (2–3 rader/join)
-- =========================

INSERT INTO location_treatments (location_id, treatment_id) VALUES
  (1, 1),
  (1, 7),
  (3, 5);

INSERT INTO employee_treatments (treatment_id, employee_id) VALUES
  (1, 1),
  (7, 1),
  (5, 3);

INSERT INTO owners (business_id, user_id) VALUES
  (1, 3),
  (2, 6),
  (3, 7);

INSERT INTO business_service_categories (business_id, category_id) VALUES
  (1, 1),
  (2, 3),
  (4, 2);

INSERT INTO locations_employees (employee_id, location_id) VALUES
  (1, 1),
  (2, 2),
  (3, 3);

INSERT INTO employee_specializations (employee_id, specialization_id) VALUES
  (1, 1),
  (1, 2),
  (3, 3);

-- OPENING HOURS (10 rader)
INSERT INTO opening_hours (location_id, day_of_week, open_time, close_time) VALUES
  (1, 1, '10:00', '19:00'),
  (1, 2, '10:00', '19:00'),
  (1, 3, '10:00', '19:00'),
  (3, 1, '11:00', '20:00'),
  (3, 2, '11:00', '20:00'),
  (4, 1, '10:00', '18:00'),
  (4, 2, '10:00', '18:00'),
  (5, 5, '10:00', '19:00'),
  (6, 6, '10:00', '17:00'),
  (6, 7, '10:00', '17:00');

-- =========================
-- BOOKING / PAYMENT FLOW (kärnflöde)
-- =========================

-- BOOKINGS (8)
INSERT INTO bookings (
  location_id, treatment_id, customer_id, employee_id, business_id,
  booked_date, time_start, time_stop, notes, booking_status, payment_confirmed, created_at
) VALUES
  (1, 1, 1, 1, 1, '2025-12-10', '10:00', '10:45', 'First visit',          2, TRUE,  NOW()),
  (1, 7, 2, 1, 1, '2025-12-11', '11:00', '12:00', NULL,                  2, TRUE,  NOW()),
  (3, 5, 3, 3, 2, '2025-12-12', '14:00', '15:00', 'Neck tension',        4, TRUE,  NOW()),
  (4, 2, 4, 4, 3, '2025-12-13', '09:00', '10:00', 'Fade please',         4, TRUE,  NOW()),
  (5, 8, 5, 6, 4, '2025-12-14', '16:00', '17:00', 'No gel, regular',     1, FALSE, NOW()),
  (6, 9, 6, 7, 5, '2025-12-15', '13:00', '14:15', 'Sensitive skin',      2, FALSE, NOW()),
  (3, 6, 2, 3, 2, '2025-12-16', '12:00', '13:30', NULL,                  3, FALSE, NOW()),
  (2, 3, 1, 2, 1, '2025-12-17', '15:00', '17:00', 'Full color consult',  2, FALSE, NOW());

-- PAYMENTS (8)
INSERT INTO payments (customer_id, location_id, booking_id, payment_method_id, amount, payment_status_id, created_at) VALUES
  (1, 1, 1, 1,  450.00, 2, NOW()),
  (2, 1, 2, 1,  650.00, 2, NOW()),
  (3, 3, 3, 4,  900.00, 2, NOW()),
  (4, 4, 4, 1,  700.00, 2, NOW()),
  (5, 5, 5, 2,  500.00, 1, NOW()),
  (6, 6, 6, 1, 1200.00, 1, NOW()),
  (2, 3, 7, 1, 1300.00, 3, NOW()),
  (1, 2, 8, 3, 2500.00, 1, NOW());

-- REFUNDS (2–3)
INSERT INTO refunds (payment_id, amount, reason, refund_status_id, created_at) VALUES
  (7, 1300.00, 'Service cancelled', 2, NOW()),
  (5,  200.00, 'Partial refund',    1, NOW()),
  (3,  100.00, 'Goodwill',          3, NOW());

-- PAYMENT ATTEMPTS (5)
INSERT INTO payment_attempts (booking_id, customer_id, amount, payment_method_id, failed_attempt_status_id, created_at) VALUES
  (6, 6, 1200.00, 1, 2, NOW()),
  (6, 6, 1200.00, 1, 1, NOW()),
  (7, 2, 1300.00, 1, 2, NOW()),
  (5, 5,  500.00, 2, 3, NOW()),
  (8, 1, 2500.00, 3, 2, NOW());

-- REVIEWS (5)
INSERT INTO reviews (
  booking_id, customer_id, employee_id, location_id, treatment_id,
  overall_rating, location_rating, employee_rating, treatment_rating, review_comment, created_at
) VALUES
  (1, 1, 1, 1, 1, 5, 5, 5, 5, 'Super happy!', NOW()),
  (2, 2, 1, 1, 7, 4, 4, 5, 4, 'Nice nails.',  NOW()),
  (3, 3, 3, 3, 5, 5, 4, 5, 5, 'Amazing massage', NOW()),
  (4, 4, 4, 4, 2, 4, 4, 4, 4, 'Great fade', NOW()),
  (8, 1, 2, 2, 3, 4, 3, 4, 4, 'Color looks good', NOW());

-- FAVORITES (6)
INSERT INTO favorites (treatment_id, customer_id, location_id, employee_id, created_at) VALUES
  (1, 1, 1, 1, NOW()),
  (7, 2, 1, 1, NOW()),
  (5, 3, 3, 3, NOW()),
  (2, 4, 4, 4, NOW()),
  (9, 6, 6, 7, NOW()),
  (8, 5, 5, 6, NOW());

-- GIFT CARDS (3)
INSERT INTO gift_cards (gift_card_code, purchaser_id, gift_card_amount, remaining_balance, purchase_date) VALUES
  ('GC-2025-AAA111', 1, 1000.00, 600.00, NOW()),
  ('GC-2025-BBB222', 2,  500.00, 500.00, NOW()),
  ('GC-2025-CCC333', 3, 1500.00, 900.00, NOW());

-- NOTIFICATIONS (6)
INSERT INTO notifications (customer_id, business_id, employee_id, notification_type, title, message, is_read, read_at, created_at) VALUES
  (1, 1, 1, 'booking', 'Booking confirmed', 'Your booking #1 is confirmed.', TRUE, NOW(), NOW()),
  (2, 1, 1, 'payment', 'Payment received',  'Payment for booking #2 received.', FALSE, NULL, NOW()),
  (3, 2, 3, 'review',  'Thanks!',           'Thanks for your review.', FALSE, NULL, NOW()),
  (5, 4, 6, 'booking', 'Pending',           'Please confirm your booking.', FALSE, NULL, NOW()),
  (6, 5, 7, 'promo',   'Last minute deal',  'A last minute deal is available.', FALSE, NULL, NOW()),
  (NULL, 1, NULL, 'system','Maintenance','System maintenance tonight.', FALSE, NULL, NOW());

-- =========================
-- SUPPORT FLOW (2–3/tabell)
-- =========================

INSERT INTO support_tickets (customer_id, agent_id, status_id, created_at) VALUES
  (1, 1, 1, NOW()),
  (2, 2, 2, NOW()),
  (3, NULL, 1, NOW()),
  (6, 3, 3, NOW());

INSERT INTO support_messages (ticket_id, sender_id, sender_type_id, message, created_at) VALUES
  (1, 1, 1, 'Hi, I have a question about my booking.', NOW()),
  (1, 6, 2, 'Sure! What can I help you with?', NOW()),
  (2, 2, 1, 'My payment seems pending.', NOW()),
  (2, 7, 2, 'We are checking it now.', NOW()),
  (3, 5, 1, 'Can I reschedule?', NOW()),
  (4, 4, 2, 'Ticket is closed now.', NOW());

INSERT INTO ticket_attachment (message_id, file_url, uploaded_at) VALUES
  (3, 'https://files.example.com/receipt_2.png', NOW()),
  (1, 'https://files.example.com/screenshot_booking.png', NOW()),
  (5, 'https://files.example.com/new_time_options.txt', NOW());

-- =========================
-- SCHEDULING + PRICING (2–3/join, lite fler time slots)
-- =========================

INSERT INTO employee_time_slots (employee_id, slot_day, start_time, end_time, is_booked) VALUES
  (1, '2025-12-14', '10:00', '10:45', TRUE),
  (1, '2025-12-14', '11:00', '12:00', TRUE),
  (1, '2025-12-15', '10:00', '10:45', FALSE),
  (3, '2025-12-15', '14:00', '15:00', TRUE),
  (3, '2025-12-16', '12:00', '13:30', FALSE),
  (4, '2025-12-17', '09:00', '10:00', TRUE),
  (6, '2025-12-14', '16:00', '17:00', FALSE),
  (7, '2025-12-15', '13:00', '14:15', TRUE),
  (2, '2025-12-17', '15:00', '17:00', TRUE),
  (2, '2025-12-18', '12:00', '14:00', FALSE);

INSERT INTO employee_pricing (employee_id, treatment_id, location_id, price_per_hour) VALUES
  (1, 1, 1, 600.00),
  (1, 7, 1, 650.00),
  (3, 5, 3, 900.00);