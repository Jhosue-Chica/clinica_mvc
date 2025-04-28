from tabulate import tabulate
from datetime import datetime
from views.menu_view import MenuView

class PacienteView:
    """Vista para la gestión de pacientes"""
    
    @staticmethod
    def solicitar_datos_paciente(editar=False):
        """
        Solicita al usuario los datos de un paciente
        
        Args:
            editar (bool): Indica si estamos editando un paciente existente
            
        Returns:
            dict: Diccionario con los datos del paciente
        """
        MenuView.mostrar_titulo("DATOS DEL PACIENTE")
        
        datos = {}
        
        if editar:
            print("Deje en blanco los campos que no desea modificar")
        
        # Solicitar información
        datos['nombre'] = input("Nombre: ")
        datos['apellido'] = input("Apellido: ")
        datos['cedula'] = input("Número de cédula: ")
        
        while True:
            try:
                fecha_nacimiento = input("Fecha de nacimiento (DD-MM-YYYY): ")
                if fecha_nacimiento:
                    # Validar formato de fecha
                    datetime.strptime(fecha_nacimiento, "%d-%m-%Y")
                datos['fecha_nacimiento'] = fecha_nacimiento
                break
            except ValueError:
                print("Formato de fecha incorrecto. Use DD-MM-YYYY")
        
        datos['email'] = input("Email (opcional): ")
        
        return datos
    
    @staticmethod
    def mostrar_paciente(paciente):
        """
        Muestra los detalles de un paciente
        
        Args:
            paciente: Objeto Paciente a mostrar
        """
        if not paciente:
            MenuView.mostrar_mensaje("No se encontró el paciente", error=True)
            return
        
        MenuView.mostrar_titulo(f"INFORMACIÓN DEL PACIENTE - ID: {paciente.id}")
        
        # Formatear fecha para mostrar
        fecha_nacimiento = paciente.fecha_nacimiento.strftime("%d-%m-%Y") if paciente.fecha_nacimiento else "No especificada"
        
        datos = [
            ["Nombre", paciente.nombre],
            ["Apellido", paciente.apellido],
            ["Cédula", paciente.cedula],
            ["Fecha de nacimiento", fecha_nacimiento],
            ["Email", paciente.email if paciente.email else "No especificado"]
        ]
        
        print(tabulate(datos, tablefmt="fancy_grid"))
        input("\nPresione Enter para continuar...")
    
    @staticmethod
    def listar_pacientes(pacientes):
        """
        Muestra una lista de pacientes
        
        Args:
            pacientes: Lista de objetos Paciente
        """
        if not pacientes:
            MenuView.mostrar_mensaje("No hay pacientes registrados", error=False)
            return
        
        MenuView.mostrar_titulo("LISTA DE PACIENTES")
        
        # Preparar datos para mostrar en tabla
        datos = []
        for p in pacientes:
            fecha_nacimiento = p.fecha_nacimiento.strftime("%d-%m-%Y") if p.fecha_nacimiento else "N/A"
            datos.append([p.id, f"{p.nombre} {p.apellido}", p.cedula, fecha_nacimiento])
        
        headers = ["ID", "Nombre completo", "Cédula", "Fecha nacimiento"]
        print(tabulate(datos, headers=headers, tablefmt="fancy_grid"))
        input("\nPresione Enter para continuar...")
    
    @staticmethod
    def solicitar_id_paciente():
        """
        Solicita el ID de un paciente
        
        Returns:
            int: ID del paciente o None si no es válido
        """
        try:
            return int(input("ID del paciente: "))
        except ValueError:
            MenuView.mostrar_mensaje("ID inválido", error=True)
            return None
    
    @staticmethod
    def solicitar_cedula_paciente():
        """
        Solicita la cédula de un paciente
        
        Returns:
            str: Cédula del paciente
        """
        return input("Cédula del paciente: ")