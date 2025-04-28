from flask import Blueprint, render_template, request, redirect, url_for, flash
from controllers.cita_controller import CitaController
from controllers.paciente_controller import PacienteController
from controllers.medico_controller import MedicoController
from forms.cita_forms import CitaForm, BusquedaFechaForm
from datetime import datetime

cita_bp = Blueprint('citas', __name__)

@cita_bp.route('/')
def listar_citas():
    """Vista para listar citas"""
    citas = CitaController.listar_citas()
    return render_template('citas/listar.html', citas=citas)

@cita_bp.route('/crear', methods=['GET', 'POST'])
def crear_cita():
    """Vista para crear cita"""
    # Obtener listas de pacientes y médicos para los selectores
    pacientes = PacienteController.listar_pacientes()
    medicos = MedicoController.listar_medicos()
    
    if not pacientes:
        flash('No hay pacientes registrados. Registre un paciente primero.', 'warning')
        return redirect(url_for('pacientes.crear_paciente'))
        
    if not medicos:
        flash('No hay médicos registrados. Registre un médico primero.', 'warning')
        return redirect(url_for('medicos.crear_medico'))
    
    form = CitaForm()
    # Configurar opciones para los selectores
    form.id_paciente.choices = [(p.id, f"{p.nombre} {p.apellido} (Cédula: {p.cedula})") for p in pacientes]
    form.id_medico.choices = [(m.id, f"{m.nombre} - {m.especialidad}") for m in medicos]
    
    if form.validate_on_submit():
        # Combinar fecha y hora en un solo string
        fecha_hora_str = f"{form.fecha.data.strftime('%d-%m-%Y')} {form.hora.data.strftime('%H:%M')}"
        
        exito, resultado = CitaController.crear_cita(
            form.id_paciente.data,
            form.id_medico.data,
            fecha_hora_str,
            form.motivo.data
        )
        
        if exito:
            flash('Cita registrada con éxito', 'success')
            return redirect(url_for('citas.listar_citas'))
        else:
            flash(f'Error: {resultado}', 'danger')
    
    return render_template('citas/crear.html', form=form)

@cita_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_cita(id):
    """Vista para editar cita"""
    cita = CitaController.buscar_cita_por_id(id)
    if not cita:
        flash('Cita no encontrada', 'danger')
        return redirect(url_for('citas.listar_citas'))
    
    # Obtener listas de pacientes y médicos para los selectores
    pacientes = PacienteController.listar_pacientes()
    medicos = MedicoController.listar_medicos()
    
    form = CitaForm()
    # Configurar opciones para los selectores
    form.id_paciente.choices = [(p.id, f"{p.nombre} {p.apellido} (Cédula: {p.cedula})") for p in pacientes]
    form.id_medico.choices = [(m.id, f"{m.nombre} - {m.especialidad}") for m in medicos]
    
    if request.method == 'GET':
        # Llenar el formulario con los datos actuales
        form.id_paciente.data = cita.id_paciente
        form.id_medico.data = cita.id_medico
        if cita.fecha_hora:
            form.fecha.data = cita.fecha_hora.date()
            form.hora.data = cita.fecha_hora.time()
        form.motivo.data = cita.motivo
    
    if form.validate_on_submit():
        # Combinar fecha y hora en un solo string
        fecha_hora_str = f"{form.fecha.data.strftime('%d-%m-%Y')} {form.hora.data.strftime('%H:%M')}"
        
        exito, mensaje = CitaController.actualizar_cita(
            id,
            form.id_paciente.data,
            form.id_medico.data,
            fecha_hora_str,
            form.motivo.data
        )
        
        if exito:
            flash('Cita actualizada con éxito', 'success')
            return redirect(url_for('citas.listar_citas'))
        else:
            flash(f'Error: {mensaje}', 'danger')
    
    return render_template('citas/editar.html', form=form, cita=cita)

@cita_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_cita(id):
    """Vista para eliminar cita"""
    exito, mensaje = CitaController.eliminar_cita(id)
    if exito:
        flash('Cita eliminada con éxito', 'success')
    else:
        flash(f'Error: {mensaje}', 'danger')
    return redirect(url_for('citas.listar_citas'))

@cita_bp.route('/ver/<int:id>')
def ver_cita(id):
    """Vista para ver detalles de una cita"""
    cita = CitaController.buscar_cita_por_id(id)
    if not cita:
        flash('Cita no encontrada', 'danger')
        return redirect(url_for('citas.listar_citas'))
    return render_template('citas/ver.html', cita=cita)

@cita_bp.route('/paciente/<int:id_paciente>')
def citas_por_paciente(id_paciente):
    """Vista para listar citas de un paciente específico"""
    paciente = PacienteController.buscar_paciente_por_id(id_paciente)
    if not paciente:
        flash('Paciente no encontrado', 'danger')
        return redirect(url_for('pacientes.listar_pacientes'))
    
    citas = CitaController.buscar_citas_por_paciente(id_paciente)
    return render_template('citas/por_paciente.html', citas=citas, paciente=paciente)

@cita_bp.route('/medico/<int:id_medico>')
def citas_por_medico(id_medico):
    """Vista para listar citas de un médico específico"""
    medico = MedicoController.buscar_medico_por_id(id_medico)
    if not medico:
        flash('Médico no encontrado', 'danger')
        return redirect(url_for('medicos.listar_medicos'))
    
    citas = CitaController.buscar_citas_por_medico(id_medico)
    return render_template('citas/por_medico.html', citas=citas, medico=medico)

@cita_bp.route('/fecha', methods=['GET', 'POST'])
def citas_por_fecha():
    """Vista para buscar citas por fecha"""
    form = BusquedaFechaForm()
    
    if form.validate_on_submit():
        fecha_inicio = form.fecha_inicio.data.strftime('%d-%m-%Y')
        
        if form.fecha_fin.data:
            fecha_fin = form.fecha_fin.data.strftime('%d-%m-%Y')
        else:
            fecha_fin = None
        
        citas = CitaController.buscar_citas_por_fecha(fecha_inicio, fecha_fin)
        return render_template('citas/por_fecha.html', 
                               citas=citas, 
                               form=form, 
                               fecha_inicio=fecha_inicio, 
                               fecha_fin=fecha_fin)
    
    return render_template('citas/buscar_fecha.html', form=form)