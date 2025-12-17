-- ENHANCED SQL INSERTS FOR PROFESSIONAL DEMO
-- This file adds more realistic and comprehensive data

-- Gender types
INSERT INTO gender_types (gender_types) VALUES
('Man'),
('Kvinna'),
('Icke-binär'),
('Vill ej uppge');

-- Users (Extended with more variety)
INSERT INTO users (email, password, first_name, last_name, phone_number, date_of_birth, gender_id, profile_photo) VALUES
('anna.andersson@email.com', 'hashed_pw_1', 'Anna', 'Andersson', '0701234567', '1990-05-15', 2, NULL),
('erik.eriksson@email.com', 'hashed_pw_2', 'Erik', 'Eriksson', '0701234568', '1985-08-22', 1, NULL),
('maria.karlsson@email.com', 'hashed_pw_3', 'Maria', 'Karlsson', '0701234569', '1992-11-30', 2, NULL),
('johan.nilsson@email.com', 'hashed_pw_4', 'Johan', 'Nilsson', '0701234570', '1988-03-12', 1, NULL),
('lisa.svensson@email.com', 'hashed_pw_5', 'Lisa', 'Svensson', '0701234571', '1995-07-08', 2, NULL),
('peter.olsson@email.com', 'hashed_pw_6', 'Peter', 'Olsson', '0701234572', '1987-12-19', 1, NULL),
('sara.gustafsson@email.com', 'hashed_pw_7', 'Sara', 'Gustafsson', '0701234573', '1993-04-25', 2, NULL),
('mikael.larsson@email.com', 'hashed_pw_8', 'Mikael', 'Larsson', '0701234574', '1991-09-14', 1, NULL),
('emma.berg@email.com', 'hashed_pw_9', 'Emma', 'Berg', '0701234575', '1989-06-07', 2, NULL),
('david.lundgren@email.com', 'hashed_pw_10', 'David', 'Lundgren', '0701234576', '1994-01-23', 1, NULL),
('karin.johansson@email.com', 'hashed_pw_11', 'Karin', 'Johansson', '0701234577', '1986-05-10', 2, NULL),
('anders.andersson@email.com', 'hashed_pw_12', 'Anders', 'Andersson', '0701234578', '1990-08-15', 1, NULL),
('sofia.lindberg@email.com', 'hashed_pw_13', 'Sofia', 'Lindberg', '0701234579', '1996-02-20', 2, NULL),
('oscar.berg@email.com', 'hashed_pw_14', 'Oscar', 'Berg', '0701234580', '1984-11-05', 1, NULL),
('jenny.hall@email.com', 'hashed_pw_15', 'Jenny', 'Hall', '0701234581', '1998-07-12', 2, NULL);

-- Businesses (More descriptive)
INSERT INTO businesses (business_name, email, phone_number, about_text) VALUES
('Glam Beauty Lounge', 'info@glambeauty.se', '08-1234567', 'Stockholms mest exklusiva skönhetssalong. Vi erbjuder premium behandlingar i en lyxig miljö med erfarna specialister.'),
('Urban Cuts Stockholm', 'kontakt@urbancuts.se', '08-7654321', 'Modern hårsalong i city med fokus på de senaste trenderna och hållbara produkter.'),
('Serenity Spa Göteborg', 'info@serenityspa.se', '031-9876543', 'Avkoppling och välmående i världsklass. Vårt spa erbjuder allt från massage till ansiktsbehandlingar.'),
('NailArt Studio', 'hello@nailart.se', '08-5556789', 'Sveriges ledande nagelsalong med spetskompetens inom gellack, nagelförlängning och nail art.'),
('Zen Massage Malmö', 'info@zenmassage.se', '040-5551234', 'Professionell massage i lugn och ro. Specialiserade på rygg, nacke och helkroppsmassage.');

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
(6, 750.00),
(7, 200.00),
(8, 0.00),
(9, 350.00),
(10, 100.00);

-- Booking statuses
INSERT INTO booking_statuses (status_name) VALUES
('Bekräftad'),
('Avbokad'),
('Genomförd'),
('Inställd'),
('Väntande');

-- Business locations
INSERT INTO business_locations (business_id, phone_number, email, street_address, city, postal_code, country, longitude, latitude) VALUES
(1, '08-1234567', 'ostermalm@glambeauty.se', 'Strandvägen 12', 'Stockholm', '11451', 'Sverige', 18.0875490, 59.3326090),
(1, '08-1234568', 'sodermalm@glambeauty.se', 'Götgatan 45', 'Stockholm', '11621', 'Sverige', 18.0709140, 59.3142340),
(2, '08-7654321', 'vasastan@urbancuts.se', 'Odengatan 82', 'Stockholm', '11322', 'Sverige', 18.0504650, 59.3438880),
(3, '031-9876543', 'info@serenityspa.se', 'Avenyn 28', 'Göteborg', '41136', 'Sverige', 11.9745620, 57.7007470),
(4, '08-5556789', 'info@nailart.se', 'Drottninggatan 95', 'Stockholm', '11360', 'Sverige', 18.0620720, 59.3375150),
(5, '040-5551234', 'info@zenmassage.se', 'Stortorget 7', 'Malmö', '21122', 'Sverige', 13.0007310, 55.6048660);

-- Employees
INSERT INTO employees (user_id, business_id, location_id, rating) VALUES
(7, 1, 1, 5),
(8, 1, 1, 4),
(9, 1, 2, 5),
(11, 2, 3, 5),
(12, 3, 4, 4),
(13, 4, 5, 5),
(14, 5, 6, 5);

-- Images
INSERT INTO images (business_id, employee_id, location_id, image_url) VALUES
(1, NULL, 1, 'https://images.unsplash.com/photo-1560066984-138dadb4c035?w=800'),
(1, NULL, 2, 'https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?w=800'),
(2, NULL, 3, 'https://images.unsplash.com/photo-1562322140-8baeececf3df?w=800'),
(3, NULL, 4, 'https://images.unsplash.com/photo-1540555700478-4be289fbecef?w=800'),
(4, NULL, 5, 'https://images.unsplash.com/photo-1604654894610-df63bc536371?w=800'),
(5, NULL, 6, 'https://images.unsplash.com/photo-1544161515-4ab6ce6db874?w=800');

-- Treatments (Significantly expanded)
INSERT INTO treatments (treatment_name, treatment_description, category_id, image_id, time_duration, last_min_deal) VALUES
-- Hår (Category 1)
('Damklippning', 'Professionell klippning med konsultation, tvätt, klippning och styling. Våra erfarna frisörer hjälper dig hitta den perfekta frisyren.', 1, 1, 60, FALSE),
('Herrklippning', 'Herrklippning med tvätt, klippning och styling. Inkluderar trimning av skägg om så önskas.', 1, 1, 45, FALSE),
('Barnklippning', 'Mjuk och omtänksam klippning för barn upp till 12 år i en barnvänlig miljö.', 1, 1, 30, TRUE),
('Helförgning', 'Komplett färgbehandling med premium färg och eftervård. Inkluderar toning för perfekt resultat.', 1, 1, 120, FALSE),
('Highlights/Slingor', 'Slingor eller highlights enligt önskemål med balayage- eller folieteknik.', 1, 1, 90, FALSE),
('Permanent/Behandling', 'Keratinbehandling, permanent eller annan hårbehandling för mjukt och friskt hår.', 1, 1, 90, FALSE),
('Uppsättning', 'Professionell uppsättning för fest, bröllop eller andra tillfällen.', 1, 1, 60, FALSE),
('Hårförlängning Konsultation', 'Kostnadsfri konsultation för hårförlängning med extensions eller tejp.', 1, 1, 30, FALSE),

-- Naglar (Category 2)
('Manikyr', 'Klassisk manikyr med nagelbandspushning, formning och lack.', 2, 5, 45, FALSE),
('Gellack Händer', 'Gellack på naturliga naglar med formning och finish. Håller i 2-3 veckor.', 2, 5, 60, FALSE),
('Gellack Fötter', 'Pedikyr med gellack, perfekt för sommarens sandaler.', 2, 5, 60, FALSE),
('Nagel Förlängning Gel', 'Nagelförlängning med gel, inklusive formning och finish.', 2, 5, 90, FALSE),
('Nagel Förlängning Akryl', 'Akrylnaglar med valfri längd och form. Håller extra länge.', 2, 5, 90, FALSE),
('Nail Art', 'Kreativ nail art med mönster, glitter eller 3D-dekorationer.', 2, 5, 30, TRUE),
('French Manicure', 'Klassisk french manicure med vit spets och naturlig nagelbädd.', 2, 5, 60, FALSE),

-- Ansiktsbehandling (Category 3)
('Ansiktsbehandling Basic', 'Grundläggande ansiktsbehandling med rengöring, peeling och mask för alla hudtyper.', 3, 1, 60, FALSE),
('Ansiktsbehandling Lyx', 'Lyxig ansiktsbehandling med djuprengöring, massage, mask och serum. Inkluderar ögon- och läppvård.', 3, 1, 90, FALSE),
('Hydrafacial', 'Revolutionerande behandling som rengör, exfolierar och återfuktar huden på djupet.', 3, 1, 60, FALSE),
('Microneedling', 'Anti-age behandling som stimulerar kollagenproduktionen för fastare och jämnare hud.', 3, 1, 75, FALSE),
('Kemisk Peeling', 'Professionell kemisk peeling för förnyad och strålande hud.', 3, 1, 45, FALSE),
('LED-ljusbehandling', 'Behandling med LED-ljus för att minska akne, rynkor och pigmentfläckar.', 3, 1, 30, TRUE),

-- Massage (Category 4)
('Ryggmassage 30min', 'Avslappnande ryggmassage som löser upp spänningar i rygg och nacke.', 4, 6, 30, TRUE),
('Ryggmassage 50min', 'Fördjupad ryggmassage med extra fokus på problemområden.', 4, 6, 50, FALSE),
('Helkroppsmassage', 'Klassisk svensk massage av hela kroppen för total avslappning.', 4, 6, 90, FALSE),
('Djupvävnadsmassage', 'Intensiv massage som arbetar på djupare muskellager. Perfekt för kroniska spänningar.', 4, 6, 75, FALSE),
('Hot Stone Massage', 'Massage med varma stenar som värmer upp musklerna och ökar avslappningen.', 4, 6, 90, FALSE),
('Thailändsk Massage', 'Traditionell thailändsk massage med stretching och tryckpunktsbehandling.', 4, 6, 60, FALSE),
('Aromaterapi Massage', 'Massage med aromatiska oljor anpassade efter dina behov.', 4, 6, 75, FALSE),

-- Spa (Category 5)
('Spa-paket Halvdag', 'Halvdagspaket med ansiktsbehandling, massage och tillgång till relaxavdelning.', 5, 4, 150, FALSE),
('Spa-paket Heldag', 'Heldagspaket med flera behandlingar, lunch och full tillgång till spa-anläggningen.', 5, 4, 240, FALSE),
('Bastu & Relax', 'Tillgång till bastu, relaxavdelning och te/frukt i 2 timmar.', 5, 4, 120, TRUE),

-- Makeup (Category 6)
('Dagmakeup', 'Naturlig och fräsch makeup för vardag eller kontor.', 6, 1, 45, FALSE),
('Festmakeup', 'Makeup för fest, middag eller andra speciella tillfällen.', 6, 1, 60, FALSE),
('Brudmakeup', 'Professionell makeup för bröllopsdagen med provsminking.', 6, 1, 90, FALSE),
('Makeup Lektion', 'Lär dig göra din egen makeup med proffsens tips och tricks.', 6, 1, 90, FALSE),

-- Vaxning (Category 7)
('Vaxning Överläpp', 'Snabb och skonsam vaxning av överläppen.', 7, 1, 15, TRUE),
('Vaxning Ben Helt', 'Vaxning av hela benen från tår till lår.', 7, 1, 45, FALSE),
('Vaxning Ben Halva', 'Vaxning av underbenen eller bara låren.', 7, 1, 30, TRUE),
('Vaxning Bikinilinje', 'Vaxning längs bikinilinjen, klassisk form.', 7, 1, 30, FALSE),
('Vaxning Brazilian', 'Komplett vaxning av bikiniområdet.', 7, 1, 45, FALSE),
('Vaxning Armhålor', 'Snabb vaxning av armhålorna.', 7, 1, 15, TRUE),
('Vaxning Rygg/Bröst', 'Vaxning av rygg eller bröst för män.', 7, 1, 45, FALSE);

-- Bookings (More varied for demo)
INSERT INTO bookings (location_id, treatment_id, customer_id, employee_id, business_id, booked_date, time_start, time_stop, notes, booking_status, payment_confirmed) VALUES
(1, 1, 1, 1, 1, '2025-12-20', '10:00', '11:00', 'Vill ha lugg', 1, TRUE),
(1, 4, 2, 1, 1, '2025-12-20', '14:00', '16:00', 'Blond färg', 1, TRUE),
(2, 9, 3, 3, 1, '2025-12-21', '11:00', '11:45', NULL, 1, TRUE),
(3, 2, 4, 4, 2, '2025-12-21', '15:00', '15:45', 'Kort klippning', 1, TRUE),
(4, 18, 5, 5, 3, '2025-12-22', '13:00', '14:30', NULL, 1, TRUE),
(1, 16, 6, 2, 1, '2025-12-23', '10:00', '11:30', NULL, 1, FALSE),
(2, 10, 1, 3, 1, '2025-12-25', '09:00', '10:00', NULL, 1, TRUE),
(5, 13, 3, 6, 4, '2025-12-27', '14:00', '15:30', 'Första gången', 1, TRUE),
(1, 5, 7, 1, 1, '2026-01-05', '11:00', '12:30', 'Balayage', 1, TRUE),
(2, 10, 8, 3, 1, '2026-01-06', '10:00', '11:00', NULL, 1, TRUE),
(4, 26, 9, 5, 3, '2026-01-08', '15:00', '16:30', NULL, 5, FALSE),
(3, 2, 10, 4, 2, '2026-01-10', '09:00', '09:45', NULL, 1, TRUE);

-- Favorites
INSERT INTO favorites (treatment_id, customer_id, location_id, employee_id) VALUES
(1, 1, 1, 1),
(4, 1, 1, 1),
(9, 3, 2, 3),
(18, 5, 4, 5),
(2, 4, 3, 4),
(16, 6, 1, 2),
(10, 1, 2, 3),
(26, 3, 4, 5),
(5, 7, 1, 1),
(13, 9, 5, 6);

-- Reviews
INSERT INTO reviews (booking_id, customer_id, employee_id, location_id, treatment_id, overall_rating, location_rating, employee_rating, treatment_rating, review_comment) VALUES
(1, 1, 1, 1, 1, 5, 5, 5, 5, 'Fantastisk klippning! Sara är duktig och lyssnar på mina önskemål.'),
(2, 2, 1, 1, 4, 4, 5, 4, 4, 'Bra färgning men tog lite längre tid än planerat'),
(3, 3, 3, 2, 9, 5, 4, 5, 5, 'Mycket nöjd med manikyr! Emma är proffs.'),
(4, 4, 4, 3, 2, 4, 4, 4, 4, 'Bra klippning, trevlig personal'),
(5, 5, 5, 4, 18, 5, 5, 5, 5, 'Bästa massagen jag fått! Kommer definitivt tillbaka.'),
(8, 3, 6, 5, 13, 5, 5, 5, 5, 'Helt underbar nagelförlängning! Ser så naturliga ut.');

-- Location treatments
INSERT INTO location_treatments (location_id, treatment_id) VALUES
-- Glam Beauty Lounge Östermalm (loc 1)
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8),
(1, 16), (1, 17), (1, 18), (1, 19), (1, 20), (1, 21),
(1, 31), (1, 32), (1, 33), (1, 34),
-- Glam Beauty Lounge Södermalm (loc 2)
(2, 1), (2, 2), (2, 3), (2, 9), (2, 10), (2, 11),
(2, 37), (2, 38), (2, 39), (2, 40), (2, 41), (2, 42),
-- Urban Cuts (loc 3)
(3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7),
-- Serenity Spa (loc 4)
(4, 16), (4, 17), (4, 18), (4, 19),
(4, 22), (4, 23), (4, 24), (4, 25), (4, 26), (4, 27), (4, 28),
(4, 29), (4, 30),
-- NailArt Studio (loc 5)
(5, 9), (5, 10), (5, 11), (5, 12), (5, 13), (5, 14), (5, 15),
-- Zen Massage (loc 6)
(6, 22), (6, 23), (6, 24), (6, 25), (6, 26), (6, 27), (6, 28);

-- Employee treatments
INSERT INTO employee_treatments (treatment_id, employee_id) VALUES
(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1),
(9, 2), (10, 2), (11, 2), (16, 2), (17, 2),
(1, 3), (2, 3), (9, 3), (10, 3), (37, 3), (38, 3),
(1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4),
(16, 5), (17, 5), (22, 5), (23, 5), (24, 5), (25, 5), (26, 5),
(9, 6), (10, 6), (11, 6), (12, 6), (13, 6), (14, 6), (15, 6),
(22, 7), (23, 7), (24, 7), (25, 7), (26, 7), (27, 7), (28, 7);

-- Owners
INSERT INTO owners (business_id, user_id) VALUES
(1, 7),
(2, 11),
(3, 12),
(4, 13),
(5, 14);

-- Opening hours (All locations)
INSERT INTO opening_hours (location_id, day_of_week, open_time, close_time) VALUES
(1, 1, '09:00', '18:00'), (1, 2, '09:00', '18:00'), (1, 3, '09:00', '18:00'),
(1, 4, '09:00', '20:00'), (1, 5, '09:00', '18:00'), (1, 6, '10:00', '16:00'),
(2, 1, '10:00', '19:00'), (2, 2, '10:00', '19:00'), (2, 3, '10:00', '19:00'),
(2, 4, '10:00', '20:00'), (2, 5, '10:00', '19:00'), (2, 6, '10:00', '17:00'),
(3, 1, '09:00', '17:00'), (3, 2, '09:00', '17:00'), (3, 3, '09:00', '17:00'),
(3, 4, '09:00', '19:00'), (3, 5, '09:00', '17:00'), (3, 6, '10:00', '15:00'),
(4, 1, '10:00', '20:00'), (4, 2, '10:00', '20:00'), (4, 3, '10:00', '20:00'),
(4, 4, '10:00', '20:00'), (4, 5, '10:00', '20:00'), (4, 6, '09:00', '18:00'), (4, 0, '10:00', '17:00'),
(5, 1, '10:00', '19:00'), (5, 2, '10:00', '19:00'), (5, 3, '10:00', '19:00'),
(5, 4, '10:00', '20:00'), (5, 5, '10:00', '19:00'), (5, 6, '11:00', '17:00'),
(6, 1, '09:00', '20:00'), (6, 2, '09:00', '20:00'), (6, 3, '09:00', '20:00'),
(6, 4, '09:00', '21:00'), (6, 5, '09:00', '20:00'), (6, 6, '10:00', '18:00'), (6, 0, '11:00', '17:00');

-- Locations employees
INSERT INTO locations_employees (employee_id, location_id) VALUES
(1, 1), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6);

-- Employee pricing (Sample pricing)
INSERT INTO employee_pricing (employee_id, treatment_id, location_id, price_per_hour) VALUES
(1, 1, 1, 650.00), (1, 2, 1, 500.00), (1, 4, 1, 1200.00), (1, 5, 1, 900.00),
(2, 9, 1, 450.00), (2, 10, 1, 550.00), (2, 16, 1, 750.00),
(3, 1, 2, 600.00), (3, 9, 2, 450.00), (3, 37, 2, 400.00),
(4, 1, 3, 550.00), (4, 2, 3, 400.00), (4, 4, 3, 1100.00),
(5, 16, 4, 750.00), (5, 22, 4, 600.00), (5, 24, 4, 950.00),
(6, 9, 5, 450.00), (6, 10, 5, 550.00), (6, 12, 5, 800.00),
(7, 22, 6, 600.00), (7, 24, 6, 950.00), (7, 26, 6, 1000.00);
