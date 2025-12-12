-- Gender types
INSERT INTO gender_types (gender_types) VALUES
('Man'),
('Kvinna'),
('Icke-binär'),
('Vill ej ange');

-- Users (kunder, anställda, ägare, supportagenter)
INSERT INTO users (email, password, first_name, last_name, phone_number, date_of_birth, gender) VALUES
('anna.andersson@email.com', '$2b$12$hashedpassword1', 'Anna', 'Andersson', '0701234567', '1990-05-15', 2),
('erik.eriksson@email.com', '$2b$12$hashedpassword2', 'Erik', 'Eriksson', '0702345678', '1985-08-22', 1),
('maria.svensson@email.com', '$2b$12$hashedpassword3', 'Maria', 'Svensson', '0703456789', '1992-03-10', 2),
('johan.johansson@email.com', '$2b$12$hashedpassword4', 'Johan', 'Johansson', '0704567890', '1988-11-30', 1),
('lisa.karlsson@email.com', '$2b$12$hashedpassword5', 'Lisa', 'Karlsson', '0705678901', '1995-07-18', 2),
('peter.nilsson@email.com', '$2b$12$hashedpassword6', 'Peter', 'Nilsson', '0706789012', '1987-09-25', 1),
('emma.pettersson@email.com', '$2b$12$hashedpassword7', 'Emma', 'Pettersson', '0707890123', '1993-12-05', 2),
('oskar.lundberg@email.com', '$2b$12$hashedpassword8', 'Oskar', 'Lundberg', '0708901234', '1991-04-14', 1),
('sara.berg@email.com', '$2b$12$hashedpassword9', 'Sara', 'Berg', '0709012345', '1989-06-20', 2),
('daniel.lindström@email.com', '$2b$12$hashedpassword10', 'Daniel', 'Lindström', '0700123456', '1994-02-28', 1),
('karin.henriksson@email.com', '$2b$12$hashedpassword11', 'Karin', 'Henriksson', '0701112233', '1986-10-12', 2),
('mikael.ström@email.com', '$2b$12$hashedpassword12', 'Mikael', 'Ström', '0702223344', '1990-01-08', 1),
('sofia.magnusson@email.com', '$2b$12$hashedpassword13', 'Sofia', 'Magnusson', '0703334455', '1992-08-16', 2),
('andreas.olsson@email.com', '$2b$12$hashedpassword14', 'Andreas', 'Olsson', '0704445566', '1988-05-22', 1),
('linda.gustafsson@email.com', '$2b$12$hashedpassword15', 'Linda', 'Gustafsson', '0705556677', '1991-11-03', 2);

-- Businesses
INSERT INTO businesses (business_name, email, phone_number, about_text, number_of_employees) VALUES
('Beauty Stockholm AB', 'info@beautystockholm.se', '0812345678', 'Stockholms ledande skönhetssalong med fokus på professionell behandling och kundnöjdhet.', 8),
('Spa & Relax Göteborg', 'kontakt@sparelax.se', '0313456789', 'Lyxig spa-upplevelse i hjärtat av Göteborg. Vi erbjuder massage, ansiktsbehandlingar och kroppsbehandlingar.', 6),
('Nagelsalongen Malmö', 'hello@nagelsalongen.se', '0404567890', 'Specialister på nagelvård, gelé och nagelförlängning.', 4),
('Hårstudion Uppsala', 'info@harstudion.se', '0187654321', 'Modern frisörsalong med erfarna stylister.', 5);

-- Treatment categories
INSERT INTO treatment_categories (category_name) VALUES
('Ansiktsbehandling'),
('Massage'),
('Nagelvård'),
('Hårvård'),
('Kroppsbehandling'),
('Vaxning'),
('Make-up'),
('Ögonfransar & Bryn');

-- Customers
INSERT INTO customers (user_id, balance) VALUES
(1, 0.00),
(2, 150.00),
(3, 0.00),
(4, 200.00),
(5, 0.00),
(10, 50.00);

-- Booking statuses
INSERT INTO booking_statuses (status_name) VALUES
('Bekräftad'),
('Avbokad'),
('Slutförd'),
('Ej uppkommen'),
('Väntande');

-- Refund statuses
INSERT INTO refund_statuses (status) VALUES
('Pending'),
('Completed'),
('Rejected'),
('Processing');

-- Payment statuses
INSERT INTO payment_statuses (status_name) VALUES
('Completed'),
('Pending'),
('Failed'),
('Refunded');

-- Payment methods
INSERT INTO payment_methods (method_name) VALUES
('Swish'),
('Kreditkort'),
('Presentkort'),
('Faktura');

-- Failed statuses
INSERT INTO failed_statuses (status_name) VALUES
('Insufficient funds'),
('Card declined'),
('Network error'),
('Timeout'),
('Invalid card');

-- Support ticket statuses
INSERT INTO support_ticket_statuses (status_name) VALUES
('Open'),
('In Progress'),
('Waiting for customer'),
('Resolved'),
('Closed');

-- Sender types
INSERT INTO sender_types (type_name, is_active) VALUES
('Customer', TRUE),
('Agent', TRUE),
('System', TRUE);

-- Service categories
INSERT INTO service_categories (category_name) VALUES
('Skönhet & Spa'),
('Hår & Makeup'),
('Nagelvård'),
('Massage & Wellness'),
('Hudvård');

-- Specializations
INSERT INTO specializations (specialization_name) VALUES
('Ansiktsbehandlingar'),
('Klassisk massage'),
('Nagelteknolog'),
('Frisör'),
('Makeup artist'),
('Laser & IPL'),
('Permanent makeup'),
('Vaxning');

-- Business locations
INSERT INTO business_locations (business_id, phone_number, email, street_address, city, postal_code, country, longitude, latitude) VALUES
(1, '0812345678', 'ostermalm@beautystockholm.se', 'Karlavägen 25', 'Stockholm', '11431', 'Sverige', 18.0773, 59.3422),
(1, '0812345679', 'sodermalm@beautystockholm.se', 'Götgatan 50', 'Stockholm', '11621', 'Sverige', 18.0721, 59.3157),
(2, '0313456789', 'centrum@sparelax.se', 'Avenyn 15', 'Göteborg', '41136', 'Sverige', 11.9746, 57.7017),
(3, '0404567890', 'info@nagelsalongen.se', 'Södergatan 8', 'Malmö', '21134', 'Sverige', 13.0007, 55.6044),
(4, '0187654321', 'info@harstudion.se', 'Svartbäcksgatan 12', 'Uppsala', '75332', 'Sverige', 17.6389, 59.8586);

-- Employees
INSERT INTO employees (user_id, business_id, location_id, rating) VALUES
(6, 1, 1, 5),
(7, 1, 1, 4),
(8, 1, 2, 5),
(9, 2, 3, 4),
(11, 2, 3, 5),
(12, 3, 4, 4),
(13, 3, 4, 5),
(14, 4, 5, 4),
(15, 4, 5, 5);

-- Images (nu med user_id också)
INSERT INTO images (business_id, employee_id, location_id, user_id, image_url) VALUES
(1, NULL, 1, NULL, 'https://images.bokadirekt.se/business1_loc1.jpg'),
(1, NULL, 2, NULL, 'https://images.bokadirekt.se/business1_loc2.jpg'),
(2, NULL, 3, NULL, 'https://images.bokadirekt.se/business2_loc3.jpg'),
(3, NULL, 4, NULL, 'https://images.bokadirekt.se/business3_loc4.jpg'),
(4, NULL, 5, NULL, 'https://images.bokadirekt.se/business4_loc5.jpg'),
(NULL, 1, NULL, 6, 'https://images.bokadirekt.se/employee1.jpg'),
(NULL, 2, NULL, 7, 'https://images.bokadirekt.se/employee2.jpg'),
(NULL, 3, NULL, 8, 'https://images.bokadirekt.se/employee3.jpg'),
(NULL, NULL, NULL, 1, 'https://images.bokadirekt.se/user1_profile.jpg'),
(NULL, NULL, NULL, 2, 'https://images.bokadirekt.se/user2_profile.jpg');

-- Treatments
INSERT INTO treatments (treatment_name, treatment_description, category_id, image_id, time_duration, last_min_deal) VALUES
('Klassisk ansiktsbehandling', 'Rengöring, peeling och mask anpassad efter din hudtyp.', 1, 1, 60, FALSE),
('Lyxig ansiktsbehandling', 'Omfattande behandling med djuprengöring, massage och mask.', 1, 1, 90, FALSE),
('Svensk massage 60 min', 'Avslappnande helkroppsmassage som lindrar spänningar.', 2, 2, 60, FALSE),
('Deep tissue massage', 'Djup vävnadsmassage för kroniska spänningar.', 2, 2, 75, FALSE),
('Manikyr', 'Fullständig nagelvård med lack eller gelé.', 3, 4, 45, FALSE),
('Pedikyr', 'Fotvård och nagelvård för fötterna.', 3, 4, 60, FALSE),
('Gelé naglar', 'Hållbar gelélackning som håller i 2-3 veckor.', 3, 4, 60, FALSE),
('Klippning & föning dam', 'Professionell hårklippning och styling.', 4, 5, 60, FALSE),
('Klippning & föning herr', 'Herrklippning med styling.', 4, 5, 45, FALSE),
('Färgning helthuvud', 'Heltäckande hårfärgning.', 4, 5, 120, FALSE),
('Slingor', 'Highlights/slingor för dimension i håret.', 4, 5, 150, FALSE),
('Brasiliansk vaxning', 'Professionell vaxning av bikinilinjen.', 6, 3, 30, FALSE),
('Benvaxning hela ben', 'Vaxning av båda benen.', 6, 3, 45, FALSE),
('Brynplock & färgning', 'Formning och färgning av ögonbryn.', 8, 1, 30, FALSE),
('Fransar & bryn paket', 'Komplett paket för ögonfransar och bryn.', 8, 1, 45, TRUE);

-- Bookings
INSERT INTO bookings (location_id, treatment_id, customer_id, employee_id, business_id, booked_date, time_start, time_stop, notes, booking_status, payment_confirmed) VALUES
(1, 1, 1, 1, 1, '2024-12-10', '10:00', '11:00', 'Första besöket', 1, TRUE),
(1, 3, 2, 2, 1, '2024-12-10', '14:00', '15:00', NULL, 1, TRUE),
(2, 5, 3, 3, 1, '2024-12-11', '11:00', '11:45', 'Allergisk mot vissa produkter', 1, TRUE),
(3, 4, 4, 4, 2, '2024-12-12', '09:00', '10:15', NULL, 1, TRUE),
(3, 2, 1, 5, 2, '2024-12-13', '15:00', '16:30', 'Önskar extra ansiktsmassage', 1, FALSE),
(4, 7, 5, 6, 3, '2024-12-14', '10:00', '11:00', NULL, 3, TRUE),
(4, 5, 2, 7, 3, '2024-12-09', '13:00', '13:45', NULL, 3, TRUE),
(5, 8, 3, 8, 4, '2024-12-15', '12:00', '13:00', 'Vill ha lager i håret', 5, FALSE);

-- Reviews
INSERT INTO reviews (booking_id, customer_id, employee_id, location_id, treatment_id, overall_rating, location_rating, employee_rating, treatment_rating, review_comment) VALUES
(6, 5, 6, 4, 7, 5, 5, 5, 5, 'Fantastisk behandling! Supernöjd med resultatet.'),
(7, 2, 7, 4, 5, 4, 4, 5, 4, 'Bra service, trevlig personal. Kommer tillbaka!');

-- Favorites
INSERT INTO favorites (treatment_id, customer_id, location_id, employee_id) VALUES
(1, 1, 1, 1),
(3, 2, 1, 2),
(5, 3, 2, 3),
(4, 4, 3, 4);

-- Gift cards
INSERT INTO gift_cards (gift_card_code, purchaser_id, gift_card_amount, remaining_balance) VALUES
('GIFT2024-ABC123', 2, 500.00, 350.00),
('GIFT2024-XYZ789', 4, 1000.00, 1000.00);

-- Payments
INSERT INTO payments (customer_id, location_id, booking_id, payment_method_id, amount, payment_status_id) VALUES
(1, 1, 1, 1, 650.00, 1),
(2, 1, 2, 2, 850.00, 1),
(3, 2, 3, 1, 450.00, 1),
(4, 3, 4, 2, 950.00, 1),
(5, 4, 6, 1, 600.00, 1),
(2, 4, 7, 1, 450.00, 1);

-- Refunds
INSERT INTO refunds (payment_id, amount, reason, refund_status_id) VALUES
(6, 450.00, 'Kunden var inte nöjd med behandlingen', 2);

-- Payment attempts
INSERT INTO payment_attempts (booking_id, customer_id, amount, payment_method_id, failed_attempt_status_id) VALUES
(5, 1, 950.00, 2, 2),
(8, 3, 650.00, 2, 1);

-- Notifications
INSERT INTO notifications (customer_id, business_id, employee_id, notification_type, title, message, is_read) VALUES
(1, 1, 1, 'booking_confirmation', 'Bokning bekräftad', 'Din bokning den 10 december kl 10:00 är nu bekräftad.', TRUE),
(2, 1, 2, 'booking_reminder', 'Påminnelse: Bokning imorgon', 'Glöm inte din bokning imorgon kl 14:00.', FALSE),
(3, 1, 3, 'payment_confirmed', 'Betalning mottagen', 'Vi har mottagit din betalning på 450 kr.', TRUE);

-- Support agents
INSERT INTO support_agents (user_id, department) VALUES
(10, 'Customer Service'),
(11, 'Technical Support');

-- Support tickets
INSERT INTO support_tickets (customer_id, agent_id, status_id) VALUES
(1, 1, 4),
(2, 1, 1),
(3, 2, 2);

-- Support messages
INSERT INTO support_messages (ticket_id, sender_id, sender_type_id, message) VALUES
(1, 1, 1, 'Jag kan inte hitta min bokning i appen.'),
(1, 10, 2, 'Hej! Jag hjälper dig gärna. Kan du ange vilket datum du bokade för?'),
(1, 1, 1, 'Det var den 10 december kl 10:00.'),
(1, 10, 2, 'Tack! Jag ser din bokning nu. Den är bekräftad och allt ser bra ut.'),
(2, 2, 1, 'Kan jag ändra min bokningstid?'),
(2, 10, 2, 'Ja, det går bra! Vilken ny tid önskar du?');

-- Ticket attachments
INSERT INTO ticket_attachment (message_id, file_url) VALUES
(1, 'https://support.bokadirekt.se/attachments/ticket1_screenshot.png');

-- Location treatments
INSERT INTO location_treatments (location_id, treatment_id) VALUES
(1, 1), (1, 2), (1, 3), (1, 4),
(2, 5), (2, 6), (2, 7), (2, 12), (2, 13),
(3, 2), (3, 3), (3, 4),
(4, 5), (4, 6), (4, 7),
(5, 8), (5, 9), (5, 10), (5, 11);

-- Employee treatments
INSERT INTO employee_treatments (treatment_id, employee_id) VALUES
(1, 1), (2, 1), (14, 1), (15, 1),
(3, 2), (4, 2),
(5, 3), (6, 3), (7, 3),
(3, 4), (4, 4), (2, 5),
(5, 6), (6, 6), (7, 6),
(5, 7), (7, 7),
(8, 8), (9, 8), (10, 8),
(8, 9), (9, 9), (11, 9);

-- Owners
INSERT INTO owners (business_id, user_id) VALUES
(1, 6),
(2, 9),
(3, 12),
(4, 14);

-- Business service categories
INSERT INTO business_service_categories (business_id, category_id) VALUES
(1, 1), (1, 4), (1, 5),
(2, 1), (2, 4),
(3, 3),
(4, 2);

-- Opening hours
INSERT INTO opening_hours (location_id, day_of_week, open_time, close_time) VALUES
-- Location 1 (Stockholm Östermalm)
(1, 1, '09:00', '18:00'), -- Måndag
(1, 2, '09:00', '18:00'), -- Tisdag
(1, 3, '09:00', '18:00'), -- Onsdag
(1, 4, '09:00', '20:00'), -- Torsdag
(1, 5, '09:00', '18:00'), -- Fredag
(1, 6, '10:00', '16:00'), -- Lördag
-- Location 2 (Stockholm Södermalm)
(2, 1, '10:00', '19:00'),
(2, 2, '10:00', '19:00'),
(2, 3, '10:00', '19:00'),
(2, 4, '10:00', '19:00'),
(2, 5, '10:00', '19:00'),
(2, 6, '10:00', '17:00'),
(2, 0, '11:00', '16:00'), -- Söndag
-- Location 3 (Göteborg)
(3, 1, '08:00', '17:00'),
(3, 2, '08:00', '17:00'),
(3, 3, '08:00', '17:00'),
(3, 4, '08:00', '17:00'),
(3, 5, '08:00', '17:00'),
-- Location 4 (Malmö)
(4, 1, '09:00', '18:00'),
(4, 2, '09:00', '18:00'),
(4, 3, '09:00', '20:00'),
(4, 4, '09:00', '18:00'),
(4, 5, '09:00', '18:00'),
(4, 6, '10:00', '15:00'),
-- Location 5 (Uppsala)
(5, 1, '10:00', '19:00'),
(5, 2, '10:00', '19:00'),
(5, 3, '10:00', '19:00'),
(5, 4, '10:00', '19:00'),
(5, 5, '10:00', '19:00'),
(5, 6, '10:00', '16:00');

-- Locations employees
INSERT INTO locations_employees (employee_id, location_id) VALUES
(1, 1), (2, 1),
(3, 2),
(4, 3), (5, 3),
(6, 4), (7, 4),
(8, 5), (9, 5);

-- Employee specializations
INSERT INTO employee_specializations (employee_id, specialization_id) VALUES
(1, 1), (1, 8),
(2, 2),
(3, 3),
(4, 2),
(5, 1),
(6, 3),
(7, 3),
(8, 4), (8, 5),
(9, 4);

-- Employee time slots
INSERT INTO employee_time_slots (employee_id, slot_day, start_time, end_time, is_booked) VALUES
(1, '2024-12-10', '10:00', '11:00', TRUE),
(1, '2024-12-10', '11:00', '12:00', FALSE),
(1, '2024-12-10', '13:00', '14:00', FALSE),
(2, '2024-12-10', '14:00', '15:00', TRUE),
(2, '2024-12-10', '15:00', '16:00', FALSE),
(3, '2024-12-11', '11:00', '12:00', TRUE),
(3, '2024-12-11', '12:00', '13:00', FALSE),
(4, '2024-12-12', '09:00', '10:00', TRUE),
(4, '2024-12-12', '10:00', '11:00', FALSE);

-- Employee pricing
INSERT INTO employee_pricing (employee_id, treatment_id, location_id, price_per_hour) VALUES
(1, 1, 1, 650.00),
(1, 2, 1, 950.00),
(1, 14, 1, 300.00),
(1, 15, 1, 450.00),
(2, 3, 1, 850.00),
(2, 4, 1, 950.00),
(3, 5, 2, 450.00),
(3, 6, 2, 600.00),
(3, 7, 2, 600.00),
(4, 3, 3, 850.00),
(4, 4, 3, 950.00),
(5, 2, 3, 950.00),
(6, 5, 4, 450.00),
(6, 6, 4, 600.00),
(6, 7, 4, 600.00),
(7, 5, 4, 450.00),
(7, 7, 4, 600.00),
(8, 8, 5, 650.00),
(8, 9, 5, 450.00),
(8, 10, 5, 1200.00),
(9, 8, 5, 650.00),
(9, 9, 5, 450.00),
(9, 11, 5, 1500.00);