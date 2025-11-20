"""
PRUEBAS DE SEGURIDAD PARA APLICACIONES SPRING BOOT + ANGULAR
"""

import requests
import json
import time
from urllib.parse import urljoin

class SpringBootSecurityTester:
    def __init__(self, base_url="http://localhost:8080"):
        self.base_url = base_url
        self.api_url = urljoin(base_url, "/api/teachers")
        self.session = requests.Session()
        
    def check_application_status(self):
        """Check if the application is running"""
        try:
            response = requests.get(self.base_url)
            if response.status_code == 200:
                print("✅ Application is accessible")
                return True
            else:
                print(f"❌ Application returned status code: {response.status_code}")
                return False
        except requests.exceptions.ConnectionError:
            print("❌ Cannot connect to the application. Make sure it's running on port 8080")
            return False
            
    def test_cors_configuration(self):
        """Test CORS configuration"""
        print("\n=== Testing CORS Configuration ===")
        try:
            response = requests.options(self.api_url, headers={
                'Origin': 'http://malicious-site.com',
                'Access-Control-Request-Method': 'POST'
            })
            
            if 'Access-Control-Allow-Origin' in response.headers:
                allowed_origin = response.headers.get('Access-Control-Allow-Origin')
                print(f"✅ CORS is configured. Allowed origin: {allowed_origin}")
            else:
                print("⚠️  CORS headers not found in response")
        except Exception as e:
            print(f"❌ Error testing CORS: {e}")
            
    def test_api_endpoints(self):
        """Test API endpoints for basic functionality"""
        print("\n=== Testing API Endpoints ===")
        
        # Test GET all teachers
        try:
            response = requests.get(self.api_url)
            if response.status_code == 200:
                teachers = response.json()
                print(f"✅ GET /api/teachers successful. Found {len(teachers)} teachers")
            else:
                print(f"❌ GET /api/teachers failed with status {response.status_code}")
        except Exception as e:
            print(f"❌ Error testing GET /api/teachers: {e}")
            
        # Test GET specific teacher
        try:
            response = requests.get(f"{self.api_url}/1")
            if response.status_code == 200:
                teacher = response.json()
                print(f"✅ GET /api/teachers/1 successful")
            elif response.status_code == 404:
                print("⚠️  Teacher with ID 1 not found")
            else:
                print(f"❌ GET /api/teachers/1 failed with status {response.status_code}")
        except Exception as e:
            print(f"❌ Error testing GET /api/teachers/1: {e}")
            
    def test_input_validation(self):
        """Test input validation by sending malformed data"""
        print("\n=== Testing Input Validation ===")
        
        # Test with missing required fields
        malformed_teacher = {
            "firstName": "",  # Required field
            "lastName": "Doe",
            "email": "invalid-email",  # Invalid format
            "subject": "Math",
            "yearsOfExperience": -5  # Negative value
        }
        
        try:
            response = requests.post(self.api_url, json=malformed_teacher)
            if response.status_code == 400:
                print("✅ Server properly validates input and returns 400 for bad request")
            elif response.status_code == 200:
                print("⚠️  Server accepted malformed data (potential validation issue)")
            else:
                print(f"ℹ️  POST returned status {response.status_code}")
        except Exception as e:
            print(f"❌ Error testing input validation: {e}")
            
    def test_security_headers(self):
        """Check for important security headers"""
        print("\n=== Testing Security Headers ===")
        
        try:
            response = requests.get(self.base_url)
            headers = response.headers
            
            security_headers = {
                'X-Content-Type-Options': 'nosniff',
                'X-Frame-Options': 'DENY',
                'X-XSS-Protection': '1; mode=block',
                'Strict-Transport-Security': 'max-age=31536000'
            }
            
            missing_headers = []
            for header, expected_value in security_headers.items():
                if header in headers:
                    print(f"✅ {header}: {headers[header]}")
                else:
                    missing_headers.append(header)
                    
            if missing_headers:
                print(f"⚠️  Missing security headers: {', '.join(missing_headers)}")
                print("   These headers help protect against common web vulnerabilities")
        except Exception as e:
            print(f"❌ Error checking security headers: {e}")
            
    def test_sql_injection(self):
        """Test for basic SQL injection vulnerabilities"""
        print("\n=== Testing for SQL Injection (Basic) ===")
        
        # Test with SQL injection payload in URL parameters
        try:
            response = requests.get(f"{self.api_url}/1' OR '1'='1")
            if response.status_code == 404:
                print("✅ Application properly handles special characters in URL parameters")
            elif response.status_code == 500:
                print("❌ Application may be vulnerable to SQL injection (500 error)")
            else:
                print(f"ℹ️  SQL injection test returned status {response.status_code}")
        except Exception as e:
            print(f"❌ Error testing SQL injection: {e}")
            
    def test_xss_vulnerabilities(self):
        """Test for basic XSS vulnerabilities"""
        print("\n=== Testing for XSS Vulnerabilities (Basic) ===")
        
        # Test with XSS payload
        xss_payload = "<script>alert('XSS')</script>"
        
        # Test in query parameters
        try:
            response = requests.get(f"{self.base_url}/?search={xss_payload}")
            if xss_payload in response.text:
                print("❌ Potential XSS vulnerability found in search parameter")
            else:
                print("✅ Application properly escapes HTML in search parameter")
        except Exception as e:
            print(f"❌ Error testing XSS in search parameter: {e}")
            
    def run_all_tests(self):
        """Run all security tests"""
        print("Starting Security Tests for Spring Boot + Angular Application")
        print("=" * 60)
        
        # Check if application is running
        if not self.check_application_status():
            print("Cannot proceed with tests. Please start your Spring Boot application.")
            return
            
        # Run all tests
        self.test_cors_configuration()
        self.test_api_endpoints()
        self.test_input_validation()
        self.test_security_headers()
        self.test_sql_injection()
        self.test_xss_vulnerabilities()
        
        print("\n" + "=" * 60)
        print("Security Testing Complete")
        print("Note: This is a basic security test. For comprehensive security testing,")
        print("use tools like OWASP ZAP or Burp Suite.")

if __name__ == "__main__":
    tester = SpringBootSecurityTester()
    tester.run_all_tests()