# Proyecto Final Automation Testing - Leila Peña

Este proyecto es un framework de automatización de pruebas que utiliza Selenium WebDriver para pruebas de interfaz de usuario (UI) en el sitio web de demostración [Saucedemo](www.saucedemo.com) y la biblioteca Requests para pruebas de API en [JSONPlaceholder](https://jsonplaceholder.typicode.com/).

El objetivo principal es demostrar la implementación de buenas prácticas de testing, como el patrón Page Object Model (POM), la parametrización de datos y la generación de reportes detallados.

## 🚀 Tecnologías Utilizadas

*   **Lenguaje de Programación:** Python
*   **Framework de Testing:** Pytest
*   **Automatización UI:** Selenium WebDriver
*   **Gestión de Drivers:** `webdriver-manager`
*   **Pruebas de API:** Requests
*   **Reportes:** `pytest-html`
*   **Control de Versiones:** Git y GitHub

## 📁 Estructura del Proyecto

proyecto-final-automation-testing--Leila-Pena-/
├── page/ # Clases que representan las páginas web (POM)
├── test/ # Casos de pruebas de Interfaz de Usuario (Selenium)
├── test-api/ # Casos de pruebas de pruebas de API (Requests)
├── utils/ # Funciones de utilidad (lectura de datos, logging, etc.)
├── data/ # Archivos externos de datos de prueba (CSV, JSON)
├── logs/ # Logs de las pruebas de API
├── pytest.ini # Archivo de configuración de Pytest
├── report.html # Reportes de las pruebas UI
└── README.md # Documentación del proyecto

¿Cómo Instalar las Dependencias?

1.  Clona el repositorio en tu máquina local.
2.  Navega a la carpeta raíz del proyecto.
3.  Instala las dependencias con este comando`: pip install pytest
selenium requests pytest-html webdriver-manager faker


## 🏃 ¿Cómo Ejecutar las Pruebas?

Asegúrate de tener el entorno virtual activado y estar en la raíz del proyecto.

### Ejecutar todas las pruebas (UI y API)

```bash
pytest

Ejecutar solo las pruebas de UI
pytest test

Ejecutar solo las pruebas de API
pytest test-api

Ejecutar pruebas y generar reporte HTML
pytest --html=reportes/reporte_final.html
