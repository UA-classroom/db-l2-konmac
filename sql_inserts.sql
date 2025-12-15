-- Gender types
INSERT INTO gender_types (gender_types) VALUES
('Man'),
('Kvinna'),
('Icke-binär'),
('Vill ej uppge');

-- Users
INSERT INTO users (email, password, first_name, last_name, phone_number, date_of_birth, gender_id, profile_photo) VALUES
('anna.andersson@email.com', 'hashed_pw_1', 'Anna', 'Andersson', '0701234567', '1990-05-15', 2, 'https://example.com/photos/anna.jpg'),
('erik.eriksson@email.com', 'hashed_pw_2', 'Erik', 'Eriksson', '0701234568', '1985-08-22', 1, 'https://example.com/photos/erik.jpg'),
('maria.karlsson@email.com', 'hashed_pw_3', 'Maria', 'Karlsson', '0701234569', '1992-11-30', 2, 'https://example.com/photos/maria.jpg'),
('johan.nilsson@email.com', 'hashed_pw_4', 'Johan', 'Nilsson', '0701234570', '1988-03-12', 1, 'https://example.com/photos/johan.jpg'),
('lisa.svensson@email.com', 'hashed_pw_5', 'Lisa', 'Svensson', '0701234571', '1995-07-08', 2, 'https://example.com/photos/lisa.jpg'),
('peter.olsson@email.com', 'hashed_pw_6', 'Peter', 'Olsson', '0701234572', '1987-12-19', 1, NULL),
('sara.gustafsson@email.com', 'hashed_pw_7', 'Sara', 'Gustafsson', '0701234573', '1993-04-25', 2, NULL),
('mikael.larsson@email.com', 'hashed_pw_8', 'Mikael', 'Larsson', '0701234574', '1991-09-14', 1, NULL),
('emma.berg@email.com', 'hashed_pw_9', 'Emma', 'Berg', '0701234575', '1989-06-07', 2, NULL),
('david.lundgren@email.com', 'hashed_pw_10', 'David', 'Lundgren', '0701234576', '1994-01-23', 1, NULL),
('support.agent1@bokadirekt.se', 'hashed_pw_11', 'Karin', 'Support', '0701234577', '1986-05-10', 2, NULL),
('support.agent2@bokadirekt.se', 'hashed_pw_12', 'Anders', 'Hjälp', '0701234578', '1990-08-15', 1, NULL);

-- Businesses
INSERT INTO businesses (business_name, email, phone_number, about_text) VALUES
('Skönhetssalongen Glam', 'info@glamsalong.se', '08-1234567', 'Stockholms mest exklusiva skönhetssalong med över 15 års erfarenhet'),
('Hårstudion Clips', 'kontakt@clips.se', '031-9876543', 'Modern hårsalong i hjärtat av Göteborg'),
('Spa & Relax Malmö', 'info@sparelax.se', '040-5551234', 'Avkoppling och välmående i toppklass');

-- Treatment categories
INSERT INTO treatment_categories (category_name) VALUES
('Hår'),
('Naglar'),
('Ansiktsbehandling'),
('Massage'),
('Spa'),
('Makeup'),
('Vaxning'),
('Skönhet');

-- Customers
INSERT INTO customers (user_id, balance) VALUES
(1, 500.00),
(2, 0.00),
(3, 250.00),
(4, 100.00),
(5, 0.00),
(6, 750.00);

-- Booking statuses
INSERT INTO booking_statuses (status_name) VALUES
('Bekräftad'),
('Avbokad'),
('Genomförd'),
('Inställd'),
('Väntande');

-- Refund statuses
INSERT INTO refund_statuses (status) VALUES
('Begärd'),
('Godkänd'),
('Behandlas'),
('Slutförd'),
('Nekad');

-- Payment statuses
INSERT INTO payment_statuses (status_name) VALUES
('Väntande'),
('Genomförd'),
('Misslyckad'),
('Återbetald');

-- Payment methods
INSERT INTO payment_methods (method_name) VALUES
('Swish'),
('Kort'),
('Presentkort'),
('Saldo'),
('Klarna');

-- Failed statuses
INSERT INTO failed_statuses (status_name) VALUES
('Otillräckliga medel'),
('Kort nekat'),
('Timeout'),
('Tekniskt fel'),
('Ogiltigt kort');

-- Support ticket statuses
INSERT INTO support_ticket_statuses (status_name) VALUES
('Öppet'),
('Under behandling'),
('Väntar på kund'),
('Löst'),
('Stängt');

-- Sender types
INSERT INTO sender_types (type_name, is_active) VALUES
('Kund', TRUE),
('Agent', TRUE),
('System', TRUE);

-- Service categories
INSERT INTO service_categories (category_name) VALUES
('Hår & Styling'),
('Skönhet & Spa'),
('Nagelvård'),
('Massage & Wellness'),
('Hudvård');

-- Specializations
INSERT INTO specializations (specialization_name) VALUES
('Klippning'),
('Färgning'),
('Permanent'),
('Naglar'),
('Ansiktsbehandling'),
('Massage'),
('Vaxning'),
('Makeup artistry'),
('Bröllopsstyling');

-- Business locations
INSERT INTO business_locations (business_id, phone_number, email, street_address, city, postal_code, country, longitude, latitude) VALUES
(1, '08-1234567', 'ostermalm@glamsalong.se', 'Strandvägen 12', 'Stockholm', '11451', 'Sverige', 18.0875490, 59.3326090),
(1, '08-1234568', 'sodermalm@glamsalong.se', 'Götgatan 45', 'Stockholm', '11621', 'Sverige', 18.0709140, 59.3142340),
(2, '031-9876543', 'info@clips.se', 'Avenyn 28', 'Göteborg', '41136', 'Sverige', 11.9745620, 57.7007470),
(3, '040-5551234', 'info@sparelax.se', 'Stortorget 7', 'Malmö', '21122', 'Sverige', 13.0007310, 55.6048660);

-- Employees
INSERT INTO employees (user_id, business_id, location_id, rating) VALUES
(7, 1, 1, 5),
(8, 1, 1, 4),
(9, 1, 2, 5),
(10, 2, 3, 4),
(5, 3, 4, 5);

-- Images
INSERT INTO images (business_id, employee_id, location_id, image_url) VALUES
(1, NULL, 1, 'https://example.com/business/glam_ostermalm.jpg'),
(1, NULL, 2, 'https://example.com/business/glam_sodermalm.jpg'),
(2, NULL, 3, 'https://example.com/business/clips_gbg.jpg'),
(3, NULL, 4, 'https://example.com/business/spa_malmo.jpg'),
(NULL, 1, NULL, 'https://example.com/employees/sara.jpg'),
(NULL, 2, NULL, 'https://example.com/employees/mikael.jpg'),
(NULL, 3, NULL, 'https://example.com/employees/emma.jpg'),
(NULL, 4, NULL, 'https://example.com/employees/david.jpg'),
(NULL, 5, NULL, 'https://example.com/employees/lisa.jpg');

-- Treatments
INSERT INTO treatments (treatment_name, treatment_description, category_id, image_id, time_duration, last_min_deal) VALUES
('Damklippning', 'Professionell klippning med styling', 1, 1, 60, FALSE),
('Herrklippning', 'Klippning och trimning', 1, 1, 45, FALSE),
('Helförgning', 'Komplett färgbehandling', 1, 1, 120, FALSE),
('Highlights', 'Slingor/highlights enligt önskemål', 1, 1, 90, FALSE),
('Manikyr', 'Klassisk manikyr med lack', 2, 2, 45, FALSE),
('Gellack', 'Gellack behandling', 2, 2, 60, FALSE),
('Ansiktsbehandling Basic', 'Rengöring och återfuktning', 3, 3, 60, FALSE),
('Ansiktsbehandling Lyx', 'Komplett lyxbehandling med mask', 3, 3, 90, TRUE),
('Ryggmassage', 'Avslappnande ryggmassage', 4, 4, 50, FALSE),
('Helkroppsmassage', 'Massage av hela kroppen', 4, 4, 90, FALSE),
('Spa-paket Dag', 'Heldagspaket med behandlingar', 5, 4, 240, FALSE),
('Brudmakeup', 'Professionell makeup för bröllopsdagen', 6, 1, 90, FALSE),
('Vaxning Ben', 'Vaxning av hela ben', 7, 2, 45, TRUE),
('Vaxning Bikinilinje', 'Vaxning av bikinilinje', 7, 2, 30, FALSE);

-- Bookings
INSERT INTO bookings (location_id, treatment_id, customer_id, employee_id, business_id, booked_date, time_start, time_stop, notes, booking_status, payment_confirmed) VALUES
(1, 1, 1, 1, 1, '2025-01-15', '10:00', '11:00', 'Vill ha lugg', 1, TRUE),
(1, 3, 2, 1, 1, '2025-01-15', '14:00', '16:00', 'Blond färg', 1, TRUE),
(2, 5, 3, 3, 1, '2025-01-16', '11:00', '11:45', NULL, 1, TRUE),
(3, 2, 4, 4, 2, '2025-01-16', '15:00', '15:45', 'Kort klippning', 1, TRUE),
(4, 10, 5, 5, 3, '2025-01-17', '13:00', '14:30', 'Djup vävnadsmassage', 1, TRUE),
(1, 8, 6, 2, 1, '2025-01-18', '10:00', '11:30', NULL, 5, FALSE),
(2, 6, 1, 3, 1, '2025-01-20', '09:00', '10:00', NULL, 1, TRUE),
(4, 9, 3, 5, 3, '2025-01-22', '16:00', '16:50', 'Allergisk mot vissa oljor', 1, TRUE);

-- Reviews
INSERT INTO reviews (booking_id, customer_id, employee_id, location_id, treatment_id, overall_rating, location_rating, employee_rating, treatment_rating, review_comment) VALUES
(1, 1, 1, 1, 1, 5, 5, 5, 5, 'Fantastisk klippning! Sara är duktig och lyssnar på mina önskemål.'),
(2, 2, 1, 1, 3, 4, 5, 4, 4, 'Bra färgning men tog lite längre tid än planerat'),
(3, 3, 3, 2, 5, 5, 4, 5, 5, 'Mycket nöjd med manikyr! Emma är proffs.'),
(4, 4, 4, 3, 2, 4, 4, 4, 4, 'Bra klippning, trevlig personal'),
(5, 5, 5, 4, 10, 5, 5, 5, 5, 'Bästa massagen jag fått! Kommer definitivt tillbaka.');

-- Favorites
INSERT INTO favorites (treatment_id, customer_id, location_id, employee_id) VALUES
(1, 1, 1, 1),
(3, 1, 1, 1),
(5, 3, 2, 3),
(10, 5, 4, 5),
(2, 4, 3, 4),
(8, 6, 1, 2);

-- Gift cards
INSERT INTO gift_cards (gift_card_code, purchaser_id, gift_card_amount, remaining_balance) VALUES
('GC2025-001-XKPL', 1, 1000.00, 1000.00),
('GC2025-002-BMQR', 2, 500.00, 250.00),
('GC2025-003-TNWP', 6, 750.00, 750.00);

-- Payments
INSERT INTO payments (customer_id, location_id, booking_id, payment_method_id, amount, payment_status_id) VALUES
(1, 1, 1, 1, 650.00, 2),
(2, 1, 2, 2, 1200.00, 2),
(3, 2, 3, 1, 450.00, 2),
(4, 3, 4, 2, 400.00, 2),
(5, 4, 5, 3, 950.00, 2),
(1, 2, 7, 1, 550.00, 2),
(3, 4, 8, 2, 500.00, 2);

-- Refunds
INSERT INTO refunds (payment_id, amount, reason, refund_status_id) VALUES
(2, 600.00, 'Kunden var missnöjd med resultatet', 4);

-- Payment attempts
INSERT INTO payment_attempts (booking_id, customer_id, amount, payment_method_id, failed_attempt_status_id) VALUES
(6, 6, 850.00, 2, 1),
(6, 6, 850.00, 2, 4);

-- Notifications
INSERT INTO notifications (customer_id, business_id, employee_id, notification_type, title, message, is_read) VALUES
(1, 1, NULL, 'booking_confirmation', 'Bokning bekräftad', 'Din bokning den 15 januari kl 10:00 är bekräftad', TRUE),
(2, 1, NULL, 'booking_confirmation', 'Bokning bekräftad', 'Din bokning den 15 januari kl 14:00 är bekräftad', TRUE),
(1, NULL, 1, 'reminder', 'Påminnelse om bokning', 'Din behandling är imorgon kl 10:00', FALSE),
(5, 3, NULL, 'special_offer', 'Specialerbjudande!', 'Boka massage denna vecka och få 20% rabatt', FALSE);

-- Support agents
INSERT INTO support_agents (user_id, department) VALUES
(11, 'Kundsupport'),
(12, 'Teknisk support');

-- Support tickets
INSERT INTO support_tickets (customer_id, agent_id, status_id) VALUES
(1, 1, 4),
(2, 1, 2),
(3, NULL, 1);

-- Support messages
INSERT INTO support_messages (ticket_id, sender_id, sender_type_id, message) VALUES
(1, 1, 1, 'Jag kan inte hitta min bokning i appen'),
(1, 11, 2, 'Hej! Jag ska hjälpa dig. Kan du ange bokningsdatum?'),
(1, 1, 1, 'Det var den 15 januari'),
(1, 11, 2, 'Jag ser din bokning nu. Den är bekräftad för kl 10:00'),
(2, 2, 1, 'Vill ändra tid på min bokning'),
(2, 11, 2, 'Vilket datum och ny tid önskar du?'),
(3, 3, 1, 'Hur avbokar jag en behandling?');

-- Ticket attachments
INSERT INTO ticket_attachment (message_id, file_url) VALUES
(1, 'https://example.com/screenshots/booking_issue.png');

-- Location treatments
INSERT INTO location_treatments (location_id, treatment_id) VALUES
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 12),
(2, 1), (2, 2), (2, 5), (2, 6), (2, 7), (2, 13), (2, 14),
(3, 1), (3, 2), (3, 3), (3, 4),
(4, 7), (4, 8), (4, 9), (4, 10), (4, 11);

-- Employee treatments
INSERT INTO employee_treatments (treatment_id, employee_id) VALUES
(1, 1), (2, 1), (3, 1), (4, 1), (12, 1),
(5, 2), (6, 2), (8, 2),
(1, 3), (5, 3), (6, 3), (13, 3), (14, 3),
(1, 4), (2, 4), (3, 4), (4, 4),
(7, 5), (8, 5), (9, 5), (10, 5), (11, 5);

-- Owners
INSERT INTO owners (business_id, user_id) VALUES
(1, 7),
(2, 10),
(3, 5);

-- Business service categories
INSERT INTO business_service_categories (business_id, category_id) VALUES
(1, 1), (1, 2), (1, 3),
(2, 1),
(3, 2), (3, 4), (3, 5);

-- Opening hours
INSERT INTO opening_hours (location_id, day_of_week, open_time, close_time) VALUES
-- Location 1 (Glam Östermalm)
(1, 1, '09:00', '18:00'), -- Måndag
(1, 2, '09:00', '18:00'), -- Tisdag
(1, 3, '09:00', '18:00'), -- Onsdag
(1, 4, '09:00', '20:00'), -- Torsdag
(1, 5, '09:00', '18:00'), -- Fredag
(1, 6, '10:00', '16:00'), -- Lördag
-- Location 2 (Glam Södermalm)
(2, 1, '10:00', '19:00'),
(2, 2, '10:00', '19:00'),
(2, 3, '10:00', '19:00'),
(2, 4, '10:00', '20:00'),
(2, 5, '10:00', '19:00'),
(2, 6, '10:00', '17:00'),
-- Location 3 (Clips Göteborg)
(3, 1, '09:00', '17:00'),
(3, 2, '09:00', '17:00'),
(3, 3, '09:00', '17:00'),
(3, 4, '09:00', '19:00'),
(3, 5, '09:00', '17:00'),
(3, 6, '10:00', '15:00'),
-- Location 4 (Spa Malmö)
(4, 1, '10:00', '20:00'),
(4, 2, '10:00', '20:00'),
(4, 3, '10:00', '20:00'),
(4, 4, '10:00', '20:00'),
(4, 5, '10:00', '20:00'),
(4, 6, '09:00', '18:00'),
(4, 0, '10:00', '17:00'); -- Söndag

-- Locations employees
INSERT INTO locations_employees (employee_id, location_id) VALUES
(1, 1),
(2, 1),
(3, 2),
(4, 3),
(5, 4);

-- Employee specializations
INSERT INTO employee_specializations (employee_id, specialization_id) VALUES
(1, 1), (1, 2), (1, 8),
(2, 4), (2, 5),
(3, 1), (3, 4), (3, 7),
(4, 1), (4, 2), (4, 3),
(5, 5), (5, 6);

-- Employee time slots
INSERT INTO employee_time_slots (employee_id, slot_day, start_time, end_time, is_booked) VALUES
-- Sara (employee 1) - 15 januari
(1, '2025-01-15', '09:00', '10:00', FALSE),
(1, '2025-01-15', '10:00', '11:00', TRUE),
(1, '2025-01-15', '11:00', '12:00', FALSE),
(1, '2025-01-15', '14:00', '16:00', TRUE),
(1, '2025-01-15', '16:00', '17:00', FALSE),
-- Mikael (employee 2) - 18 januari
(2, '2025-01-18', '09:00', '10:00', FALSE),
(2, '2025-01-18', '10:00', '11:30', TRUE),
(2, '2025-01-18', '11:30', '13:00', FALSE),
(2, '2025-01-18', '14:00', '15:30', FALSE),
-- Emma (employee 3) - 16 & 20 januari
(3, '2025-01-16', '09:00', '10:00', FALSE),
(3, '2025-01-16', '11:00', '11:45', TRUE),
(3, '2025-01-16', '13:00', '14:00', FALSE),
(3, '2025-01-20', '09:00', '10:00', TRUE),
(3, '2025-01-20', '10:00', '11:00', FALSE),
-- David (employee 4) - 16 januari
(4, '2025-01-16', '14:00', '15:00', FALSE),
(4, '2025-01-16', '15:00', '15:45', TRUE),
(4, '2025-01-16', '16:00', '17:00', FALSE),
-- Lisa (employee 5) - 17 & 22 januari
(5, '2025-01-17', '10:00', '11:30', FALSE),
(5, '2025-01-17', '13:00', '14:30', TRUE),
(5, '2025-01-17', '15:00', '16:30', FALSE),
(5, '2025-01-22', '14:00', '15:00', FALSE),
(5, '2025-01-22', '16:00', '16:50', TRUE),
(5, '2025-01-22', '17:00', '18:00', FALSE);

-- Employee pricing
INSERT INTO employee_pricing (employee_id, treatment_id, location_id, price_per_hour) VALUES
-- Sara (employee 1) at location 1
(1, 1, 1, 650.00),
(1, 2, 1, 500.00),
(1, 3, 1, 1200.00),
(1, 4, 1, 900.00),
(1, 12, 1, 1500.00),
-- Mikael (employee 2) at location 1
(2, 5, 1, 450.00),
(2, 6, 1, 550.00),
(2, 8, 1, 850.00),
-- Emma (employee 3) at location 2
(3, 1, 2, 600.00),
(3, 5, 2, 450.00),
(3, 6, 2, 550.00),
(3, 13, 2, 400.00),
(3, 14, 2, 350.00),
-- David (employee 4) at location 3
(4, 1, 3, 550.00),
(4, 2, 3, 400.00),
(4, 3, 3, 1100.00),
(4, 4, 3, 850.00),
-- Lisa (employee 5) at location 4
(5, 7, 4, 750.00),
(5, 8, 4, 950.00),
(5, 9, 4, 600.00),
(5, 10, 4, 950.00),
(5, 11, 4, 2500.00);