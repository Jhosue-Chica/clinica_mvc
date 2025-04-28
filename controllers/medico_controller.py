from models.medico import Medico

class MedicoController:
    """Controlador para gestionar operaciones con médicos"""
    
    @staticmethod
    def crear_medico(nombre, especialidad, email=None):
        """
        Crea un nuevo médico
        
        Args:
            nombre (str): Nombre completo del médico
            especialidad (str): Especialidad médica
            email (str, opcional): Correo electrónico del médico
            
        Returns:
            tuple: (éxito, mensaje o médico)
        """
        try:
            # Crear el nuevo médico
            nuevo_medico = Medico(
                nombre=nombre,
                especialidad=especialidad,
                email=email
            )
            
            # Guardar en la base de datos
            medico_creado = Medico.crear(nuevo_medico)
            return True, medico_creado
            
        except Exception as e:
            return False, f"Error al crear médico: {str(e)}"
    
    @staticmethod
    def listar_medicos():
        """
        Obtiene la lista de todos los médicos
        
        Returns:
            list: Lista de objetos Medico
        """
        try:
            return Medico.obtener_todos()
        except Exception as e:
            print(f"Error al listar médicos: {e}")
            return []
    
    @staticmethod
    def buscar_medico_por_id(id):
        """
        Busca un médico por su ID
        
        Args:
            id (int): ID del médico a buscar
            
        Returns:
            Medico or None: El médico encontrado o None
        """
        try:
            return Medico.obtener_por_id(id)
        except Exception as e:
            print(f"Error al buscar médico: {e}")
            return None
    
    @staticmethod
    def buscar_medicos_por_especialidad(especialidad):
        """
        Busca médicos por su especialidad
        
        Args:
            especialidad (str): Especialidad médica a buscar
            
        Returns:
            list: Lista de médicos que coinciden con la especialidad
        """
        try:
            return Medico.obtener_por_especialidad(especialidad)
        except Exception as e:
            print(f"Error al buscar médicos por especialidad: {e}")
            return []
    
    @staticmethod
    def actualizar_medico(id, nombre, especialidad, email=None):
        """
        Actualiza los datos de un médico existente
        
        Args:
            id (int): ID del médico a actualizar
            nombre (str): Nombre completo del médico
            especialidad (str): Especialidad médica
            email (str, opcional): Correo electrónico del médico
            
        Returns:
            tuple: (éxito, mensaje)
        """
        try:
            # Verificar que el médico existe
            medico = Medico.obtener_por_id(id)
            if not medico:
                return False, f"No se encontró el médico con ID {id}"
            
            # Actualizar datos
            medico.nombre = nombre
            medico.especialidad = especialidad
            medico.email = email
            
            # Guardar cambios
            resultado = Medico.actualizar(medico)
            if resultado:
                return True, "Médico actualizado correctamente"
            else:
                return False, "No se pudo actualizar el médico"
                
        except Exception as e:
            return False, f"Error al actualizar médico: {str(e)}"
    
    @staticmethod
    def eliminar_medico(id):
        """
        Elimina un médico de la base de datos
        
        Args:
            id (int): ID del médico a eliminar
            
        Returns:
            tuple: (éxito, mensaje)
        """
        try:
            # Verificar que el médico existe
            medico = Medico.obtener_por_id(id)
            if not medico:
                return False, f"No se encontró el médico con ID {id}"
            
            # Intentar eliminar
            return Medico.eliminar(id)
                
        except Exception as e:
            return False, f"Error al eliminar médico: {str(e)}"