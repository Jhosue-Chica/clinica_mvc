from datetime import datetime
from models.cita import Cita
from models.paciente import Paciente
from models.medico import Medico

class CitaController:
    """Controlador para gestionar operaciones con citas médicas"""
    
    @staticmethod
    def crear_cita(id_paciente, id_medico, fecha_hora, motivo=None):
        """
        Crea una nueva cita médica
        
        Args:
            id_paciente (int): ID del paciente
            id_medico (int): ID del médico
            fecha_hora (str): Fecha y hora en formato DD-MM-YYYY HH:MM
            motivo (str, opcional): Motivo de la consulta
            
        Returns:
            tuple: (éxito, mensaje o cita)
        """
        try:
            # Verificar que existen el paciente y el médico
            paciente = Paciente.obtener_por_id(id_paciente)
            if not paciente:
                return False, f"No existe un paciente con ID {id_paciente}"
            
            medico = Medico.obtener_por_id(id_medico)
            if not medico:
                return False, f"No existe un médico con ID {id_medico}"
            
            # Convertir la fecha y hora de texto a objeto datetime
            try:
                fecha_obj = datetime.strptime(fecha_hora, "%d-%m-%Y %H:%M")
            except ValueError:
                return False, "Formato de fecha y hora incorrecto. Use DD-MM-YYYY HH:MM"
            
            # Crear la nueva cita
            nueva_cita = Cita(
                id_paciente=id_paciente,
                id_medico=id_medico,
                fecha_hora=fecha_obj,
                motivo=motivo
            )
            
            # Guardar en la base de datos
            cita_creada = Cita.crear(nueva_cita)
            
            # Completar los datos relacionados para devolver
            cita_creada.paciente = paciente
            cita_creada.medico = medico
            
            return True, cita_creada
            
        except Exception as e:
            return False, f"Error al crear cita: {str(e)}"
    
    @staticmethod
    def listar_citas():
        """
        Obtiene la lista de todas las citas
        
        Returns:
            list: Lista de objetos Cita con sus relaciones
        """
        try:
            return Cita.obtener_todas()
        except Exception as e:
            print(f"Error al listar citas: {e}")
            return []
    
    @staticmethod
    def buscar_cita_por_id(id):
        """
        Busca una cita por su ID
        
        Args:
            id (int): ID de la cita a buscar
            
        Returns:
            Cita or None: La cita encontrada o None
        """
        try:
            return Cita.obtener_por_id(id)
        except Exception as e:
            print(f"Error al buscar cita: {e}")
            return None
    
    @staticmethod
    def buscar_citas_por_paciente(id_paciente):
        """
        Busca citas de un paciente específico
        
        Args:
            id_paciente (int): ID del paciente
            
        Returns:
            list: Lista de citas del paciente
        """
        try:
            # Verificar que existe el paciente
            paciente = Paciente.obtener_por_id(id_paciente)
            if not paciente:
                print(f"No existe un paciente con ID {id_paciente}")
                return []
            
            return Cita.obtener_por_paciente(id_paciente)
        except Exception as e:
            print(f"Error al buscar citas por paciente: {e}")
            return []
    
    @staticmethod
    def buscar_citas_por_medico(id_medico):
        """
        Busca citas de un médico específico
        
        Args:
            id_medico (int): ID del médico
            
        Returns:
            list: Lista de citas del médico
        """
        try:
            # Verificar que existe el médico
            medico = Medico.obtener_por_id(id_medico)
            if not medico:
                print(f"No existe un médico con ID {id_medico}")
                return []
            
            return Cita.obtener_por_medico(id_medico)
        except Exception as e:
            print(f"Error al buscar citas por médico: {e}")
            return []
    
    @staticmethod
    def buscar_citas_por_fecha(fecha_inicio, fecha_fin=None):
        """
        Busca citas en un rango de fechas
        
        Args:
            fecha_inicio (str): Fecha de inicio en formato DD-MM-YYYY
            fecha_fin (str, opcional): Fecha de fin en formato DD-MM-YYYY
            
        Returns:
            list: Lista de citas en el rango de fechas
        """
        try:
            # Convertir las fechas de texto a objetos datetime
            try:
                fecha_inicio_obj = datetime.strptime(fecha_inicio, "%d-%m-%Y")
                
                # Si no se proporciona fecha_fin, usar la misma fecha de inicio
                if fecha_fin:
                    fecha_fin_obj = datetime.strptime(fecha_fin, "%d-%m-%Y")
                    # Ajustar al final del día
                    fecha_fin_obj = fecha_fin_obj.replace(hour=23, minute=59, second=59)
                else:
                    fecha_fin_obj = fecha_inicio_obj.replace(hour=23, minute=59, second=59)
                
                # Ajustar al inicio del día para fecha_inicio
                fecha_inicio_obj = fecha_inicio_obj.replace(hour=0, minute=0, second=0)
                
            except ValueError:
                print("Formato de fecha incorrecto. Use DD-MM-YYYY")
                return []
            
            return Cita.obtener_por_fecha(fecha_inicio_obj, fecha_fin_obj)
        except Exception as e:
            print(f"Error al buscar citas por fecha: {e}")
            return []
    
    @staticmethod
    def actualizar_cita(id, id_paciente, id_medico, fecha_hora, motivo=None):
        """
        Actualiza los datos de una cita existente
        
        Args:
            id (int): ID de la cita a actualizar
            id_paciente (int): ID del paciente
            id_medico (int): ID del médico
            fecha_hora (str): Fecha y hora en formato DD-MM-YYYY HH:MM
            motivo (str, opcional): Motivo de la consulta
            
        Returns:
            tuple: (éxito, mensaje)
        """
        try:
            # Verificar que la cita existe
            cita = Cita.obtener_por_id(id)
            if not cita:
                return False, f"No se encontró la cita con ID {id}"
            
            # Verificar que existen el paciente y el médico
            paciente = Paciente.obtener_por_id(id_paciente)
            if not paciente:
                return False, f"No existe un paciente con ID {id_paciente}"
            
            medico = Medico.obtener_por_id(id_medico)
            if not medico:
                return False, f"No existe un médico con ID {id_medico}"
            
            # Convertir la fecha y hora de texto a objeto datetime
            try:
                fecha_obj = datetime.strptime(fecha_hora, "%d-%m-%Y %H:%M")
            except ValueError:
                return False, "Formato de fecha y hora incorrecto. Use DD-MM-YYYY HH:MM"
            
            # Actualizar datos
            cita.id_paciente = id_paciente
            cita.id_medico = id_medico
            cita.fecha_hora = fecha_obj
            cita.motivo = motivo
            
            # Guardar cambios
            resultado = Cita.actualizar(cita)
            if resultado:
                return True, "Cita actualizada correctamente"
            else:
                return False, "No se pudo actualizar la cita"
                
        except Exception as e:
            return False, f"Error al actualizar cita: {str(e)}"
    
    @staticmethod
    def eliminar_cita(id):
        """
        Elimina una cita de la base de datos
        
        Args:
            id (int): ID de la cita a eliminar
            
        Returns:
            tuple: (éxito, mensaje)
        """
        try:
            # Verificar que la cita existe
            cita = Cita.obtener_por_id(id)
            if not cita:
                return False, f"No se encontró la cita con ID {id}"
            
            # Intentar eliminar
            return Cita.eliminar(id)
                
        except Exception as e:
            return False, f"Error al eliminar cita: {str(e)}"