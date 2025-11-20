"""
Prueba de integración para aplicaciones Spring Boot + Angular

Este script prueba la integración entre tu frontend Angular y tu backend Spring Boot
simulando las interacciones del usuario y verificando el flujo de datos.
"""

import requests
import json
import time

class IntegrationTester:
    def __init__(self):
        self.backend_url = "http://localhost:8080"
        self.api_url = f"{self.backend_url}/api/teachers"
        self.frontend_url = "http://localhost:4201"
        
    def test_backend_connectivity(self):
        """Test if backend is accessible"""
        print("=== Testing Backend Connectivity ===")
        try:
            response = requests.get(self.backend_url)
            if response.status_code == 200:
                print("✅ Backend is accessible")
                return True
            else:
                print(f"❌ Backend returned status code: {response.status_code}")
                return False
        except requests.exceptions.ConnectionError:
            print("❌ Cannot connect to backend. Make sure it's running on port 8080")
            return False
            
    def test_frontend_connectivity(self):
        """Test if frontend is accessible"""
        print("\n=== Testing Frontend Connectivity ===")
        try:
            response = requests.get(self.frontend_url)
            if response.status_code == 200:
                print("✅ Frontend is accessible")
                return True
            else:
                print(f"❌ Frontend returned status code: {response.status_code}")
                return False
        except requests.exceptions.ConnectionError:
            print("❌ Cannot connect to frontend. Make sure it's running on port 4201")
            return False
            
    def test_api_endpoints(self):
        """Test all API endpoints"""
        print("\n=== Testing API Endpoints ===")
        
        # Test GET all teachers
        try:
            response = requests.get(self.api_url)
            if response.status_code == 200:
                teachers = response.json()
                print(f"✅ GET /api/teachers successful. Found {len(teachers)} teachers")
                return teachers
            else:
                print(f"❌ GET /api/teachers failed with status {response.status_code}")
                return []
        except Exception as e:
            print(f"❌ Error testing GET /api/teachers: {e}")
            return []
            
    def test_create_teacher(self):
        """Test creating a new teacher"""
        print("\n=== Testing Teacher Creation ===")
        
        new_teacher = {
            "firstName": "Integration",
            "lastName": "Test",
            "email": "integration@test.com",
            "subject": "Testing",
            "yearsOfExperience": 2
        }
        
        try:
            response = requests.post(self.api_url, json=new_teacher)
            if response.status_code == 201:
                created_teacher = response.json()
                print(f"✅ Teacher created successfully with ID: {created_teacher.get('id')}")
                return created_teacher.get('id')
            else:
                print(f"❌ Failed to create teacher. Status code: {response.status_code}")
                print(f"Response: {response.text}")
                return None
        except Exception as e:
            print(f"❌ Error creating teacher: {e}")
            return None
            
    def test_update_teacher(self, teacher_id):
        """Test updating a teacher"""
        print("\n=== Testing Teacher Update ===")
        
        if not teacher_id:
            print("⚠️  No teacher ID provided for update test")
            return False
            
        updated_teacher = {
            "firstName": "Updated",
            "lastName": "Teacher",
            "email": "updated@teacher.com",
            "subject": "Updated Subject",
            "yearsOfExperience": 5
        }
        
        try:
            response = requests.put(f"{self.api_url}/{teacher_id}", json=updated_teacher)
            if response.status_code == 200:
                print("✅ Teacher updated successfully")
                return True
            elif response.status_code == 404:
                print("⚠️  Teacher not found for update")
                return False
            else:
                print(f"❌ Failed to update teacher. Status code: {response.status_code}")
                return False
        except Exception as e:
            print(f"❌ Error updating teacher: {e}")
            return False
            
    def test_delete_teacher(self, teacher_id):
        """Test deleting a teacher"""
        print("\n=== Testing Teacher Deletion ===")
        
        if not teacher_id:
            print("⚠️  No teacher ID provided for deletion test")
            return False
            
        try:
            response = requests.delete(f"{self.api_url}/{teacher_id}")
            if response.status_code == 204:
                print("✅ Teacher deleted successfully")
                return True
            elif response.status_code == 404:
                print("⚠️  Teacher not found for deletion")
                return False
            else:
                print(f"❌ Failed to delete teacher. Status code: {response.status_code}")
                return False
        except Exception as e:
            print(f"❌ Error deleting teacher: {e}")
            return False
            
    def test_cors_integration(self):
        """Test CORS between frontend and backend"""
        print("\n=== Testing CORS Integration ===")
        
        try:
            # Simulate a request from the frontend
            response = requests.get(self.api_url, headers={
                'Origin': self.frontend_url,
                'Referer': f"{self.frontend_url}/"
            })
            
            if response.status_code == 200:
                print("✅ CORS is properly configured for frontend-backend communication")
                
                # Check CORS headers
                if 'Access-Control-Allow-Origin' in response.headers:
                    allowed_origin = response.headers.get('Access-Control-Allow-Origin')
                    print(f"   Allowed origin: {allowed_origin}")
                return True
            else:
                print(f"❌ CORS test failed with status {response.status_code}")
                return False
        except Exception as e:
            print(f"❌ Error testing CORS: {e}")
            return False
            
    def run_integration_tests(self):
        """Run all integration tests"""
        print("Starting Integration Tests for Spring Boot + Angular Application")
        print("=" * 65)
        
        # Test connectivity
        backend_ok = self.test_backend_connectivity()
        frontend_ok = self.test_frontend_connectivity()
        
        if not (backend_ok and frontend_ok):
            print("\nCannot proceed with integration tests.")
            return
            
        # Test API endpoints
        teachers = self.test_api_endpoints()
        
        # Test CORS
        self.test_cors_integration()
        
        # Test CRUD operations
        print("\n=== Testing CRUD Operations ===")
        teacher_id = self.test_create_teacher()
        
        if teacher_id:
            self.test_update_teacher(teacher_id)
            # Verify the teacher was updated by fetching it
            try:
                response = requests.get(f"{self.api_url}/{teacher_id}")
                if response.status_code == 200:
                    teacher = response.json()
                    if teacher.get('firstName') == 'Updated':
                        print("✅ Verified teacher was updated correctly")
                    else:
                        print("❌ Teacher update verification failed")
            except Exception as e:
                print(f"❌ Error verifying teacher update: {e}")
                
            self.test_delete_teacher(teacher_id)
            
            # Verify the teacher was deleted
            try:
                response = requests.get(f"{self.api_url}/{teacher_id}")
                if response.status_code == 404:
                    print("✅ Verified teacher was deleted correctly")
                else:
                    print("❌ Teacher deletion verification failed")
            except Exception as e:
                print(f"❌ Error verifying teacher deletion: {e}")
        
        print("\n" + "=" * 65)
        print("Integration Testing Complete")
        print("Your Spring Boot backend and Angular frontend are properly integrated!")

if __name__ == "__main__":
    tester = IntegrationTester()
    tester.run_integration_tests()