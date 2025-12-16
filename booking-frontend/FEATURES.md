# Bokadirekt Frontend - Feature Summary

## Overview
Professional React + TypeScript frontend for booking treatments, inspired by Bokadirekt.se. The application features a clean, modern design with full booking management capabilities.

## Implemented Features

### 1. Demo Login System
- **Auto-login**: Users are automatically logged in as demo customer "Anna Andersson"
- **No authentication required**: Simplified demo experience
- **User context**: Available throughout the app via `useAuth()` hook
- **User display**: Name shown in header on desktop view

**Demo User Details:**
- Name: Anna Andersson
- Email: anna.andersson@email.se
- Phone: 070-1234567
- Customer ID: 1

### 2. Search Functionality
**Fixed Issues:**
- Header search bar now properly navigates to treatments page with search query
- Home page hero search functional with both treatment and location filters
- Treatments page reads URL parameters and filters results
- Search works by treatment name AND description (accurate matching)

**How it works:**
- Type query in search bar → Press enter or click search
- Navigates to `/treatments?q=your-query&location=your-location`
- Results filter by matching treatment names and descriptions

### 3. Category Filtering
**Fixed Issues:**
- Category tabs properly filter treatments
- "Alla" (All) tab shows all treatments
- Clicking category in navigation or on home page navigates to filtered view
- URL-based filtering persists on page refresh

**Categories Available:**
1. Alla (All treatments)
2. Hår (Hair)
3. Massage
4. Naglar (Nails)
5. Ansiktsbehandling (Facial)
6. Spa
7. Makeup
8. Vaxning (Waxing)

### 4. My Bookings Page
**Path:** `/account/bookings`

**Features:**
- Displays all bookings for the logged-in customer
- Separated into "Kommande" (Upcoming) and "Tidigare" (Past) bookings
- Shows booking details:
  - Date and time
  - Treatment name and description
  - Location address
  - Booking status (Confirmed, Cancelled, Pending)
  - Customer notes
- Actions available:
  - View treatment details
  - Cancel booking (for confirmed bookings)

**Backend Integration:**
- New endpoint: `GET /customers/{customer_id}/bookings`
- Returns bookings sorted by date (newest first)

### 5. My Favorites Page
**Path:** `/favorites`

**Features:**
- View all favorited treatments
- Favorite treatments are saved to localStorage
- Shows treatment cards with:
  - Image
  - Category badge
  - Name and description
  - Duration and price
  - Favorite button (filled heart)
- Click heart to remove from favorites
- Direct booking from favorites page

**How to Add Favorites:**
- Browse treatments page
- Click the heart icon on any treatment card
- Treatment is saved to favorites

### 6. Support Page
**Path:** `/support`

**Features:**
- **Contact Support Form:**
  - Select category (Booking, Payment, Account, Technical, Other)
  - Enter subject and detailed message
  - Submit ticket (demo - shows success message)

- **My Tickets Section:**
  - View submitted support tickets
  - Shows ticket status (Open, In Progress, Resolved)
  - Displays ticket details and timestamps

- **Direct Contact Info:**
  - Phone: 08-123 456 78 (Mon-Fri 9-17)
  - Email: support@bokadirekt.se (responds within 24h)

- **FAQ Section:**
  - Common questions answered
  - Quick help without submitting ticket

### 7. Enhanced Header
**Features:**
- User profile button shows user's first name (desktop)
- Dropdown menu with user info:
  - Full name and email displayed
  - Links to:
    - My Account
    - My Bookings
    - Favorites
    - Settings
    - Logout
- Quick access icons:
  - Calendar (My Bookings)
  - Heart (Favorites)

### 8. Updated Footer
**Fixed Links:**
- "Mina bokningar" → `/account/bookings`
- "Mina favoriter" → `/favorites`
- "Support" → `/support`

## Technical Implementation

### State Management
- **React Query**: Data fetching and caching for treatments, categories, locations
- **React Context**: Authentication state (demo user)
- **localStorage**: Favorites persistence

### Routing
All routes in [App.tsx](src/App.tsx):
- `/` - Home page
- `/treatments` - All treatments (with search/filter)
- `/categories/:categoryId` - Category-specific treatments
- `/treatment/:treatmentId` - Treatment details and booking
- `/account` - Account overview
- `/account/bookings` - My Bookings
- `/favorites` - My Favorites
- `/support` - Support & Help

### New Components
1. **AuthContext** - Demo user authentication
2. **MyBookings** - Customer bookings management
3. **MyFavorites** - Favorited treatments
4. **Support** - Support ticket system

### API Integration
- Fixed field name mismatches between backend and frontend
- Added customer bookings endpoint to backend
- All data properly typed with TypeScript interfaces

## How to Use

### Starting the Application
1. **Start Backend:**
   ```bash
   python app.py
   ```
   Backend runs on http://127.0.0.1:8000

2. **Start Frontend:**
   ```bash
   cd booking-frontend
   npm run dev
   ```
   Frontend runs on http://localhost:5175

### Testing Features
1. **Browse Treatments:**
   - Click on category cards on home page
   - Use category tabs on treatments page
   - Search for treatments by name (e.g., "massage", "klippning")

2. **Add Favorites:**
   - Go to treatments page
   - Click heart icon on any treatment
   - View in "Mina favoriter" from header menu

3. **View Bookings:**
   - Click calendar icon in header OR
   - Click user menu → "Mina bokningar"
   - See demo customer's existing bookings

4. **Contact Support:**
   - Click "Support" in footer
   - Fill out support form
   - View existing tickets

## Design Features
- **Professional Bokadirekt-inspired design**
- **Teal/blue color scheme** (#2b6777, #52ab98)
- **Clean card-based layouts**
- **Hover effects and smooth transitions**
- **Fully responsive** (mobile, tablet, desktop)
- **Swedish language** throughout

## Known Demo Limitations
1. Authentication is auto-login only (no real login/logout)
2. Support tickets are demo only (not saved to database)
3. Favorites are localStorage only (not synced across devices)
4. Booking cancellation is UI-only (would need backend confirmation)

All core functionality is implemented and working for professional demonstration purposes.
