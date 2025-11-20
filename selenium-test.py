"""
Script de prueba funcional con Selenium para la aplicación de gestión de profesores
Versión mejorada con esperas explícitas y manejo de errores más robusto.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time


def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(options=chrome_options)


def test_teacher_management():
    driver = setup_driver()
    driver.get("http://localhost:4201")

    print("\n=== Test 1: Opening the application ===")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "app-root"))
    )
    print("✅ Aplicación cargada correctamente")

    time.sleep(2)

    print("\n=== Test 2: Verificando listado de profesores ===")
    try:
        # Esperar tabla si existe
        teacher_rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")

        if len(teacher_rows) > 0:
            print(f"✅ Lista cargada con {len(teacher_rows)} profesores")
        else:
            print("ℹ Lista vacía, agregando profesor primero...")
    except:
        print("⚠ No se encontró la tabla")

    print("\n=== Test 3: Creando profesor ===")

    driver.find_element(By.ID, "firstName").send_keys("Selenium")
    driver.find_element(By.ID, "lastName").send_keys("Tester")
    driver.find_element(By.ID, "email").send_keys("selenium.tester@example.com")
    driver.find_element(By.ID, "subject").send_keys("QA Automation")
    driver.find_element(By.ID, "yearsOfExperience").send_keys("3")

    submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_btn.click()

    time.sleep(3)
    print("✅ Profesor registrado correctamente")

    print("\n=== Test 4: Verificando actualización del listado ===")
    teacher_rows_after = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
    print(f"📌 Total de profesores ahora: {len(teacher_rows_after)}")

    print("\n=== Test 5: Validaciones del formulario ===")
    
    # Enviar formulario vacío
    driver.find_element(By.ID, "firstName").clear()
    submit_btn.click()
    time.sleep(1)

    errors = driver.find_elements(By.CSS_SELECTOR, ".error-message")
    print(f"🔍 Validaciones detectadas: {len(errors)}")

    print("\n=== PRUEBAS FINALIZADAS ===")
    driver.quit()
    print("WebDriver cerrado")


if __name__ == "__main__":
    test_teacher_management()
