# Booking Management System - React Frontend

This is a React frontend application for the Booking Management System, built with Vite and React Router.

## Features

- Treatment management (CRUD operations)
- User management (create, update, delete users)
- Customer management
- Business management
- Modern, responsive UI
- RESTful API integration with FastAPI backend

## Prerequisites

- Node.js (v14 or higher)
- npm or yarn
- FastAPI backend running on `http://localhost:8000`

## Installation

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

## Running the Application

1. Make sure your FastAPI backend is running on port 8000

2. Start the development server:
```bash
npm run dev
```

3. Open your browser and navigate to:
```
http://localhost:5173
```

## Available Scripts

- `npm run dev` - Start the development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build locally

## Project Structure

```
frontend/
├── src/
│   ├── components/      # Reusable components
│   │   └── Navigation.jsx
│   ├── pages/          # Page components
│   │   ├── Home.jsx
│   │   ├── Treatments.jsx
│   │   ├── Users.jsx
│   │   ├── Customers.jsx
│   │   └── Businesses.jsx
│   ├── services/       # API service layer
│   │   └── api.js
│   ├── App.jsx         # Main app component
│   ├── App.css         # Global styles
│   └── main.jsx        # Entry point
├── public/             # Static assets
└── package.json
```

## API Endpoints Used

The frontend communicates with the following backend endpoints:

- `/treatments/` - GET, POST, PUT, DELETE
- `/treatment_categories/` - GET, POST
- `/users/` - GET, POST, PUT, DELETE
- `/customers/` - GET, POST, PUT, DELETE
- `/businesses/` - GET, POST, PUT
- `/business_locations/` - GET, POST, PUT
- `/employees/` - GET, POST, DELETE
- `/owners/` - GET, POST
- `/bookings/` - GET, POST, PATCH, DELETE

## Technologies Used

- React 18
- Vite
- React Router DOM
- Axios
- CSS3

## Notes

- The application uses CORS, make sure the backend allows requests from `http://localhost:5173`
- Error messages are displayed in the UI when API calls fail
- All forms include validation
