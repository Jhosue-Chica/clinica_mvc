from config.database import DatabaseConnection

class Paciente:
    """Modelo para la tabla Paciente"""
    
    def __init__(self, id=None, nombre=None, apellido=None, cedula=None, fecha_nacimiento=None, email=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.fecha_nacimiento = fecha_nacimiento
        self.email = email
    
    @staticmethod
    def crear(paciente):
        """Crea un nuevo paciente en la base de datos"""
        db = DatabaseConnection()
        try:
            cursor = db.get_cursor()
            # Primero insertamos el paciente
            query = """
                INSERT INTO Paciente (Nombre, Apellido, Cedula, FechaNacimiento, Email)
                VALUES (?, ?, ?, CONVERT(DATE, ?, 105), ?)
            """
            cursor.execute(
                query, 
                (paciente.nombre, paciente.apellido, paciente.cedula, 
                 paciente.fecha_nacimiento.strftime('%d-%m-%Y'), paciente.email)
            )
            
            # Luego obtenemos el ID generado usando @@IDENTITY
            cursor.execute("SELECT @@IDENTITY AS Id")
            row = cursor.fetchone()
            if row and row.Id:
                paciente.id = int(row.Id)
            else:
                raise Exception("No se pudo obtener el ID del paciente creado")
                
            db.commit()
            return paciente
        except Exception as e:
            db.rollback()
            print(f"Error al crear paciente: {e}")
            raise e
    
    @staticmethod
    def obtener_todos():
        """Obtiene todos los pacientes de la base de datos"""
        db = DatabaseConnection()
        try:
            cursor = db.get_cursor()
            query = "SELECT Id, Nombre, Apellido, Cedula, FechaNacimiento, Email FROM Paciente ORDER BY Apellido, Nombre"
            cursor.execute(query)
            pacientes = []
            for row in cursor.fetchall():
                # Convertir la fecha a objeto date si es necesario
                fecha_nacimiento = row.FechaNacimiento
                if fecha_nacimiento is not None:
                    if isinstance(fecha_nacimiento, str):
                        from datetime import datetime
                        try:
                            fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d').date()
                        except ValueError:
                            try:
                                fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%d-%m-%Y').date()
                            except ValueError:
                                print(f"Formato de fecha no reconocido: {fecha_nacimiento}")
                                fecha_nacimiento = None
                
                paciente = Paciente(
                    id=row.Id,
                    nombre=row.Nombre,
                    apellido=row.Apellido,
                    cedula=row.Cedula,
                    fecha_nacimiento=fecha_nacimiento,
                    email=row.Email
                )
                pacientes.append(paciente)
            return pacientes
        except Exception as e:
            print(f"Error al obtener pacientes: {e}")
            raise e
    
    @staticmethod
    def obtener_por_id(id):
        """Obtiene un paciente por su ID"""
        db = DatabaseConnection()
        try:
            cursor = db.get_cursor()
            query = "SELECT Id, Nombre, Apellido, Cedula, FechaNacimiento, Email FROM Paciente WHERE Id = ?"
            cursor.execute(query, (id,))
            row = cursor.fetchone()
            if row:
                return Paciente(
                    id=row.Id,
                    nombre=row.Nombre,
                    apellido=row.Apellido,
                    cedula=row.Cedula,
                    fecha_nacimiento=row.FechaNacimiento,
                    email=row.Email
                )
            return None
        except Exception as e:
            print(f"Error al obtener paciente por ID: {e}")
            raise e
    
    @staticmethod
    def obtener_por_cedula(cedula):
        """Obtiene un paciente por su número de cédula"""
        db = DatabaseConnection()
        try:
            cursor = db.get_cursor()
            query = "SELECT Id, Nombre, Apellido, Cedula, FechaNacimiento, Email FROM Paciente WHERE Cedula = ?"
            cursor.execute(query, (cedula,))
            row = cursor.fetchone()
            if row:
                return Paciente(
                    id=row.Id,
                    nombre=row.Nombre,
                    apellido=row.Apellido,
                    cedula=row.Cedula,
                    fecha_nacimiento=row.FechaNacimiento,
                    email=row.Email
                )
            return None
        except Exception as e:
            print(f"Error al obtener paciente por cédula: {e}")
            raise e
    
    @staticmethod
    def actualizar(paciente):
        """Actualiza los datos de un paciente existente"""
        db = DatabaseConnection()
        try:
            cursor = db.get_cursor()
            query = """
                UPDATE Paciente 
                SET Nombre = ?, Apellido = ?, Cedula = ?, 
                    FechaNacimiento = CONVERT(DATE, ?, 105), Email = ?
                WHERE Id = ?
            """
            cursor.execute(
                query, 
                (paciente.nombre, paciente.apellido, paciente.cedula, 
                 paciente.fecha_nacimiento.strftime('%d-%m-%Y'), paciente.email, paciente.id)
            )
            db.commit()
            return True
        except Exception as e:
            db.rollback()
            print(f"Error al actualizar paciente: {e}")
            raise e
    
    @staticmethod
    def eliminar(id):
        """Elimina un paciente por su ID"""
        db = DatabaseConnection()
        try:
            cursor = db.get_cursor()
            # Primero verificamos si el paciente tiene citas
            check_query = "SELECT COUNT(*) AS CitasCount FROM Cita WHERE IdPaciente = ?"
            cursor.execute(check_query, (id,))
            result = cursor.fetchone()
            if result.CitasCount > 0:
                return False, "No se puede eliminar el paciente porque tiene citas registradas."
            
            # Si no tiene citas, procedemos a eliminar
            query = "DELETE FROM Paciente WHERE Id = ?"
            cursor.execute(query, (id,))
            db.commit()
            return True, "Paciente eliminado correctamente."
        except Exception as e:
            db.rollback()
            print(f"Error al eliminar paciente: {e}")
            return False, f"Error al eliminar paciente: {str(e)}"
    
    def __str__(self):
        """Representación de cadena del objeto paciente"""
        return f"{self.nombre} {self.apellido} (Cédula: {self.cedula})"