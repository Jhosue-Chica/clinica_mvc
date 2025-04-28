# Sistema de Gestión de Clínica (MVC)

## Descripción
Sistema web para la gestión de una clínica desarrollado con el patrón de arquitectura MVC (Modelo-Vista-Controlador). Esta aplicación permite la administración eficiente de los procesos principales de una clínica médica, facilitando la gestión de pacientes, citas y personal médico.

## Funcionalidades principales
- Gestión de pacientes
  - Registro de pacientes nuevos
  - Actualización de información personal
  - Historial de visitas
  - Gestión de documentos médicos

- Gestión de citas médicas 
  - Programación de citas
  - Cancelación y reprogramación
  - Recordatorios automáticos
  - Vista de calendario médico

- Gestión de historias clínicas
  - Registro de consultas
  - Historial médico completo
  - Gestión de diagnósticos
  - Seguimiento de tratamientos

- Gestión de personal médico
  - Registro de médicos y especialidades
  - Control de horarios
  - Asignación de consultorios
  - Gestión de disponibilidad

- Gestión de usuarios y roles
  - Administración de perfiles
  - Control de accesos
  - Registro de actividades
  - Configuración de permisos

- Reportes y estadísticas
  - Informes de atención
  - Estadísticas de pacientes
  - Reportes financieros
  - Indicadores de gestión

## Tecnologías utilizadas
- Backend:
  - PHP 8.1
  - Laravel 10.x
  - MySQL 8.0
  
- Frontend:
  - HTML5
  - CSS3
  - JavaScript
  - Bootstrap 5
  - jQuery

- Herramientas adicionales:
  - Composer
  - npm
  - Git
  - PHPUnit para testing

## Requisitos previos
1. PHP >= 8.1
2. Composer
3. Node.js y npm
4. MySQL >= 8.0
5. Servidor web (Apache/Nginx)
6. Git

## Instalación
1. Clonar el repositorio
```bash
git clone https://github.com/Jhosue-Chica/clinica_mvc.git
cd clinica_mvc
```

2. Instalar dependencias de PHP
```bash
composer install
```

3. Instalar dependencias de JavaScript
```bash
npm install
```

4. Configurar el entorno
```bash
cp .env.example .env
php artisan key:generate
```

5. Configurar la base de datos
```bash
php artisan migrate
php artisan db:seed
```

6. Compilar assets
```bash
npm run dev
```

7. Iniciar el servidor
```bash
php artisan serve
```

## Configuración
1. Configuración del entorno (.env):
   - DB_DATABASE=clinica_db
   - DB_USERNAME=root
   - DB_PASSWORD=your_password
   - MAIL_MAILER=smtp
   - MAIL_HOST=your_mail_host
   - MAIL_PORT=your_mail_port

2. Configuración de permisos:
```bash
chmod -R 777 storage
chmod -R 777 bootstrap/cache
```

## Estructura del proyecto
```
clinica_mvc/
├── app/
│   ├── Http/
│   │   ├── Controllers/
│   │   └── Middleware/
│   ├── Models/
│   └── Services/
├── config/
├── database/
│   ├── migrations/
│   └── seeders/
├── public/
├── resources/
│   ├── views/
│   ├── js/
│   └── css/
├── routes/
├── storage/
├── tests/
└── vendor/
```

## Uso
1. Acceder al sistema: http://localhost:8000
2. Credenciales por defecto:
   - Admin: admin@clinica.com / password
   - Doctor: doctor@clinica.com / password
   - Paciente: paciente@clinica.com / password

## Contribución
1. Fork el proyecto
2. Cree una rama para su feature (`git checkout -b feature/NuevaFuncionalidad`)
3. Commit sus cambios (`git commit -m 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/NuevaFuncionalidad`)
5. Abra un Pull Request

## Testing
```bash
php artisan test
```

## Licencia
Este proyecto está bajo la licencia MIT - ver el archivo [LICENSE.md](LICENSE.md) para más detalles

## Autores
- Jhosue Israel Chica Peñarrieta - Desarrollo y documentación

## Contacto y Soporte
- Email: jhosue.chica@example.com
- GitHub: [@Jhosue-Chica](https://github.com/Jhosue-Chica)
- LinkedIn: [Jhosue Chica](https://linkedin.com/in/jhosue-chica)

## Agradecimientos
- A todos los contribuidores que han participado en este proyecto
- A la comunidad de desarrolladores de Laravel
- A los usuarios que han proporcionado feedback valioso

## Changelog
- v1.0.0 (2024-04-28)
  - Lanzamiento inicial
  - Implementación de funcionalidades básicas
  - Sistema de autenticación y autorización
