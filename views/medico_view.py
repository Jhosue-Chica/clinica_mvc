from tabulate import tabulate
from views.menu_view import MenuView

class MedicoView:
    """Vista para la gestión de médicos"""
    
    @staticmethod
    def solicitar_datos_medico(editar=False):
        """
        Solicita al usuario los datos de un médico
        
        Args:
            editar (bool): Indica si estamos editando un médico existente
            
        Returns:
            dict: Diccionario con los datos del médico
        """
        MenuView.mostrar_titulo("DATOS DEL MÉDICO")
        
        datos = {}
        
        if editar:
            print("Deje en blanco los campos que no desea modificar")
        
        # Solicitar información
        datos['nombre'] = input("Nombre completo: ")
        datos['especialidad'] = input("Especialidad: ")
        datos['email'] = input("Email (opcional): ")
        
        return datos
    
    @staticmethod
    def mostrar_medico(medico):
        """
        Muestra los detalles de un médico
        
        Args:
            medico: Objeto Medico a mostrar
        """
        if not medico:
            MenuView.mostrar_mensaje("No se encontró el médico", error=True)
            return
        
        MenuView.mostrar_titulo(f"INFORMACIÓN DEL MÉDICO - ID: {medico.id}")
        
        datos = [
            ["Nombre", medico.nombre],
            ["Especialidad", medico.especialidad],
            ["Email", medico.email if medico.email else "No especificado"]
        ]
        
        print(tabulate(datos, tablefmt="fancy_grid"))
        input("\nPresione Enter para continuar...")
    
    @staticmethod
    def listar_medicos(medicos):
        """
        Muestra una lista de médicos
        
        Args:
            medicos: Lista de objetos Medico
        """
        if not medicos:
            MenuView.mostrar_mensaje("No hay médicos registrados", error=False)
            return
        
        MenuView.mostrar_titulo("LISTA DE MÉDICOS")
        
        # Preparar datos para mostrar en tabla
        datos = []
        for m in medicos:
            datos.append([m.id, m.nombre, m.especialidad, m.email if m.email else "N/A"])
        
        headers = ["ID", "Nombre", "Especialidad", "Email"]
        print(tabulate(datos, headers=headers, tablefmt="fancy_grid"))
        input("\nPresione Enter para continuar...")
    
    @staticmethod
    def solicitar_id_medico():
        """
        Solicita el ID de un médico
        
        Returns:
            int: ID del médico o None si no es válido
        """
        try:
            return int(input("ID del médico: "))
        except ValueError:
            MenuView.mostrar_mensaje("ID inválido", error=True)
            return None
    
    @staticmethod
    def solicitar_especialidad():
        """
        Solicita una especialidad médica para filtrar
        
        Returns:
            str: Especialidad médica
        """
        return input("Especialidad a buscar: ")