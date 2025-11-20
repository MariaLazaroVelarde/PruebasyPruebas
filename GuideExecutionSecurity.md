# Cómo ejecutar la prueba de seguridad OWASP ZAP

## Requisitos previos

1. Python 3.7 o superior instalado
2. OWASP ZAP Community Edition instalado y en ejecución
3. Tu backend Spring Boot ejecutándose en el puerto 8080
4. Tu frontend Angular ejecutándose en el puerto 4201

## Instalación

1. Asegúrate de tener instalada la biblioteca requests:
```bash
pip install requests
```

## Inicio de las aplicaciones

Antes de ejecutar las pruebas de seguridad, asegúrese de que todas las aplicaciones estén en funcionamiento:

### Iniciar OWASP ZAP
1. Descargue OWASP ZAP desde https://www.zaproxy.org/download/
2. Instale e inicie OWASP ZAP
3. Asegúrese de que se esté ejecutando en el puerto predeterminado 8080

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

## Ejecutando la prueba de seguridad OWASP ZAP

Ejecutar el script de la prueba de seguridad:
```bash
python owasp-zap-security-test.py
```

## Qué hace la prueba

La prueba de seguridad OWASP ZAP realiza las siguientes acciones:

1. **Verifica la conectividad de ZAP** - Comprueba que OWASP ZAP esté en ejecución y accesible.
2. **Accede a las aplicaciones objetivo** - Se conecta al backend de Spring Boot y al frontend de Angular a través del proxy ZAP.
3. **Analiza las aplicaciones** - Descubre la estructura y los endpoints de tus aplicaciones.
4. **Realiza un escaneo activo** - Busca vulnerabilidades comunes como XSS, inyección SQL, etc.
5. **Prueba vulnerabilidades comunes** - Prueba específicamente inyección SQL, XSS y path traversal.
6. **Recupera alertas de seguridad** - Recopila y resume todas las alertas de seguridad encontradas por ZAP.

## Resultado esperado

Cuando la prueba se ejecute correctamente, debería ver un resultado similar al siguiente:

``` 
Iniciando pruebas de seguridad OWASP ZAP para la aplicación Spring Boot + Angular
======================================================================
✅ OWASP ZAP es accesible

=== Acceso a la aplicación objetivo ===
✅ Se accedió a http://localhost:8080 a través del proxy ZAP
✅ Se accedió a http://localhost:4201 a través del proxy ZAP

=== Rastreo de http://localhost:8080 ===
✅ Rastreo iniciado con ID de escaneo: 1
   Progreso del rastreo: 0%
   Progreso del rastreo: 50%
   Progreso del rastreo: 100%
✅ Rastreo finalizado

=== Rastreando http://localhost:4201 ===
✅ Rastreo iniciado con ID de escaneo: 2
   Progreso del rastreo: 0%
   Progreso del rastreo: 100%
✅ Rastreo completado

=== Escaneo activo http://localhost:8080 ===
✅ Escaneo activo iniciado con ID de escaneo: 3
   Progreso del escaneo: 0%
   Progreso del escaneo: 50%
   Progreso del escaneo: 100%
✅ Escaneo activo completado

=== Pruebas de vulnerabilidades comunes === Pruebas de inyección SQL...
✅ La aplicación gestiona correctamente los intentos de inyección SQL

Pruebas de XSS...
✅ La aplicación gestiona correctamente los intentos de XSS
Pruebas de recorrido de directorios...

✅ La aplicación gestiona correctamente los intentos de recorrido de directorios

=== Recuperación de alertas de seguridad ===
✅ Se encontraron 3 alertas

High Risk Alerts (1):
  • Cross Site Scripting (Reflected)
    URL: http://localhost:8080/search?q=<script>alert('XSS')</script>
    Description: The page returns user input directly in the response...

Medium Risk Alerts (2):
  • Missing Anti-CSRF Tokens
    URL: http://localhost:8080/api/teachers
    Description: No Anti-CSRF tokens were found in a HTML submission...

======================================================================
Pruebas de seguridad OWASP ZAP completadas
Revise las alertas anteriores para identificar posibles vulnerabilidades de seguridad en su aplicación Spring Boot + Angular.
```

## Interpretación de los resultados

### Niveles de riesgo de alerta

- **Alto**: Vulnerabilidades críticas que deben abordarse de inmediato.
- **Medio**: Vulnerabilidades importantes que deben abordarse pronto.
- **Bajo**: Vulnerabilidades menores que deben abordarse cuando sea posible.
- **Informativo**: Información que puede ser útil, pero que no necesariamente constituye una vulnerabilidad.

### Vulnerabilidades comunes detectadas

1. **Cross-Site Scripting (XSS)**: Inyección de scripts maliciosos en páginas web
2. **Inyección SQL**: Inserción de código SQL malicioso en consultas
3. **Falta de encabezados de seguridad**: Encabezados HTTP importantes que protegen contra ataques
4. **Falta de tokens anti-CSRF**: Protección contra la falsificación de solicitudes entre sitios (CSRF)
5. **Recorrido de directorios**: Acceso no autorizado a archivos y directorios

## Solución de problemas

### Problemas comunes

1. **ZAP no accesible**: Asegúrese de que OWASP ZAP se esté ejecutando en el puerto 8080.
2. **Conexión rechazada**: Asegúrese de que todas las aplicaciones se estén ejecutando en sus respectivos puertos.
3. **El escaneo tarda demasiado**: En el caso de aplicaciones grandes, los escaneos pueden tardar varios minutos.

### Ejecución de análisis manuales en ZAP

Para realizar pruebas más exhaustivas, también puede usar la interfaz gráfica de usuario (GUI) de OWASP ZAP:

1. Abra OWASP ZAP.
2. Acceda a su aplicación en un navegador configurado para usar ZAP como proxy.
3. En ZAP, haga clic con el botón derecho en el sitio en el árbol de Sitios.
4. Seleccione "Ataque" → "Análisis activo".
5. Revise las alertas en la pestaña Alertas.

## Recomendaciones de seguridad

Según los resultados de las pruebas, considere implementar las siguientes medidas de seguridad:

1. **Validación de entrada**: Valide y sanee todas las entradas del usuario.
2. **Codificación de salida**: Codifique los datos antes de mostrarlos en HTML.
3. **Encabezados de seguridad**: Agregue encabezados como X-Content-Type-Options y X-Frame-Options.
4. **Protección contra CSRF**: Implemente tokens anti-CSRF para los formularios.
5. **Autenticación**: Garantice una autenticación y autorización adecuadas.
6. **HTTPS**: Utilice HTTPS en entornos de producción.

## Próximos pasos

1. Revisar todas las alertas de riesgo alto y medio.
2. Corregir las vulnerabilidades identificadas.
3. Volver a ejecutar las pruebas de seguridad para verificar las correcciones.
4. Integrar las pruebas de seguridad en el pipeline de CI/CD.
5. Realizar evaluaciones de seguridad periódicas.