from config.database import DatabaseConnection
from models.paciente import Paciente
from models.medico import Medico

class Cita:
    """Modelo para la tabla Cita"""
    
    def __init__(self, id=None, id_paciente=None, id_medico=None, fecha_hora=None, motivo=None):
        self.id = id
        self.id_paciente = id_paciente
        self.id_medico = id_medico
        self.fecha_hora = fecha_hora
        self.motivo = motivo
        # Propiedades para almacenar datos relacionados
        self.paciente = None
        self.medico = None
    
    @staticmethod
    def crear(cita):
        """Crea una nueva cita en la base de datos"""
        db = DatabaseConnection()
        try:
            cursor = db.get_cursor()
            # Primero insertamos la cita
            query = """
                INSERT INTO Cita (IdPaciente, IdMedico, FechaHora, Motivo)
                VALUES (?, ?, ?, ?)
            """
            cursor.execute(
                query, 
                (cita.id_paciente, cita.id_medico, cita.fecha_hora, cita.motivo)
            )
            
            # Luego obtenemos el ID generado
            cursor.execute("SELECT SCOPE_IDENTITY() AS Id")
            row = cursor.fetchone()
            cita.id = row.Id
            
            db.commit()
            return cita
        except Exception as e:
            db.rollback()
            print(f"Error al crear cita: {e}")
            raise e
    
    @staticmethod
    def obtener_todas():
        """Obtiene todas las citas con datos de pacientes y médicos"""
        db = DatabaseConnection()
        try:
            cursor = db.get_cursor()
            query = """
                SELECT 
                    c.Id, c.IdPaciente, c.IdMedico, c.FechaHora, c.Motivo,
                    p.Nombre AS PacienteNombre, p.Apellido AS PacienteApellido,
                    m.Nombre AS MedicoNombre, m.Especialidad AS MedicoEspecialidad
                FROM Cita c
                INNER JOIN Paciente p ON c.IdPaciente = p.Id
                INNER JOIN Medico m ON c.IdMedico = m.Id
                ORDER BY c.FechaHora
            """
            cursor.execute(query)
            citas = []
            for row in cursor.fetchall():
                cita = Cita(
                    id=row.Id,
                    id_paciente=row.IdPaciente,
                    id_medico=row.IdMedico,
                    fecha_hora=row.FechaHora,
                    motivo=row.Motivo
                )
                # Crear objetos relacionados con datos parciales
                cita.paciente = Paciente(
                    id=row.IdPaciente,
                    nombre=row.PacienteNombre,
                    apellido=row.PacienteApellido
                )
                cita.medico = Medico(
                    id=row.IdMedico,
                    nombre=row.MedicoNombre,
                    especialidad=row.MedicoEspecialidad
                )
                citas.append(cita)
            return citas
        except Exception as e:
            print(f"Error al obtener citas: {e}")
            raise e
    
    @staticmethod
    def obtener_por_id(id):
        """Obtiene una cita por su ID con datos completos"""
        db = DatabaseConnection()
        try:
            cursor = db.get_cursor()
            query = """
                SELECT 
                    c.Id, c.IdPaciente, c.IdMedico, c.FechaHora, c.Motivo,
                    p.Nombre AS PacienteNombre, p.Apellido AS PacienteApellido,
                    m.Nombre AS MedicoNombre, m.Especialidad AS MedicoEspecialidad
                FROM Cita c
                INNER JOIN Paciente p ON c.IdPaciente = p.Id
                INNER JOIN Medico m ON c.IdMedico = m.Id
                WHERE c.Id = ?
            """
            cursor.execute(query, (id,))
            row = cursor.fetchone()
            if row:
                cita = Cita(
                    id=row.Id,
                    id_paciente=row.IdPaciente,
                    id_medico=row.IdMedico,
                    fecha_hora=row.FechaHora,
                    motivo=row.Motivo
                )
                # Crear objetos relacionados con datos parciales
                cita.paciente = Paciente(
                    id=row.IdPaciente,
                    nombre=row.PacienteNombre,
                    apellido=row.PacienteApellido
                )
                cita.medico = Medico(
                    id=row.IdMedico,
                    nombre=row.MedicoNombre,
                    especialidad=row.MedicoEspecialidad
                )
                return cita
            return None
        except Exception as e:
            print(f"Error al obtener cita por ID: {e}")
            raise e
    
    @staticmethod
    def obtener_por_paciente(id_paciente):
        """Obtiene todas las citas de un paciente específico"""
        db = DatabaseConnection()
        try:
            cursor = db.get_cursor()
            query = """
                SELECT 
                    c.Id, c.IdPaciente, c.IdMedico, c.FechaHora, c.Motivo,
                    p.Nombre AS PacienteNombre, p.Apellido AS PacienteApellido,
                    m.Nombre AS MedicoNombre, m.Especialidad AS MedicoEspecialidad
                FROM Cita c
                INNER JOIN Paciente p ON c.IdPaciente = p.Id
                INNER JOIN Medico m ON c.IdMedico = m.Id
                WHERE c.IdPaciente = ?
                ORDER BY c.FechaHora
            """
            cursor.execute(query, (id_paciente,))
            citas = []
            for row in cursor.fetchall():
                cita = Cita(
                    id=row.Id,
                    id_paciente=row.IdPaciente,
                    id_medico=row.IdMedico,
                    fecha_hora=row.FechaHora,
                    motivo=row.Motivo
                )
                # Crear objetos relacionados con datos parciales
                cita.paciente = Paciente(
                    id=row.IdPaciente,
                    nombre=row.PacienteNombre,
                    apellido=row.PacienteApellido
                )
                cita.medico = Medico(
                    id=row.IdMedico,
                    nombre=row.MedicoNombre,
                    especialidad=row.MedicoEspecialidad
                )
                citas.append(cita)
            return citas
        except Exception as e:
            print(f"Error al obtener citas por paciente: {e}")
            raise e
    
    @staticmethod
    def obtener_por_medico(id_medico):
        """Obtiene todas las citas de un médico específico"""
        db = DatabaseConnection()
        try:
            cursor = db.get_cursor()
            query = """
                SELECT 
                    c.Id, c.IdPaciente, c.IdMedico, c.FechaHora, c.Motivo,
                    p.Nombre AS PacienteNombre, p.Apellido AS PacienteApellido,
                    m.Nombre AS MedicoNombre, m.Especialidad AS MedicoEspecialidad
                FROM Cita c
                INNER JOIN Paciente p ON c.IdPaciente = p.Id
                INNER JOIN Medico m ON c.IdMedico = m.Id
                WHERE c.IdMedico = ?
                ORDER BY c.FechaHora
            """
            cursor.execute(query, (id_medico,))
            citas = []
            for row in cursor.fetchall():
                cita = Cita(
                    id=row.Id,
                    id_paciente=row.IdPaciente,
                    id_medico=row.IdMedico,
                    fecha_hora=row.FechaHora,
                    motivo=row.Motivo
                )
                # Crear objetos relacionados con datos parciales
                cita.paciente = Paciente(
                    id=row.IdPaciente,
                    nombre=row.PacienteNombre,
                    apellido=row.PacienteApellido
                )
                cita.medico = Medico(
                    id=row.IdMedico,
                    nombre=row.MedicoNombre,
                    especialidad=row.MedicoEspecialidad
                )
                citas.append(cita)
            return citas
        except Exception as e:
            print(f"Error al obtener citas por médico: {e}")
            raise e
    
    @staticmethod
    def obtener_por_fecha(fecha_inicio, fecha_fin):
        """Obtiene citas en un rango de fechas"""
        db = DatabaseConnection()
        try:
            cursor = db.get_cursor()
            query = """
                SELECT 
                    c.Id, c.IdPaciente, c.IdMedico, c.FechaHora, c.Motivo,
                    p.Nombre AS PacienteNombre, p.Apellido AS PacienteApellido,
                    m.Nombre AS MedicoNombre, m.Especialidad AS MedicoEspecialidad
                FROM Cita c
                INNER JOIN Paciente p ON c.IdPaciente = p.Id
                INNER JOIN Medico m ON c.IdMedico = m.Id
                WHERE c.FechaHora BETWEEN ? AND ?
                ORDER BY c.FechaHora
            """
            cursor.execute(query, (fecha_inicio, fecha_fin))
            citas = []
            for row in cursor.fetchall():
                cita = Cita(
                    id=row.Id,
                    id_paciente=row.IdPaciente,
                    id_medico=row.IdMedico,
                    fecha_hora=row.FechaHora,
                    motivo=row.Motivo
                )
                # Crear objetos relacionados con datos parciales
                cita.paciente = Paciente(
                    id=row.IdPaciente,
                    nombre=row.PacienteNombre,
                    apellido=row.PacienteApellido
                )
                cita.medico = Medico(
                    id=row.IdMedico,
                    nombre=row.MedicoNombre,
                    especialidad=row.MedicoEspecialidad
                )
                citas.append(cita)
            return citas
        except Exception as e:
            print(f"Error al obtener citas por fecha: {e}")
            raise e
    
    @staticmethod
    def actualizar(cita):
        """Actualiza los datos de una cita existente"""
        db = DatabaseConnection()
        try:
            cursor = db.get_cursor()
            query = """
                UPDATE Cita 
                SET IdPaciente = ?, IdMedico = ?, FechaHora = ?, Motivo = ?
                WHERE Id = ?
            """
            cursor.execute(
                query, 
                (cita.id_paciente, cita.id_medico, cita.fecha_hora, cita.motivo, cita.id)
            )
            db.commit()
            return True
        except Exception as e:
            db.rollback()
            print(f"Error al actualizar cita: {e}")
            raise e
    
    @staticmethod
    def eliminar(id):
        """Elimina una cita por su ID"""
        db = DatabaseConnection()
        try:
            cursor = db.get_cursor()
            query = "DELETE FROM Cita WHERE Id = ?"
            cursor.execute(query, (id,))
            db.commit()
            return True, "Cita eliminada correctamente."
        except Exception as e:
            db.rollback()
            print(f"Error al eliminar cita: {e}")
            return False, f"Error al eliminar cita: {str(e)}"
    
    def __str__(self):
        """Representación de cadena del objeto cita"""
        paciente_info = f"{self.paciente.nombre} {self.paciente.apellido}" if self.paciente else f"Paciente ID: {self.id_paciente}"
        medico_info = f"Dr(a). {self.medico.nombre}" if self.medico else f"Médico ID: {self.id_medico}"
        fecha_formateada = self.fecha_hora.strftime("%d-%m-%Y %H:%M") if self.fecha_hora else "Sin fecha"
        
        return f"Cita: {fecha_formateada} - {paciente_info} con {medico_info} - {self.motivo}"