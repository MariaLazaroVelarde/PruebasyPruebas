""" 
Script de prueba simple con Selenium para la aplicación de gestión de profesores

Este script realiza pruebas funcionales básicas de la aplicación de gestión de profesores.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def setup_driver():
    """Setup Chrome WebDriver with basic configuration"""
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in background
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-logging")
    chrome_options.add_argument("--silent")
    
    try:
        driver = webdriver.Chrome(options=chrome_options)
        return driver
    except Exception as e:
        print(f"Error setting up Chrome driver: {e}")
        return None

def simple_test():
    """Simple test to verify the application loads"""
    driver = setup_driver()
    if not driver:
        print("Failed to setup WebDriver")
        return
    
    try:
        print("=== Simple Test: Opening the application ===")
        driver.get("http://localhost:4201")
        time.sleep(5)  # Wait for page to load
        
        # Check if the page title is correct
        title = driver.title
        if "teacher" in title.lower() or "management" in title.lower():
            print("✅ Application page loaded successfully")
        else:
            print(f"ℹ️ Page loaded with title: {title}")
        
        # Check if Angular app root is present
        app_elements = driver.find_elements(By.TAG_NAME, "app-root")
        if len(app_elements) > 0:
            print("✅ Angular application is running")
        else:
            print("⚠️ Angular application root not found")
            
        print("✅ Simple test completed successfully")
        
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
    finally:
        driver.quit()
        print("WebDriver closed")

if __name__ == "__main__":
    print("Starting Simple Selenium Test for Teacher Management Application")
    print("=" * 60)
    simple_test()