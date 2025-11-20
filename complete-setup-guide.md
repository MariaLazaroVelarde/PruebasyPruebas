# Complete Guide: Running the Teacher Management Application with Tests

## Overview

This document provides step-by-step instructions for running the complete Teacher Management application with all tests. The application consists of:
- Spring Boot backend (port 8080)
- Angular frontend (port 4201)
- Functional tests with Selenium
- Security tests with OWASP ZAP

## Prerequisites

1. **Java 17+** installed
2. **Node.js 16+** installed
3. **Python 3.7+** installed
4. **Google Chrome** browser installed
5. **Git** (optional, for version control)

## Directory Structure

```
d:\Pruebas\
├── src\main\java\vallegrande\edu\pe\Pruebas\  (Spring Boot backend)
├── angular-frontend\                         (Angular frontend)
├── selenium-test.py                          (Selenium functional tests)
├── owasp-zap-security-test.py                (OWASP ZAP security tests)
├── simple-selenium-test.py                   (Simple Selenium test)
├── selenium-requirements.txt                 (Python dependencies)
├── pom.xml                                   (Maven configuration)
└── mvnw                                      (Maven wrapper)
```

## Step 1: Start the Spring Boot Backend

### Open Command Prompt/Terminal:
```bash
cd d:\Pruebas
```

### Run the backend application:
```bash
./mvnw spring-boot:run
```

### Expected Output:
```
Tomcat started on port(s): 8080 (http)
Started PruebasApplication in X.XXX seconds
```

### Verification:
Open your browser and navigate to `http://localhost:8080/api/teachers`
You should see a JSON response with teacher data.

## Step 2: Start the Angular Frontend

### Open a NEW Command Prompt/Terminal:
```bash
cd d:\Pruebas\angular-frontend
```

### Install Angular dependencies (first time only):
```bash
npm install
```

### Run the frontend application:
```bash
ng serve --port 4201
```

### Expected Output:
```
Angular Live Development Server is listening on localhost:4201
Compiled successfully.
```

### Verification:
Open your browser and navigate to `http://localhost:4201`
You should see the Teacher Management application interface.

## Step 3: Run Functional Tests with Selenium

### Open a NEW Command Prompt/Terminal:
```bash
cd d:\Pruebas
```

### Install Python dependencies (first time only):
```bash
pip install -r selenium-requirements.txt
```

### Run the simple Selenium test:
```bash
python simple-selenium-test.py
```

### Expected Output:
```
Starting Simple Selenium Test for Teacher Management Application
============================================================
=== Simple Test: Opening the application ===
✅ Application page loaded successfully
✅ Angular application is running
✅ Simple test completed successfully
WebDriver closed
```

### Run the comprehensive Selenium test:
```bash
python selenium-test.py
```

### Expected Output:
```
Starting Selenium Functional Tests for Teacher Management Application
======================================================================
=== Test 1: Opening the application ===
✅ Application opened successfully

=== Test 2: Verifying teacher list ===
✅ Teacher list loaded successfully with X teachers

=== Test 3: Creating a new teacher ===
✅ Teacher form submitted successfully

=== Test 4: Verifying new teacher in list ===
✅ Teacher list updated. Total teachers now: X+1

=== Test 5: Testing form validation ===
✅ Form validation working. Found X validation errors

=== All tests completed ===
WebDriver closed
```

## Step 4: Run Security Tests

### Prerequisites for Security Testing:
1. Download and install **OWASP ZAP** from https://www.zaproxy.org/download/
2. Start OWASP ZAP (make sure it's running on port 8080 by default)

### Open a NEW Command Prompt/Terminal:
```bash
cd d:\Pruebas
```

### Run the OWASP ZAP security test:
```bash
python owasp-zap-security-test.py
```

### Expected Output:
```
Starting OWASP ZAP Security Tests for Spring Boot + Angular Application
======================================================================
✅ OWASP ZAP is accessible

=== Accessing Target Application ===
✅ Accessed http://localhost:8080 through ZAP proxy
✅ Accessed http://localhost:4201 through ZAP proxy

=== Spidering http://localhost:8080 ===
✅ Spider started with scan ID: 1
   Spider progress: 0%
   Spider progress: 50%
   Spider progress: 100%
✅ Spidering completed

=== Active Scanning http://localhost:8080 ===
✅ Active scan started with scan ID: 2
   Scan progress: 0%
   Scan progress: 50%
   Scan progress: 100%
✅ Active scanning completed

=== Retrieving Security Alerts ===
✅ Found X alerts

======================================================================
OWASP ZAP Security Testing Complete
```

## Step 5: Verify Integration Between Components

### Check that all components are working together:

1. **Backend API**: `http://localhost:8080/api/teachers` should return JSON data
2. **Frontend UI**: `http://localhost:4201` should display the application
3. **Frontend-Backend Communication**: Teacher data should load in the frontend
4. **Functional Tests**: Selenium tests should pass
5. **Security Tests**: OWASP ZAP should be able to access and scan the applications

### Test Data Flow:
1. Create a new teacher through the frontend form
2. Verify the teacher appears in the list
3. Check that the data is stored in the backend by accessing the API directly
4. Run Selenium tests to automate this process

## Troubleshooting Common Issues

### Issue 1: Port Conflicts
**Problem**: "Port already in use" error
**Solution**: 
- Kill processes using the ports:
  ```bash
  # Windows
  netstat -ano | findstr :8080
  taskkill /PID <PID> /F
  ```

### Issue 2: Dependencies Not Found
**Problem**: "Module not found" or "Command not found" errors
**Solution**:
- Install missing dependencies:
  ```bash
  npm install -g @angular/cli
  pip install selenium requests
  ```

### Issue 3: ChromeDriver Issues
**Problem**: Selenium tests fail with ChromeDriver errors
**Solution**:
- Update ChromeDriver or use webdriver-manager:
  ```bash
  pip install webdriver-manager
  ```

### Issue 4: CORS Errors
**Problem**: Frontend cannot access backend APIs
**Solution**:
- Verify the backend has CORS configured (should already be configured in WebConfig.java)
- Check that both applications are running on their respective ports

### Issue 5: OWASP ZAP Connection Issues
**Problem**: Security tests fail to connect to ZAP
**Solution**:
- Ensure OWASP ZAP is running
- Check that ZAP is listening on port 8080
- Restart ZAP if needed

## Complete Test Execution Sequence

### 1. Preparation Phase:
```bash
# Terminal 1: Start backend
cd d:\Pruebas
./mvnw spring-boot:run

# Terminal 2: Start frontend
cd d:\Pruebas\angular-frontend
ng serve --port 4201

# Terminal 3: Prepare tests
cd d:\Pruebas
pip install -r selenium-requirements.txt
```

### 2. Functional Testing Phase:
```bash
# Terminal 3: Run tests
python simple-selenium-test.py
python selenium-test.py
```

### 3. Security Testing Phase:
```bash
# Start OWASP ZAP manually
# Then run:
python owasp-zap-security-test.py
```

## Expected Results Summary

When everything is working correctly, you should see:

1. **Backend**: Running on http://localhost:8080 with REST API accessible
2. **Frontend**: Running on http://localhost:4201 with UI accessible
3. **Functional Tests**: All Selenium tests passing
4. **Security Tests**: OWASP ZAP able to scan and report findings
5. **Integration**: Frontend successfully communicating with backend

## Next Steps After Successful Setup

1. **Customize Test Data**: Modify the test scripts to use your specific test data
2. **Add More Tests**: Extend the Selenium scripts for additional test cases
3. **Review Security Findings**: Address any vulnerabilities identified by OWASP ZAP
4. **Document Results**: Create screenshots and reports of your test execution
5. **Automate Execution**: Create batch scripts to run all components together

## Batch Script for Easy Execution (Windows)

Create a file named `start-all.bat` in `d:\Pruebas\`:

```batch
@echo off
echo Starting Teacher Management Application with Tests
echo ================================================

echo Starting Spring Boot Backend...
start "Backend" cmd /k "cd /d d:\Pruebas && ./mvnw spring-boot:run"

timeout /t 10

echo Starting Angular Frontend...
start "Frontend" cmd /k "cd /d d:\Pruebas\angular-frontend && ng serve --port 4201"

timeout /t 10

echo Opening Applications in Browser...
start http://localhost:8080/api/teachers
start http://localhost:4201

echo Setup Complete!
echo Backend: http://localhost:8080
echo Frontend: http://localhost:4201
echo.
echo Run tests in a new terminal:
echo cd d:\Pruebas
echo python simple-selenium-test.py
```

## Conclusion

This guide provides a complete walkthrough for running the Teacher Management application with all tests. Follow the steps in order, and you should have a fully functional system with automated testing capabilities.

Remember to:
1. Start components in the correct order
2. Use separate terminal windows for each component
3. Verify each component is working before proceeding
4. Run tests after all components are fully started
5. Check the troubleshooting section if you encounter issues