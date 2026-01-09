# 🛡️ SQL Injection Demo: Vulnerabilidad y Defensa

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Flask](https://img.shields.io/badge/Framework-Flask-green?style=flat&logo=flask)
![Security](https://img.shields.io/badge/Security-Educational-red)

Este proyecto es una aplicación web educativa diseñada para demostrar en tiempo real cómo ocurre una vulnerabilidad de **SQL Injection (SQLi)** y cuál es la forma correcta de mitigarla utilizando prácticas de programación segura.

---

## Objetivo del Proyecto

El sistema busca evidenciar visual y técnicamente la diferencia entre:

1. **Código Vulnerable:** Cómo la concatenación directa de cadenas (`f-strings`) permite a un atacante manipular la lógica de la base de datos.
2. **Código Seguro:** Cómo el uso de **Consultas Parametrizadas** (Prepared Statements) neutraliza los intentos de ataque al separar los datos del código.

## Arquitectura del Sistema

* **Backend:** Python (Flask).
* **Base de Datos:** SQLite (se genera automáticamente al iniciar).
* **Frontend:** HTML5 + Bootstrap (renderizado desde el servidor).
* **Concepto Clave:** Autenticación de usuarios (Login Bypass).

---

## Instalación y Ejecución

Sigue estos pasos para levantar el laboratorio en tu máquina local:

### 1. Requisitos Previos
Tener instalado **Python 3** en tu sistema.

### 2. Instalación de Dependencias
Abre tu terminal y ejecuta:

```bash
pip install flask
```

### 3. Ejecutar la Aplicación
Corre el script principal:

```bash
python app.py
```
Verás un mensaje indicando que el servidor está corriendo en: http://127.0.0.1:5000

## Guía de Pruebas (Hacking Ético)
El sistema presenta dos módulos de Login para comparar comportamientos.

### Escenario 1: El Login Vulnerable (Rojo)

Este módulo concatena directamente tu input. Intenta realizar un Authentication Bypass.

Ingresa al formulario rojo.

Usuario: Copia y pega el siguiente payload:
```bash
admin' --
```
Contraseña: Escribe cualquier cosa (ej. 123).

Resultado: Accederás como Administrador sin saber la clave real.

¿Por qué funciona? El payload transforma la consulta SQL interna en: SELECT * FROM users WHERE username='admin' --' AND password='...' (El -- comenta el resto de la línea, anulando la verificación de contraseña).

### Escenario 2: El Login Seguro (Verde)
Este módulo utiliza cursor.execute(query, params).

Intenta usar el mismo payload (admin' --) en el formulario verde.

Resultado: "Credenciales incorrectas".

¿Por qué es seguro? La base de datos trata el input estrictamente como texto literal. Busca un usuario que se llame literalmente "admin' --", el cual no existe.

## Disclaimer Ético
Este software ha sido desarrollado exclusivamente con fines académicos y educativos. El uso de las técnicas aquí demostradas contra sistemas reales sin autorización es ilegal y sancionado por la ley.

"La seguridad no es una característica, es un estado mental."

Desarrollado por: drahcirok



