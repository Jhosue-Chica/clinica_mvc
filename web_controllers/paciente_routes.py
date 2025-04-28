from flask import Blueprint, render_template, request, redirect, url_for, flash
from controllers.paciente_controller import PacienteController
from forms.paciente_forms import PacienteForm
from datetime import datetime

paciente_bp = Blueprint('pacientes', __name__)

@paciente_bp.route('/')
def listar_pacientes():
    """Vista para listar pacientes"""
    pacientes = PacienteController.listar_pacientes()
    return render_template('pacientes/listar.html', pacientes=pacientes)

@paciente_bp.route('/crear', methods=['GET', 'POST'])
def crear_paciente():
    """Vista para crear paciente"""
    form = PacienteForm()
    if form.validate_on_submit():
        exito, resultado = PacienteController.crear_paciente(
            form.nombre.data,
            form.apellido.data,
            form.cedula.data,
            form.fecha_nacimiento.data.strftime('%d-%m-%Y'),
            form.email.data
        )
        if exito:
            flash('Paciente registrado con éxito', 'success')
            return redirect(url_for('pacientes.listar_pacientes'))
        else:
            flash(f'Error: {resultado}', 'danger')
    return render_template('pacientes/crear.html', form=form)

@paciente_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_paciente(id):
    """Vista para editar paciente"""
    paciente = PacienteController.buscar_paciente_por_id(id)
    if not paciente:
        flash('Paciente no encontrado', 'danger')
        return redirect(url_for('pacientes.listar_pacientes'))
    
    form = PacienteForm()
    
    # Cuando es GET, cargar los datos actuales en el formulario
    if request.method == 'GET':
        form.nombre.data = paciente.nombre
        form.apellido.data = paciente.apellido
        form.cedula.data = paciente.cedula
        
        # Convertir la fecha a formato YYYY-MM-DD para el input type="date"
        if paciente.fecha_nacimiento:
            if isinstance(paciente.fecha_nacimiento, str):
                try:
                    # Intentar convertir desde formato DD-MM-YYYY
                    fecha_obj = datetime.strptime(paciente.fecha_nacimiento, '%d-%m-%Y')
                    form.fecha_nacimiento.data = fecha_obj.date()
                except ValueError:
                    try:
                        # Intentar convertir desde formato YYYY-MM-DD
                        fecha_obj = datetime.strptime(paciente.fecha_nacimiento, '%Y-%m-%d')
                        form.fecha_nacimiento.data = fecha_obj.date()
                    except ValueError:
                        flash('Formato de fecha no válido', 'danger')
            else:
                form.fecha_nacimiento.data = paciente.fecha_nacimiento
        
        form.email.data = paciente.email
    
    if form.validate_on_submit():
        exito, mensaje = PacienteController.actualizar_paciente(
            id,
            form.nombre.data,
            form.apellido.data,
            form.cedula.data,
            form.fecha_nacimiento.data.strftime('%d-%m-%Y'),
            form.email.data
        )
        if exito:
            flash('Paciente actualizado con éxito', 'success')
            return redirect(url_for('pacientes.listar_pacientes'))
        else:
            flash(f'Error: {mensaje}', 'danger')
    
    return render_template('pacientes/editar.html', form=form, paciente=paciente)

@paciente_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_paciente(id):
    """Vista para eliminar paciente"""
    exito, mensaje = PacienteController.eliminar_paciente(id)
    if exito:
        flash('Paciente eliminado con éxito', 'success')
    else:
        flash(f'Error: {mensaje}', 'danger')
    return redirect(url_for('pacientes.listar_pacientes'))

@paciente_bp.route('/ver/<int:id>')
def ver_paciente(id):
    """Vista para ver detalles de un paciente"""
    paciente = PacienteController.buscar_paciente_por_id(id)
    if not paciente:
        flash('Paciente no encontrado', 'danger')
        return redirect(url_for('pacientes.listar_pacientes'))
    return render_template('pacientes/ver.html', paciente=paciente)

@paciente_bp.route('/buscar', methods=['POST'])
def buscar_por_cedula():
    """Vista para buscar paciente por cédula"""
    cedula = request.form.get('cedula', '')
    if cedula:
        paciente = PacienteController.buscar_paciente_por_cedula(cedula)
        if paciente:
            return redirect(url_for('pacientes.ver_paciente', id=paciente.id))
        else:
            flash(f'No se encontró ningún paciente con cédula {cedula}', 'warning')
    else:
        flash('Debe ingresar un número de cédula', 'warning')
    
    return redirect(url_for('pacientes.listar_pacientes'))