#!/usr/bin/env python3
"""
Demostración educativa de SQL Injection para universidad
"""
from flask import Flask, request, render_template, redirect, url_for
import logic # Importamos nuestro archivo de lógica

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_sesiones'

# Inicializamos la DB al arrancar la app
with app.app_context():
    logic.init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login_vulnerable', methods=['POST'])
def login_vulnerable():
    username = request.form['username']
    password = request.form['password']
    
    # Llamamos a la función que está en logic.py
    result = logic.check_vulnerable(username, password)
    
    return render_template('index.html', result=result)

@app.route('/login_secure', methods=['POST'])
def login_secure():
    username = request.form['username']
    password = request.form['password']
    
    # Llamamos a la función que está en logic.py
    result = logic.check_secure(username, password)
    
    return render_template('index.html', result=result)

@app.route('/reset')
def reset_db():
    logic.init_db()
    return redirect(url_for('index'))

if __name__ == '__main__':
    print("Base de datos inicializada con usuario: admin / admin123")
    print("Accede a la aplicación en: http://127.0.0.1:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)