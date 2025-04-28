from config.database import DatabaseConnection

class Medico:
    """Modelo para la tabla Medico"""
    
    def __init__(self, id=None, nombre=None, especialidad=None, email=None):
        self.id = id
        self.nombre = nombre
        self.especialidad = especialidad
        self.email = email
    
    @staticmethod
    def crear(medico):
        """Crea un nuevo médico en la base de datos"""
        db = DatabaseConnection()
        try:
            cursor = db.get_cursor()
            query = """
                INSERT INTO Medico (Nombre, Especialidad, Email)
                VALUES (?, ?, ?);
                SELECT SCOPE_IDENTITY() AS Id;
            """
            cursor.execute(query, (medico.nombre, medico.especialidad, medico.email))
            row = cursor.fetchone()
            medico.id = row.Id
            db.commit()
            return medico
        except Exception as e:
            db.rollback()
            print(f"Error al crear médico: {e}")
            raise e
    
    @staticmethod
    def obtener_todos():
        """Obtiene todos los médicos de la base de datos"""
        db = DatabaseConnection()
        try:
            cursor = db.get_cursor()
            query = "SELECT Id, Nombre, Especialidad, Email FROM Medico ORDER BY Nombre"
            cursor.execute(query)
            medicos = []
            for row in cursor.fetchall():
                medico = Medico(
                    id=row.Id,
                    nombre=row.Nombre,
                    especialidad=row.Especialidad,
                    email=row.Email
                )
                medicos.append(medico)
            return medicos
        except Exception as e:
            print(f"Error al obtener médicos: {e}")
            raise e
    
    @staticmethod
    def obtener_por_id(id):
        """Obtiene un médico por su ID"""
        db = DatabaseConnection()
        try:
            cursor = db.get_cursor()
            query = "SELECT Id, Nombre, Especialidad, Email FROM Medico WHERE Id = ?"
            cursor.execute(query, (id,))
            row = cursor.fetchone()
            if row:
                return Medico(
                    id=row.Id,
                    nombre=row.Nombre,
                    especialidad=row.Especialidad,
                    email=row.Email
                )
            return None
        except Exception as e:
            print(f"Error al obtener médico por ID: {e}")
            raise e
    
    @staticmethod
    def obtener_por_especialidad(especialidad):
        """Obtiene médicos por especialidad"""
        db = DatabaseConnection()
        try:
            cursor = db.get_cursor()
            query = "SELECT Id, Nombre, Especialidad, Email FROM Medico WHERE Especialidad LIKE ?"
            cursor.execute(query, (f"%{especialidad}%",))
            medicos = []
            for row in cursor.fetchall():
                medico = Medico(
                    id=row.Id,
                    nombre=row.Nombre,
                    especialidad=row.Especialidad,
                    email=row.Email
                )
                medicos.append(medico)
            return medicos
        except Exception as e:
            print(f"Error al obtener médicos por especialidad: {e}")
            raise e
    
    @staticmethod
    def actualizar(medico):
        """Actualiza los datos de un médico existente"""
        db = DatabaseConnection()
        try:
            cursor = db.get_cursor()
            query = """
                UPDATE Medico 
                SET Nombre = ?, Especialidad = ?, Email = ?
                WHERE Id = ?
            """
            cursor.execute(query, (medico.nombre, medico.especialidad, medico.email, medico.id))
            db.commit()
            return True
        except Exception as e:
            db.rollback()
            print(f"Error al actualizar médico: {e}")
            raise e
    
    @staticmethod
    def eliminar(id):
        """Elimina un médico por su ID"""
        db = DatabaseConnection()
        try:
            cursor = db.get_cursor()
            # Primero verificamos si el médico tiene citas
            check_query = "SELECT COUNT(*) AS CitasCount FROM Cita WHERE IdMedico = ?"
            cursor.execute(check_query, (id,))
            result = cursor.fetchone()
            if result.CitasCount > 0:
                return False, "No se puede eliminar el médico porque tiene citas registradas."
            
            # Si no tiene citas, procedemos a eliminar
            query = "DELETE FROM Medico WHERE Id = ?"
            cursor.execute(query, (id,))
            db.commit()
            return True, "Médico eliminado correctamente."
        except Exception as e:
            db.rollback()
            print(f"Error al eliminar médico: {e}")
            return False, f"Error al eliminar médico: {str(e)}"
    
    def __str__(self):
        """Representación de cadena del objeto médico"""
        return f"Dr(a). {self.nombre} - {self.especialidad}"