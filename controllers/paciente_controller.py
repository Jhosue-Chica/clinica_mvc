from datetime import datetime
from models.paciente import Paciente

class PacienteController:
    """Controlador para gestionar operaciones con pacientes"""
    
    @staticmethod
    def crear_paciente(nombre, apellido, cedula, fecha_nacimiento, email=None):
        """
        Crea un nuevo paciente
        
        Args:
            nombre (str): Nombre del paciente
            apellido (str): Apellido del paciente
            cedula (str): Número de cédula del paciente
            fecha_nacimiento (str): Fecha de nacimiento en formato DD-MM-YYYY
            email (str, opcional): Correo electrónico del paciente
            
        Returns:
            tuple: (éxito, mensaje o paciente)
        """
        try:
            # Verificar si ya existe un paciente con esa cédula
            paciente_existente = Paciente.obtener_por_cedula(cedula)
            if paciente_existente:
                return False, f"Ya existe un paciente con la cédula {cedula}"
            
            # Convertir la fecha de texto a objeto date
            try:
                fecha_obj = datetime.strptime(fecha_nacimiento, "%d-%m-%Y").date()
            except ValueError:
                return False, "Formato de fecha incorrecto. Use DD-MM-YYYY"
            
            # Crear el nuevo paciente
            nuevo_paciente = Paciente(
                nombre=nombre,
                apellido=apellido,
                cedula=cedula,
                fecha_nacimiento=fecha_obj,
                email=email
            )
            
            # Guardar en la base de datos
            paciente_creado = Paciente.crear(nuevo_paciente)
            return True, paciente_creado
            
        except Exception as e:
            return False, f"Error al crear paciente: {str(e)}"
    
    @staticmethod
    def listar_pacientes():
        """
        Obtiene la lista de todos los pacientes
        
        Returns:
            list: Lista de objetos Paciente
        """
        try:
            return Paciente.obtener_todos()
        except Exception as e:
            print(f"Error al listar pacientes: {e}")
            return []
    
    @staticmethod
    def buscar_paciente_por_id(id):
        """
        Busca un paciente por su ID
        
        Args:
            id (int): ID del paciente a buscar
            
        Returns:
            Paciente or None: El paciente encontrado o None
        """
        try:
            return Paciente.obtener_por_id(id)
        except Exception as e:
            print(f"Error al buscar paciente: {e}")
            return None
    
    @staticmethod
    def buscar_paciente_por_cedula(cedula):
        """
        Busca un paciente por su número de cédula
        
        Args:
            cedula (str): Número de cédula del paciente
            
        Returns:
            Paciente or None: El paciente encontrado o None
        """
        try:
            return Paciente.obtener_por_cedula(cedula)
        except Exception as e:
            print(f"Error al buscar paciente por cédula: {e}")
            return None
    
    @staticmethod
    def actualizar_paciente(id, nombre, apellido, cedula, fecha_nacimiento, email=None):
        """
        Actualiza los datos de un paciente existente
        
        Args:
            id (int): ID del paciente a actualizar
            nombre (str): Nombre del paciente
            apellido (str): Apellido del paciente
            cedula (str): Número de cédula del paciente
            fecha_nacimiento (str): Fecha de nacimiento en formato DD-MM-YYYY
            email (str, opcional): Correo electrónico del paciente
            
        Returns:
            tuple: (éxito, mensaje)
        """
        try:
            # Verificar que el paciente existe
            paciente = Paciente.obtener_por_id(id)
            if not paciente:
                return False, f"No se encontró el paciente con ID {id}"
            
            # Verificar si la cédula ya está en uso por otro paciente
            if paciente.cedula != cedula:
                paciente_existente = Paciente.obtener_por_cedula(cedula)
                if paciente_existente and paciente_existente.id != id:
                    return False, f"La cédula {cedula} ya está registrada para otro paciente"
            
            # Convertir la fecha de texto a objeto date
            try:
                fecha_obj = datetime.strptime(fecha_nacimiento, "%d-%m-%Y").date()
            except ValueError:
                return False, "Formato de fecha incorrecto. Use DD-MM-YYYY"
            
            # Actualizar datos
            paciente.nombre = nombre
            paciente.apellido = apellido
            paciente.cedula = cedula
            paciente.fecha_nacimiento = fecha_obj
            paciente.email = email
            
            # Guardar cambios
            resultado = Paciente.actualizar(paciente)
            if resultado:
                return True, "Paciente actualizado correctamente"
            else:
                return False, "No se pudo actualizar el paciente"
                
        except Exception as e:
            return False, f"Error al actualizar paciente: {str(e)}"
    
    @staticmethod
    def eliminar_paciente(id):
        """
        Elimina un paciente de la base de datos
        
        Args:
            id (int): ID del paciente a eliminar
            
        Returns:
            tuple: (éxito, mensaje)
        """
        try:
            # Verificar que el paciente existe
            paciente = Paciente.obtener_por_id(id)
            if not paciente:
                return False, f"No se encontró el paciente con ID {id}"
            
            # Intentar eliminar
            return Paciente.eliminar(id)
                
        except Exception as e:
            return False, f"Error al eliminar paciente: {str(e)}"