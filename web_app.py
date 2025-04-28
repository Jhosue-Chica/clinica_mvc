from flask import Flask, render_template, redirect, url_for
import os
from dotenv import load_dotenv
from config.database import DatabaseConnection

# Importar controladores web
from web_controllers.paciente_routes import paciente_bp
from web_controllers.medico_routes import medico_bp
from web_controllers.cita_routes import cita_bp

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'clave_secreta_para_clinica_mvc')

# Inicializar conexión a la base de datos
try:
    db = DatabaseConnection()
    print("Conexión a la base de datos establecida para la aplicación web.")
except Exception as e:
    print(f"Error al conectar con la base de datos: {e}")
    print("Verifique su archivo .env con las credenciales de conexión")
    exit(1)

# Registrar blueprints
app.register_blueprint(paciente_bp, url_prefix='/pacientes')
app.register_blueprint(medico_bp, url_prefix='/medicos')
app.register_blueprint(cita_bp, url_prefix='/citas')

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    """Manejo de errores 404"""
    return render_template('404.html'), 404

@app.context_processor
def utility_processor():
    """Funciones de utilidad para las plantillas"""
    def format_date(date):
        """Formatea fecha para mostrar"""
        if date:
            return date.strftime('%d-%m-%Y')
        return ""
        
    def format_datetime(datetime):
        """Formatea fecha y hora para mostrar"""
        if datetime:
            return datetime.strftime('%d-%m-%Y %H:%M')
        return ""
    
    return dict(
        format_date=format_date,
        format_datetime=format_datetime
    )

# Manejo de errores de base de datos
@app.errorhandler(Exception)
def handle_exception(e):
    """Manejo general de excepciones"""
    print(f"Error: {e}")
    return render_template('error.html', error=str(e)), 500

if __name__ == '__main__':
    try:
        print("Iniciando aplicación web MVC para Clínica...")
        app.run(debug=True)
    except KeyboardInterrupt:
        print("\nServidor web detenido por el usuario.")
    except Exception as e:
        print(f"\nError inesperado: {e}")
    finally:
        if 'db' in locals():
            db.close()
            print("Conexión a la base de datos cerrada correctamente.")