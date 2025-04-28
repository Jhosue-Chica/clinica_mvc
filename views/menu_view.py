import os
from datetime import datetime

class MenuView:
    """Vista principal para la navegación por menús"""
    
    @staticmethod
    def limpiar_pantalla():
        """Limpia la pantalla de la consola"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def mostrar_titulo(titulo):
        """Muestra un título formateado"""
        MenuView.limpiar_pantalla()
        print("\n" + "=" * 50)
        print(f"{titulo.center(50)}")
        print("=" * 50 + "\n")
    
    @staticmethod
    def mostrar_menu_principal():
        """Muestra el menú principal de la aplicación"""
        MenuView.mostrar_titulo("SISTEMA DE GESTIÓN DE CLÍNICA")
        print("1. Gestión de Pacientes")
        print("2. Gestión de Médicos")
        print("3. Gestión de Citas")
        print("0. Salir")
        return input("\nSeleccione una opción: ")
    
    @staticmethod
    def mostrar_menu_pacientes():
        """Muestra el menú de gestión de pacientes"""
        MenuView.mostrar_titulo("GESTIÓN DE PACIENTES")
        print("1. Registrar nuevo paciente")
        print("2. Listar todos los pacientes")
        print("3. Buscar paciente por ID")
        print("4. Buscar paciente por cédula")
        print("5. Actualizar datos de paciente")
        print("6. Eliminar paciente")
        print("0. Volver al menú principal")
        return input("\nSeleccione una opción: ")
    
    @staticmethod
    def mostrar_menu_medicos():
        """Muestra el menú de gestión de médicos"""
        MenuView.mostrar_titulo("GESTIÓN DE MÉDICOS")
        print("1. Registrar nuevo médico")
        print("2. Listar todos los médicos")
        print("3. Buscar médico por ID")
        print("4. Buscar médicos por especialidad")
        print("5. Actualizar datos de médico")
        print("6. Eliminar médico")
        print("0. Volver al menú principal")
        return input("\nSeleccione una opción: ")
    
    @staticmethod
    def mostrar_menu_citas():
        """Muestra el menú de gestión de citas"""
        MenuView.mostrar_titulo("GESTIÓN DE CITAS")
        print("1. Registrar nueva cita")
        print("2. Listar todas las citas")
        print("3. Buscar cita por ID")
        print("4. Buscar citas por paciente")
        print("5. Buscar citas por médico")
        print("6. Buscar citas por fecha")
        print("7. Actualizar datos de cita")
        print("8. Eliminar cita")
        print("0. Volver al menú principal")
        return input("\nSeleccione una opción: ")
    
    @staticmethod
    def mostrar_mensaje(mensaje, error=False):
        """Muestra un mensaje al usuario"""
        tipo = "ERROR" if error else "MENSAJE"
        print(f"\n[{tipo}] {mensaje}")
        input("\nPresione Enter para continuar...")
    
    @staticmethod
    def confirmar_accion(mensaje):
        """Solicita confirmación para una acción"""
        print(f"\n{mensaje}")
        respuesta = input("¿Está seguro? (s/n): ").lower()
        return respuesta == 's' or respuesta == 'si' or respuesta == 'sí'
    
    @staticmethod
    def obtener_fecha():
        """Solicita una fecha al usuario en formato DD-MM-YYYY"""
        while True:
            fecha_str = input("Fecha (DD-MM-YYYY): ")
            try:
                fecha_obj = datetime.strptime(fecha_str, "%d-%m-%Y")
                return fecha_str
            except ValueError:
                print("Formato de fecha incorrecto. Use DD-MM-YYYY")
    
    @staticmethod
    def obtener_fecha_hora():
        """Solicita una fecha y hora al usuario en formato DD-MM-YYYY HH:MM"""
        while True:
            fecha_hora_str = input("Fecha y hora (DD-MM-YYYY HH:MM): ")
            try:
                fecha_hora_obj = datetime.strptime(fecha_hora_str, "%d-%m-%Y %H:%M")
                return fecha_hora_str
            except ValueError:
                print("Formato de fecha y hora incorrecto. Use DD-MM-YYYY HH:MM")