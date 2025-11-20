# Teacher Management System - Angular Frontend

This is the Angular frontend for the Teacher Management System application.

## Prerequisites

- Node.js (version 16 or higher)
- npm (comes with Node.js)

## Setup

1. Navigate to the angular-frontend directory:
   ```
   cd angular-frontend
   ```

2. Install the dependencies:
   ```
   npm install
   ```

## Development Server

Run the development server:
```
npm start
```

The application will be available at `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

## Build

To build the project for production:
```
npm run build
```

The build artifacts will be stored in the `dist/` directory.

## Backend Integration

This frontend is designed to work with the Spring Boot backend. Make sure the backend is running on `http://localhost:8080/` for the API calls to work correctly.

## Features

- View list of all teachers
- Add new teachers
- Edit existing teachers
- Delete teachers
- Form validation
- Responsive design

## Project Structure

```
src/
├── app/
│   ├── models/              # Data models
│   ├── services/            # Services for API communication
│   ├── teacher-form/        # Component for teacher form
│   ├── teacher-list/        # Component for teacher list
│   ├── app.component.*      # Root component
│   └── app.module.ts        # Main application module
├── assets/                  # Static assets
├── environments/            # Environment configuration
└── styles.scss             # Global styles
```