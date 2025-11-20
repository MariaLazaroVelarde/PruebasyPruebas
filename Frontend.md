# Frontend Implementation Guide

## Overview

This document describes the Angular frontend implementation for the Teacher Management application. The frontend is built with Angular and communicates with the Spring Boot backend through REST APIs.

## Technology Stack

- **Angular 16+**: Frontend framework
- **TypeScript**: Programming language
- **HTML/CSS**: Markup and styling
- **RxJS**: Reactive programming library
- **Angular CLI**: Development tool

## Project Structure

```
angular-frontend/
├── src/
│   ├── app/
│   │   ├── models/
│   │   │   └── teacher.model.ts
│   │   ├── services/
│   │   │   └── teacher.service.ts
│   │   ├── teacher-form/
│   │   │   ├── teacher-form.component.html
│   │   │   ├── teacher-form.component.ts
│   │   │   └── teacher-form.component.scss
│   │   ├── teacher-list/
│   │   │   ├── teacher-list.component.html
│   │   │   ├── teacher-list.component.ts
│   │   │   └── teacher-list.component.scss
│   │   ├── app.component.html
│   │   ├── app.component.ts
│   │   └── app.module.ts
│   ├── assets/
│   ├── environments/
│   └── index.html
├── package.json
└── angular.json
```

## Key Components

### 1. Teacher Model (teacher.model.ts)

Defines the structure of a Teacher object:

```typescript
export interface Teacher {
  id?: number;
  firstName: string;
  lastName: string;
  email: string;
  subject: string;
  yearsOfExperience: number;
}
```

### 2. Teacher Service (teacher.service.ts)

Handles all HTTP communication with the backend:

```typescript
@Injectable({
  providedIn: 'root'
})
export class TeacherService {
  private apiUrl = 'http://localhost:8080/api/teachers';

  constructor(private http: HttpClient) { }

  getAllTeachers(): Observable<Teacher[]> {
    return this.http.get<Teacher[]>(this.apiUrl);
  }

  getTeacherById(id: number): Observable<Teacher> {
    return this.http.get<Teacher>(`${this.apiUrl}/${id}`);
  }

  createTeacher(teacher: Teacher): Observable<Teacher> {
    return this.http.post<Teacher>(this.apiUrl, teacher);
  }

  updateTeacher(id: number, teacher: Teacher): Observable<Teacher> {
    return this.http.put<Teacher>(`${this.apiUrl}/${id}`, teacher);
  }

  deleteTeacher(id: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/${id}`);
  }
}
```

### 3. Teacher Form Component

Handles creating and editing teachers with form validation:

- Uses reactive forms with FormBuilder
- Implements form validation for all fields
- Handles both create and update operations
- Emits events when teachers are saved

### 4. Teacher List Component

Displays the list of teachers in a table format:

- Loads teachers from the service on initialization
- Handles delete operations with confirmation
- Emits events when a teacher is selected for editing

## Features Implemented

### 1. CRUD Operations

- **Create**: Add new teachers through the form
- **Read**: Display list of all teachers
- **Update**: Edit existing teachers
- **Delete**: Remove teachers with confirmation

### 2. Form Validation

- Required field validation for all fields
- Email format validation
- Numeric validation for years of experience
- Real-time validation feedback

### 3. Responsive Design

- Mobile-friendly layout
- Responsive table for teacher list
- Adaptive form layout

### 4. User Experience

- Loading indicators during data fetch
- Success/error notifications
- Confirmation dialogs for destructive actions
- Clear error messages

## Running the Application

### Development Server

```bash
cd angular-frontend
ng serve
```

The application will be available at http://localhost:4200 by default.

### Production Build

```bash
cd angular-frontend
ng build
```

The build artifacts will be stored in the `dist/` directory.

## Integration with Backend

The frontend communicates with the Spring Boot backend through REST APIs:

- **GET /api/teachers**: Retrieve all teachers
- **GET /api/teachers/{id}**: Retrieve a specific teacher
- **POST /api/teachers**: Create a new teacher
- **PUT /api/teachers/{id}**: Update an existing teacher
- **DELETE /api/teachers/{id}**: Delete a teacher

## Testing

### Unit Tests

Components and services are tested with Jasmine and Karma:

```bash
cd angular-frontend
ng test
```

### End-to-End Tests

E2E tests are implemented with Protractor:

```bash
cd angular-frontend
ng e2e
```

## Deployment

### Prerequisites

1. Node.js and npm installed
2. Angular CLI installed globally
3. Backend application running

### Steps

1. Install dependencies:
   ```bash
   cd angular-frontend
   npm install
   ```

2. Build for production:
   ```bash
   ng build --prod
   ```

3. Deploy the contents of the `dist/` folder to your web server

## Troubleshooting

### Common Issues

1. **CORS Errors**: Ensure the backend is configured to allow requests from the frontend origin
2. **API Connection Issues**: Verify the backend is running and accessible
3. **Form Validation**: Check that all required fields are filled correctly
4. **Loading Problems**: Verify network connectivity and backend availability

### Debugging Tips

1. Use browser developer tools to inspect network requests
2. Check the console for JavaScript errors
3. Verify API endpoints are returning expected data
4. Use Angular DevTools for component debugging