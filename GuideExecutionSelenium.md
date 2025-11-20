# Cómo ejecutar una prueba funcional con Selenium

## Requisitos previos

1. Python 3.7 o superior instalado
2. Navegador Google Chrome instalado
3. Backend de Spring Boot ejecutándose en el puerto 8080
4. Frontend de Angular ejecutándose en el puerto 4201

## Instalación

1. Instalar los paquetes de Python necesarios:
```bash
pip install -r selenium-requirements.txt
```

## Inicio de las aplicaciones

Antes de ejecutar las pruebas, asegúrese de que ambas aplicaciones estén en funcionamiento:

### Iniciar el backend de Spring Boot
```bash
cd d:\Pruebas
./mvnw spring-boot:run
```

### Iniciar el frontend de Angular
```bash
cd d:\Pruebas\angular-frontend
ng serve --port 4201
```

## Ejecución de la prueba funcional con Selenium

Execute the test script:
```bash
python selenium-test.py
```

## Qué hace la prueba

La prueba de Selenium realiza las siguientes acciones:

1. **Abre la aplicación** - Navega a http://localhost:4201
2. **Verifica la lista de profesores** - Comprueba que se hayan cargado los datos iniciales de los profesores
3. **Crea un nuevo profesor** - Rellena el formulario con datos de prueba y lo envía
4. **Verifica el nuevo profesor** - Confirma que el nuevo profesor aparece en la lista
5. **Prueba la validación del formulario** - Intenta enviar un formulario vacío para verificar que la validación funciona

## Resultado esperado

Cuando la prueba se ejecute correctamente, debería ver un resultado similar a:

``` 
Iniciando pruebas funcionales de Selenium para la aplicación de gestión de profesores
======================================================================
=== Prueba 1: Apertura de la aplicación ===
✅ Aplicación abierta correctamente

=== Prueba 2: Verificación de la lista de profesores ===
✅ Lista de profesores cargada correctamente con 3 profesores

=== Prueba 3: Creación de un nuevo profesor ===
✅ Formulario del profesor enviado correctamente

=== Prueba 4: Verificación del nuevo profesor en la lista ===
✅ Nuevo profesor añadido a la lista. Total de profesores: 4

=== Prueba 5: Prueba de validación del formulario ===
✅ Validación del formulario funcionando. Se encontraron 5 errores de validación

=== Todas las pruebas completadas === WebDriver cerrado
```

## Solución de problemas

### Problemas comunes

1. **ChromeDriver no encontrado**: Asegúrese de que Chrome esté instalado y que chromedriver esté en su PATH.
2. **Elemento no encontrado**: Asegúrese de que ambas aplicaciones estén en ejecución y sean accesibles. Compruebe que:
    - Spring Boot se esté ejecutando en el puerto 8080
    - Angular se esté ejecutando en el puerto 4201
    - La aplicación se cargue correctamente en un navegador

### Ejecución en Modo No Headless

To see the browser actions during testing, comment out the headless option in [selenium-test.py](file:///d:/Pruebas/selenium-test.py):
```python
# chrome_options.add_argument("--headless")  # Comment this line
```

## Interpretación de los resultados de la prueba

- ✅ **Marca de verificación verde**: Prueba superada con éxito
- ⚠️ **Advertencia amarilla**: Prueba completada, pero con posibles problemas

- ❌ **X roja**: La prueba falló con un error

La prueba valida que tu frontend de Angular se comunica correctamente con tu backend de Spring Boot y que todas las funcionalidades funcionan como se espera.