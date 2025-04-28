# Sistema de Gestión de Clínica Médica

Sistema de gestión para clínicas médicas desarrollado en Python con Flask, implementando el patrón MVC (Modelo-Vista-Controlador).

## Características Principales

- Gestión completa de pacientes, médicos y citas
- Interfaz web moderna y responsiva
- Base de datos SQL Server para almacenamiento seguro de datos
- Autenticación y control de acceso
- Reportes y estadísticas

## Estructura del Proyecto

```
clinica_mvc/
├── config/                 # Configuración de la aplicación
│   └── database.py        # Conexión a la base de datos
├── controllers/           # Controladores (lógica de negocio)
│   ├── cita_controller.py
│   ├── paciente_controller.py
│   └── medico_controller.py
├── models/               # Modelos de datos
│   ├── cita.py
│   ├── paciente.py
│   └── medico.py
├── views/               # Vistas de consola
│   ├── cita_view.py
│   ├── paciente_view.py
│   └── medico_view.py
├── web_controllers/     # Controladores web
│   ├── cita_routes.py
│   ├── paciente_routes.py
│   └── medico_routes.py
├── templates/          # Plantillas HTML
│   ├── citas/
│   ├── pacientes/
│   └── medicos/
├── static/            # Archivos estáticos (CSS, JS, imágenes)
├── forms/             # Formularios WTForms
├── app.py            # Aplicación principal
└── requirements.txt  # Dependencias del proyecto
```

## Requisitos del Sistema

- Python 3.8 o superior
- SQL Server
- pip (gestor de paquetes de Python)

## Instalación

1. Clonar el repositorio:
```bash
git clone [url-del-repositorio]
cd clinica_mvc
```

2. Crear un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar la base de datos:
- Crear una base de datos en SQL Server
- Actualizar la configuración en `config/database.py`

5. Iniciar la aplicación:
```bash
python app.py
```

## Funcionalidades

### Gestión de Pacientes
- Registro de información personal
- Historial médico
- Búsqueda y filtrado de pacientes

### Gestión de Médicos
- Registro de especialistas
- Control de horarios
- Asignación de consultorios

### Gestión de Citas
- Programación de consultas
- Recordatorios automáticos
- Control de disponibilidad

## Tecnologías Utilizadas

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap
- **Base de Datos**: SQL Server
- **ORM**: pyodbc
- **Formularios**: WTForms
- **Plantillas**: Jinja2

## Contribución

1. Hacer fork del proyecto
2. Crear una rama para la nueva característica (`git checkout -b feature/nueva-caracteristica`)
3. Hacer commit de los cambios (`git commit -am 'Agregar nueva característica'`)
4. Hacer push a la rama (`git push origin feature/nueva-caracteristica`)
5. Crear un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

