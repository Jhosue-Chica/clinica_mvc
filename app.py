#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Sistema de Gestión de Clínica Médica
Este programa implementa un CRUD completo para gestionar pacientes, médicos y citas médicas.
"""

import os
import sys
from datetime import datetime
from dotenv import load_dotenv

# Importar componentes MVC
from models import Paciente, Medico, Cita
from controllers import PacienteController, MedicoController, CitaController
from views import MenuView, PacienteView, MedicoView, CitaView
from config.database import DatabaseConnection

class App:
    """Clase principal de la aplicación"""
    
    def __init__(self):
        """Inicializar la aplicación"""
        # Cargar variables de entorno
        load_dotenv()
        
        # Inicializar conexión a la base de datos
        try:
            self.db = DatabaseConnection()
        except Exception as e:
            print(f"Error al conectar con la base de datos: {e}")
            print("Verifique su archivo .env con las credenciales de conexión")
            print("Ejemplo de archivo .env:")
            print("DB_SERVER=localhost")
            print("DB_NAME=ClinicaDB")
            print("DB_USER=usuario")
            print("DB_PASSWORD=contraseña")
            sys.exit(1)
    
    def ejecutar(self):
        """Método principal que ejecuta la aplicación"""
        try:
            while True:
                opcion = MenuView.mostrar_menu_principal()
                
                if opcion == "1":
                    self.menu_pacientes()
                elif opcion == "2":
                    self.menu_medicos()
                elif opcion == "3":
                    self.menu_citas()
                elif opcion == "0":
                    self.salir()
                    break
                else:
                    MenuView.mostrar_mensaje("Opción inválida", error=True)
        except KeyboardInterrupt:
            self.salir()
        except Exception as e:
            print(f"Error inesperado: {e}")
            self.salir()
    
    def menu_pacientes(self):
        """Gestión del menú de pacientes"""
        while True:
            opcion = MenuView.mostrar_menu_pacientes()
            
            if opcion == "1":
                # Registrar nuevo paciente
                datos = PacienteView.solicitar_datos_paciente()
                if datos['nombre'] and datos['apellido'] and datos['cedula'] and datos['fecha_nacimiento']:
                    exito, resultado = PacienteController.crear_paciente(
                        datos['nombre'], datos['apellido'], datos['cedula'],
                        datos['fecha_nacimiento'], datos['email']
                    )
                    if exito:
                        MenuView.mostrar_mensaje(f"Paciente registrado con éxito. ID: {resultado.id}")
                    else:
                        MenuView.mostrar_mensaje(resultado, error=True)
                else:
                    MenuView.mostrar_mensaje("Todos los campos son obligatorios excepto el email", error=True)
            
            elif opcion == "2":
                # Listar todos los pacientes
                pacientes = PacienteController.listar_pacientes()
                PacienteView.listar_pacientes(pacientes)
            
            elif opcion == "3":
                # Buscar paciente por ID
                id_paciente = PacienteView.solicitar_id_paciente()
                if id_paciente is not None:
                    paciente = PacienteController.buscar_paciente_por_id(id_paciente)
                    PacienteView.mostrar_paciente(paciente)
            
            elif opcion == "4":
                # Buscar paciente por cédula
                cedula = PacienteView.solicitar_cedula_paciente()
                if cedula:
                    paciente = PacienteController.buscar_paciente_por_cedula(cedula)
                    PacienteView.mostrar_paciente(paciente)
            
            elif opcion == "5":
                # Actualizar datos de paciente
                id_paciente = PacienteView.solicitar_id_paciente()
                if id_paciente is not None:
                    paciente_actual = PacienteController.buscar_paciente_por_id(id_paciente)
                    if paciente_actual:
                        PacienteView.mostrar_paciente(paciente_actual)
                        datos = PacienteView.solicitar_datos_paciente(editar=True)
                        
                        # Usar valores existentes si no se proporcionan nuevos
                        nombre = datos['nombre'] if datos['nombre'] else paciente_actual.nombre
                        apellido = datos['apellido'] if datos['apellido'] else paciente_actual.apellido
                        cedula = datos['cedula'] if datos['cedula'] else paciente_actual.cedula
                        fecha_nacimiento = datos['fecha_nacimiento'] if datos['fecha_nacimiento'] else paciente_actual.fecha_nacimiento.strftime("%d-%m-%Y")
                        email = datos['email'] if datos['email'] else paciente_actual.email
                        
                        exito, mensaje = PacienteController.actualizar_paciente(
                            id_paciente, nombre, apellido, cedula, fecha_nacimiento, email
                        )
                        
                        MenuView.mostrar_mensaje(mensaje, not exito)
            
            elif opcion == "6":
                # Eliminar paciente
                id_paciente = PacienteView.solicitar_id_paciente()
                if id_paciente is not None:
                    paciente = PacienteController.buscar_paciente_por_id(id_paciente)
                    if paciente:
                        PacienteView.mostrar_paciente(paciente)
                        if MenuView.confirmar_accion("¿Está seguro de eliminar este paciente?"):
                            exito, mensaje = PacienteController.eliminar_paciente(id_paciente)
                            MenuView.mostrar_mensaje(mensaje, not exito)
            
            elif opcion == "0":
                # Volver al menú principal
                break
            
            else:
                MenuView.mostrar_mensaje("Opción inválida", error=True)
    
    def menu_medicos(self):
        """Gestión del menú de médicos"""
        while True:
            opcion = MenuView.mostrar_menu_medicos()
            
            if opcion == "1":
                # Registrar nuevo médico
                datos = MedicoView.solicitar_datos_medico()
                if datos['nombre'] and datos['especialidad']:
                    exito, resultado = MedicoController.crear_medico(
                        datos['nombre'], datos['especialidad'], datos['email']
                    )
                    if exito:
                        MenuView.mostrar_mensaje(f"Médico registrado con éxito. ID: {resultado.id}")
                    else:
                        MenuView.mostrar_mensaje(resultado, error=True)
                else:
                    MenuView.mostrar_mensaje("El nombre y la especialidad son obligatorios", error=True)
            
            elif opcion == "2":
                # Listar todos los médicos
                medicos = MedicoController.listar_medicos()
                MedicoView.listar_medicos(medicos)
            
            elif opcion == "3":
                # Buscar médico por ID
                id_medico = MedicoView.solicitar_id_medico()
                if id_medico is not None:
                    medico = MedicoController.buscar_medico_por_id(id_medico)
                    MedicoView.mostrar_medico(medico)
            
            elif opcion == "4":
                # Buscar médicos por especialidad
                especialidad = MedicoView.solicitar_especialidad()
                if especialidad:
                    medicos = MedicoController.buscar_medicos_por_especialidad(especialidad)
                    MedicoView.listar_medicos(medicos)
            
            elif opcion == "5":
                # Actualizar datos de médico
                id_medico = MedicoView.solicitar_id_medico()
                if id_medico is not None:
                    medico_actual = MedicoController.buscar_medico_por_id(id_medico)
                    if medico_actual:
                        MedicoView.mostrar_medico(medico_actual)
                        datos = MedicoView.solicitar_datos_medico(editar=True)
                        
                        # Usar valores existentes si no se proporcionan nuevos
                        nombre = datos['nombre'] if datos['nombre'] else medico_actual.nombre
                        especialidad = datos['especialidad'] if datos['especialidad'] else medico_actual.especialidad
                        email = datos['email'] if datos['email'] else medico_actual.email
                        
                        exito, mensaje = MedicoController.actualizar_medico(
                            id_medico, nombre, especialidad, email
                        )
                        
                        MenuView.mostrar_mensaje(mensaje, not exito)
            
            elif opcion == "6":
                # Eliminar médico
                id_medico = MedicoView.solicitar_id_medico()
                if id_medico is not None:
                    medico = MedicoController.buscar_medico_por_id(id_medico)
                    if medico:
                        MedicoView.mostrar_medico(medico)
                        if MenuView.confirmar_accion("¿Está seguro de eliminar este médico?"):
                            exito, mensaje = MedicoController.eliminar_medico(id_medico)
                            MenuView.mostrar_mensaje(mensaje, not exito)
            
            elif opcion == "0":
                # Volver al menú principal
                break
            
            else:
                MenuView.mostrar_mensaje("Opción inválida", error=True)
    
    def menu_citas(self):
        """Gestión del menú de citas"""
        while True:
            opcion = MenuView.mostrar_menu_citas()
            
            if opcion == "1":
                # Registrar nueva cita
                pacientes = PacienteController.listar_pacientes()
                medicos = MedicoController.listar_medicos()
                
                datos = CitaView.solicitar_datos_cita(pacientes, medicos)
                if datos:
                    exito, resultado = CitaController.crear_cita(
                        datos['id_paciente'], datos['id_medico'], 
                        datos['fecha_hora'], datos['motivo']
                    )
                    if exito:
                        MenuView.mostrar_mensaje(f"Cita registrada con éxito. ID: {resultado.id}")
                    else:
                        MenuView.mostrar_mensaje(resultado, error=True)
            
            elif opcion == "2":
                # Listar todas las citas
                citas = CitaController.listar_citas()
                CitaView.listar_citas(citas)
            
            elif opcion == "3":
                # Buscar cita por ID
                id_cita = CitaView.solicitar_id_cita()
                if id_cita is not None:
                    cita = CitaController.buscar_cita_por_id(id_cita)
                    CitaView.mostrar_cita(cita)
            
            elif opcion == "4":
                # Buscar citas por paciente
                id_paciente = PacienteView.solicitar_id_paciente()
                if id_paciente is not None:
                    citas = CitaController.buscar_citas_por_paciente(id_paciente)
                    CitaView.listar_citas(citas)
            
            elif opcion == "5":
                # Buscar citas por médico
                id_medico = MedicoView.solicitar_id_medico()
                if id_medico is not None:
                    citas = CitaController.buscar_citas_por_medico(id_medico)
                    CitaView.listar_citas(citas)
            
            elif opcion == "6":
                # Buscar citas por fecha
                MenuView.mostrar_titulo("BÚSQUEDA POR FECHA")
                print("Ingrese la fecha de inicio:")
                fecha_inicio = MenuView.obtener_fecha()
                
                print("\n¿Desea buscar citas en un rango de fechas? (s/n): ")
                if input().lower() in ('s', 'si', 'sí'):
                    print("\nIngrese la fecha final:")
                    fecha_fin = MenuView.obtener_fecha()
                else:
                    fecha_fin = None
                
                citas = CitaController.buscar_citas_por_fecha(fecha_inicio, fecha_fin)
                CitaView.listar_citas(citas)
            
            elif opcion == "7":
                # Actualizar datos de cita
                id_cita = CitaView.solicitar_id_cita()
                if id_cita is not None:
                    cita_actual = CitaController.buscar_cita_por_id(id_cita)
                    if cita_actual:
                        CitaView.mostrar_cita(cita_actual)
                        
                        pacientes = PacienteController.listar_pacientes()
                        medicos = MedicoController.listar_medicos()
                        datos = CitaView.solicitar_datos_cita(pacientes, medicos, editar=True)
                        
                        if datos:
                            # Usar valores existentes si no se proporcionan nuevos
                            id_paciente = datos['id_paciente'] if datos['id_paciente'] else cita_actual.id_paciente
                            id_medico = datos['id_medico'] if datos['id_medico'] else cita_actual.id_medico
                            fecha_hora = datos['fecha_hora'] if datos['fecha_hora'] else cita_actual.fecha_hora.strftime("%d-%m-%Y %H:%M")
                            motivo = datos['motivo'] if datos['motivo'] else cita_actual.motivo
                            
                            exito, mensaje = CitaController.actualizar_cita(
                                id_cita, id_paciente, id_medico, fecha_hora, motivo
                            )
                            
                            MenuView.mostrar_mensaje(mensaje, not exito)
            
            elif opcion == "8":
                # Eliminar cita
                id_cita = CitaView.solicitar_id_cita()
                if id_cita is not None:
                    cita = CitaController.buscar_cita_por_id(id_cita)
                    if cita:
                        CitaView.mostrar_cita(cita)
                        if MenuView.confirmar_accion("¿Está seguro de eliminar esta cita?"):
                            exito, mensaje = CitaController.eliminar_cita(id_cita)
                            MenuView.mostrar_mensaje(mensaje, not exito)
            
            elif opcion == "0":
                # Volver al menú principal
                break
            
            else:
                MenuView.mostrar_mensaje("Opción inválida", error=True)
    
    def salir(self):
        """Cerrar la aplicación y liberar recursos"""
        try:
            if hasattr(self, 'db'):
                self.db.close()
            
            MenuView.limpiar_pantalla()
            print("\n¡Gracias por usar el Sistema de Gestión de Clínica!")
            print("Desarrollado con el patrón MVC en Python\n")
        except Exception as e:
            print(f"Error al cerrar la aplicación: {e}")

if __name__ == "__main__":
    app = App()
    app.ejecutar()