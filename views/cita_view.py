from tabulate import tabulate
from datetime import datetime
from views.menu_view import MenuView
from models.paciente import Paciente
from models.medico import Medico

class CitaView:
    """Vista para la gestión de citas médicas"""
    
    @staticmethod
    def solicitar_datos_cita(pacientes, medicos, editar=False):
        """
        Solicita al usuario los datos de una cita
        
        Args:
            pacientes: Lista de pacientes disponibles
            medicos: Lista de médicos disponibles
            editar (bool): Indica si estamos editando una cita existente
            
        Returns:
            dict: Diccionario con los datos de la cita o None si hubo error
        """
        MenuView.mostrar_titulo("DATOS DE LA CITA")
        
        datos = {}
        
        if editar:
            print("Deje en blanco los campos que no desea modificar")
        
        # Mostrar lista de pacientes para seleccionar
        if not pacientes:
            MenuView.mostrar_mensaje("No hay pacientes registrados", error=True)
            return None
        
        print("\nPacientes disponibles:")
        for p in pacientes:
            print(f"ID: {p.id} - {p.nombre} {p.apellido} (Cédula: {p.cedula})")
        
        # Solicitar ID del paciente
        try:
            datos['id_paciente'] = int(input("\nID del paciente para la cita: "))
            # Verificar que existe
            if not any(p.id == datos['id_paciente'] for p in pacientes):
                MenuView.mostrar_mensaje("El ID del paciente no es válido", error=True)
                return None
        except ValueError:
            MenuView.mostrar_mensaje("ID inválido", error=True)
            return None
        
        # Mostrar lista de médicos para seleccionar
        if not medicos:
            MenuView.mostrar_mensaje("No hay médicos registrados", error=True)
            return None
        
        print("\nMédicos disponibles:")
        for m in medicos:
            print(f"ID: {m.id} - {m.nombre} ({m.especialidad})")
        
        # Solicitar ID del médico
        try:
            datos['id_medico'] = int(input("\nID del médico para la cita: "))
            # Verificar que existe
            if not any(m.id == datos['id_medico'] for m in medicos):
                MenuView.mostrar_mensaje("El ID del médico no es válido", error=True)
                return None
        except ValueError:
            MenuView.mostrar_mensaje("ID inválido", error=True)
            return None
        
        # Solicitar fecha y hora
        while True:
            try:
                fecha_hora = input("\nFecha y hora (DD-MM-YYYY HH:MM): ")
                if fecha_hora:
                    # Validar formato de fecha y hora
                    datetime.strptime(fecha_hora, "%d-%m-%Y %H:%M")
                    datos['fecha_hora'] = fecha_hora
                    break
                elif editar:
                    datos['fecha_hora'] = ''
                    break
                else:
                    print("La fecha y hora son obligatorias")
            except ValueError:
                print("Formato de fecha y hora incorrecto. Use DD-MM-YYYY HH:MM")
        
        # Solicitar motivo de la cita
        datos['motivo'] = input("\nMotivo de la cita: ")
        
        return datos
    
    @staticmethod
    def mostrar_cita(cita):
        """
        Muestra los detalles de una cita
        
        Args:
            cita: Objeto Cita a mostrar
        """
        if not cita:
            MenuView.mostrar_mensaje("No se encontró la cita", error=True)
            return
        
        MenuView.mostrar_titulo(f"INFORMACIÓN DE LA CITA - ID: {cita.id}")
        
        # Formatear fecha para mostrar
        fecha_hora = cita.fecha_hora.strftime("%d-%m-%Y %H:%M") if cita.fecha_hora else "No especificada"
        
        # Preparar información del paciente y médico
        paciente_info = f"{cita.paciente.nombre} {cita.paciente.apellido}" if cita.paciente else f"ID: {cita.id_paciente}"
        medico_info = f"Dr(a). {cita.medico.nombre} - {cita.medico.especialidad}" if cita.medico else f"ID: {cita.id_medico}"
        
        datos = [
            ["Fecha y hora", fecha_hora],
            ["Paciente", paciente_info],
            ["Médico", medico_info],
            ["Motivo", cita.motivo if cita.motivo else "No especificado"]
        ]
        
        print(tabulate(datos, tablefmt="fancy_grid"))
        input("\nPresione Enter para continuar...")
    
    @staticmethod
    def listar_citas(citas):
        """
        Muestra una lista de citas
        
        Args:
            citas: Lista de objetos Cita
        """
        if not citas:
            MenuView.mostrar_mensaje("No hay citas registradas", error=False)
            return
        
        MenuView.mostrar_titulo("LISTA DE CITAS")
        
        # Preparar datos para mostrar en tabla
        datos = []
        for c in citas:
            fecha_hora = c.fecha_hora.strftime("%d-%m-%Y %H:%M") if c.fecha_hora else "N/A"
            paciente_info = f"{c.paciente.nombre} {c.paciente.apellido}" if c.paciente else f"ID: {c.id_paciente}"
            medico_info = f"Dr(a). {c.medico.nombre}" if c.medico else f"ID: {c.id_medico}"
            motivo = c.motivo if c.motivo else "N/A"
            
            # Limitar longitud del motivo para la tabla
            if motivo and len(motivo) > 30:
                motivo = motivo[:27] + "..."
                
            datos.append([c.id, fecha_hora, paciente_info, medico_info, motivo])
        
        headers = ["ID", "Fecha y hora", "Paciente", "Médico", "Motivo"]
        print(tabulate(datos, headers=headers, tablefmt="fancy_grid"))
        input("\nPresione Enter para continuar...")
    
    @staticmethod
    def solicitar_id_cita():
        """
        Solicita el ID de una cita
        
        Returns:
            int: ID de la cita o None si no es válido
        """
        try:
            return int(input("ID de la cita: "))
        except ValueError:
            MenuView.mostrar_mensaje("ID inválido", error=True)
            return None