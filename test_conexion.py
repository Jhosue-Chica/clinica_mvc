#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test de conexión a la base de datos SQL Server
Este script permite verificar si la conexión a la base de datos funciona correctamente.
"""

import os
import sys
import time
import pyodbc
from dotenv import load_dotenv

def test_conexion():
    """Prueba la conexión a la base de datos SQL Server"""
    
    print("\n===== TEST DE CONEXIÓN A SQL SERVER =====\n")
    
    # Cargar variables de entorno desde archivo .env
    load_dotenv()
    
    # Obtener credenciales
    server = os.getenv('DB_SERVER', 'localhost')
    database = os.getenv('DB_NAME', 'ClinicaDB')
    username = os.getenv('DB_USER', 'sa')
    password = os.getenv('DB_PASSWORD', '')
    driver = os.getenv('DB_DRIVER', 'ODBC Driver 17 for SQL Server')
    
    # Mostrar configuración (sin contraseña)
    print(f"Configuración:")
    print(f"- Servidor: {server}")
    print(f"- Base de datos: {database}")
    print(f"- Usuario: {username}")
    print(f"- Driver ODBC: {driver}")
    print("\nIntentando conexión...\n")
    
    try:
        # Construir cadena de conexión
        connection_string = (
            f"DRIVER={{{driver}}};"
            f"SERVER={server};"
            f"DATABASE={database};"
            f"UID={username};"
            f"PWD={password};"
        )
        
        # Intentar conexión
        start_time = time.time()
        conn = pyodbc.connect(connection_string, timeout=10)
        elapsed_time = time.time() - start_time
        
        print(f"¡Conexión exitosa! (tiempo: {elapsed_time:.2f} segundos)")
        
        # Verificar versión de SQL Server
        cursor = conn.cursor()
        cursor.execute("SELECT @@version")
        version = cursor.fetchone()[0]
        print(f"\nVersión de SQL Server:")
        print(version.split('\n')[0])
        
        # Verificar tablas de la clínica
        print("\nVerificando tablas de la base de datos:")
        tablenames = ['Paciente', 'Medico', 'Cita']
        for table in tablenames:
            try:
                cursor.execute(f"SELECT COUNT(*) FROM {table}")
                count = cursor.fetchone()[0]
                print(f"- Tabla {table}: {count} registros")
            except Exception as e:
                print(f"- Tabla {table}: ERROR - {str(e)}")
        
        # Cerrar conexión
        conn.close()
        print("\nConexión cerrada correctamente.")
        
        # Mostrar drivers ODBC disponibles
        print("\nDrivers ODBC disponibles en este sistema:")
        for driver in pyodbc.drivers():
            print(f"- {driver}")
        
        return True
        
    except pyodbc.Error as e:
        print(f"Error de conexión: {e}")
        
        # Sugerencias según el error
        if "IM002" in str(e):
            print("\nSugerencia: El driver ODBC especificado no está instalado.")
            print("Drivers ODBC disponibles en este sistema:")
            for driver in pyodbc.drivers():
                print(f"- {driver}")
            print("\nEdita el archivo .env para utilizar uno de estos drivers.")
            
        elif "28000" in str(e):
            print("\nSugerencia: Credenciales incorrectas (usuario o contraseña).")
            
        elif "08001" in str(e) or "HYT00" in str(e):
            print("\nSugerencia: No se puede conectar al servidor SQL Server.")
            print("- Verifica que el servidor esté en ejecución")
            print("- Comprueba el nombre del servidor")
            print("- Asegúrate de que el firewall no esté bloqueando la conexión")
            
        elif "42000" in str(e):
            print("\nSugerencia: Base de datos inaccesible o inexistente.")
            
        return False
        
    except Exception as e:
        print(f"Error desconocido: {e}")
        return False

def crear_env_si_no_existe():
    """Crear un archivo .env si no existe"""
    if not os.path.exists('.env'):
        print("\nNo se encontró un archivo .env. Creando uno con valores predeterminados...")
        with open('.env', 'w') as f:
            f.write("# Configuración de conexión a SQL Server\n")
            f.write("DB_SERVER=localhost\n")
            f.write("DB_NAME=ClinicaDB\n")
            f.write("DB_USER=sa\n")
            f.write("DB_PASSWORD=tu_contraseña\n")
            f.write("DB_DRIVER=ODBC Driver 17 for SQL Server\n")
        print("Archivo .env creado. Por favor edita los valores antes de ejecutar nuevamente.")
        return True
    return False

if __name__ == "__main__":
    try:
        # Verificar si .env existe, si no, crearlo
        if crear_env_si_no_existe():
            sys.exit(0)
            
        # Ejecutar test de conexión
        test_conexion()
        
    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario.")
    except Exception as e:
        print(f"\nError inesperado: {e}")
    
    print("\n===== FIN DEL TEST =====")