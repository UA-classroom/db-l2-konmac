# Booking Frontend - Professional Bokadirekt-Inspired UI

A modern, professional booking system frontend inspired by Bokadirekt.se, built with React, TypeScript, and Vite.

## Features

### User-Facing Features
- **Hero Homepage** with large search bar and category browsing
- **Category Grid** with beautiful image cards
- **Treatment Browsing** with search and filtering
- **Booking Flow** with step-by-step process
- **User Account Management** (My Bookings, Favorites, Profile)
- **Responsive Design** that works on all devices

### Technical Features
- React 18 with TypeScript
- React Router for navigation
- TanStack React Query for data fetching
- Axios for API calls
- Lucide React for icons
- Professional, clean UI inspired by Bokadirekt
- Fully responsive design

## Quick Start

### 1. Install Dependencies
```bash
npm install
```

### 2. Start the Development Server
```bash
npm run dev
```

The application will run on http://localhost:5175

### 3. Start the Backend
Make sure your FastAPI backend is running:
```bash
cd ..
uvicorn app:app --reload
```

## Project Structure

```
src/
├── components/          # Reusable components
│   ├── Header.tsx       # Navigation header with search
│   └── Footer.tsx       # Footer with links
├── pages/               # Page components
│   ├── Home.tsx         # Homepage with hero and categories
│   ├── Treatments.tsx   # Treatment browsing and search
│   ├── BookingPage.tsx  # Booking flow
│   └── MyAccount.tsx    # User account management
├── services/            # API service layer
│   └── api.ts           # Axios API calls
├── types/               # TypeScript interfaces
│   └── index.ts         # Type definitions
├── App.tsx              # Main app with routing
└── index.css            # Global styles
```

## Key Pages

### Home (`/`)
- Large hero section with search
- Category grid with images
- Clean, professional design

### Treatments (`/treatments`)
- Search functionality
- Category filtering
- Treatment cards with pricing and duration
- Click to book

### Booking Page (`/treatment/:id`)
- Treatment details
- Business/location selection
- Date and time picker
- Booking confirmation

### My Account (`/account`)
- My Bookings
- My Favorites
- Profile Settings

## Design Principles

Based on Bokadirekt.se:
- Clean, minimal white/light color scheme
- Teal/blue accent colors (#2b6777, #52ab98)
- Card-based layouts
- Professional typography
- Smooth transitions and hover effects
- Mobile-first responsive design

## Backend Integration

The frontend connects to your FastAPI backend at `http://127.0.0.1:8000`.

API endpoints used:
- `GET /treatment_categories/` - Fetch categories
- `GET /treatments/` - Fetch treatments
- `GET /businesses/` - Fetch businesses
- `GET /business_locations/` - Fetch locations
- `POST /bookings/` - Create booking

## Environment Variables

Create a `.env` file:
```
VITE_API_BASE_URL=http://127.0.0.1:8000
```

## Building for Production

```bash
npm run build
```

The build output will be in the `dist/` directory.

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Notes

- The user authentication is currently mocked (uses customer_id: 1)
- Images use Unsplash placeholders
- Some features like favorites and booking history are UI-only

Enjoy your professional booking system! 🎉
