# 🛡️ SQL Injection Demo: Vulnerabilidad y Defensa

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Flask](https://img.shields.io/badge/Framework-Flask-green?style=flat&logo=flask)
![Security](https://img.shields.io/badge/Security-Educational-red)

Este proyecto es una aplicación web educativa diseñada para demostrar en tiempo real cómo ocurre una vulnerabilidad de **SQL Injection (SQLi)** y cuál es la forma correcta de mitigarla utilizando prácticas de programación segura.

---

## 🎯 Objetivo del Proyecto

El sistema busca evidenciar visual y técnicamente la diferencia entre:

1.  ❌ **Código Vulnerable:** Cómo la concatenación directa de cadenas (`f-strings`) permite a un atacante manipular la lógica de la base de datos.
2.  ✅ **Código Seguro:** Cómo el uso de **Consultas Parametrizadas** (Prepared Statements) neutraliza los intentos de ataque al separar los datos del código.

## 🏗️ Arquitectura del Sistema

* **Backend:** Python (Flask).
* **Base de Datos:** SQLite (se genera automáticamente al iniciar).
* **Frontend:** HTML5 + Bootstrap (renderizado desde el servidor).
* **Concepto Clave:** Autenticación de usuarios (Login Bypass).

---

## 🚀 Instalación y Ejecución

Sigue estos pasos para levantar el laboratorio en tu máquina local:

### 1. Requisitos Previos
Tener instalado **Python 3** en tu sistema.

### 2. Instalación de Dependencias
Abre tu terminal y ejecuta:

```bash

pip install flask
