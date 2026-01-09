import sqlite3
import os

DATABASE = 'sqli_demo.db'

def init_db():
    """Inicializa la base de datos y crea un usuario de prueba"""
    if os.path.exists(DATABASE):
        os.remove(DATABASE)
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Crear tabla de usuarios
    cursor.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT DEFAULT 'user'
        )
    ''')
    
    # Insertar usuario administrador
    cursor.execute(
        "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
        ('admin', 'admin123', 'administrator')
    )
    
    # Insertar algunos usuarios adicionales
    cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", ('usuario1', 'password1', 'user'))
    cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", ('usuario2', 'password2', 'user'))
    
    conn.commit()
    conn.close()

def check_vulnerable(username, password):
    """Ejecuta la lógica vulnerable y retorna el resultado y la query usada"""
    
    # EL CÓDIGO VULNERABLE ORIGINAL
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    result = {'method': 'Vulnerable (Concatenación directa)', 'query': query}
    
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        
        cursor.execute(query) # Ejecución insegura
        user = cursor.fetchone()
        conn.close()
        
        if user:
            result['success'] = True
            result['user'] = f"{user[1]} (Rol: {user[3]})"
        else:
            result['success'] = False
            result['error'] = 'Credenciales incorrectas'
            
    except Exception as e:
        result['success'] = False
        result['error'] = str(e)
        
    return result

def check_secure(username, password):
    """Ejecuta la lógica segura y retorna el resultado"""
    
    # EL CÓDIGO SEGURO ORIGINAL
    query = "SELECT * FROM users WHERE username=? AND password=?"
    result = {'method': 'Seguro (Consulta parametrizada)', 'query': query}
    
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        
        cursor.execute(query, (username, password)) # Ejecución segura con tupla
        user = cursor.fetchone()
        conn.close()
        
        if user:
            result['success'] = True
            result['user'] = f"{user[1]} (Rol: {user[3]})"
        else:
            result['success'] = False
            result['error'] = 'Credenciales incorrectas'
            
    except Exception as e:
        result['success'] = False
        result['error'] = str(e)
        
    return result