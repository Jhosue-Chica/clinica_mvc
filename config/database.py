import os
import pyodbc
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

class DatabaseConnection:
    """Clase para gestionar la conexión a la base de datos SQL Server"""
    
    _instance = None
    
    def __new__(cls):
        """Implementación del patrón Singleton para la conexión a BD"""
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance._connect()
        return cls._instance
    
    def _connect(self):
        """Establece la conexión a la base de datos"""
        try:
            server = os.getenv('DB_SERVER', 'localhost')
            database = os.getenv('DB_NAME', 'ClinicaDB')
            username = os.getenv('DB_USER', 'sa')
            password = os.getenv('DB_PASSWORD', '')
            # Obtener el driver desde .env o usar el valor por defecto 'SQL Server'
            driver = os.getenv('DB_DRIVER', 'SQL Server')
            
            connection_string = (
                f"DRIVER={{{driver}}};"
                f"SERVER={server};"
                f"DATABASE={database};"
                f"UID={username};"
                f"PWD={password};"
            )
            
            self.connection = pyodbc.connect(connection_string)
            self.connection.autocommit = False
            print("Conexión a la base de datos establecida con éxito.")
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")
            raise e
    
    def get_connection(self):
        """Retorna la conexión activa"""
        return self.connection
    
    def get_cursor(self):
        """Retorna un cursor para ejecutar consultas"""
        return self.connection.cursor()
    
    def commit(self):
        """Confirma los cambios en la base de datos"""
        self.connection.commit()
        
    def rollback(self):
        """Revierte los cambios en caso de error"""
        self.connection.rollback()
    
    def close(self):
        """Cierra la conexión a la base de datos"""
        if hasattr(self, 'connection') and self.connection:
            self.connection.close()
            print("Conexión a la base de datos cerrada.")