from flask import Blueprint, render_template, request, redirect, url_for, flash
from controllers.medico_controller import MedicoController
from forms.medico_forms import MedicoForm

medico_bp = Blueprint('medicos', __name__)

@medico_bp.route('/')
def listar_medicos():
    """Vista para listar médicos"""
    medicos = MedicoController.listar_medicos()
    return render_template('medicos/listar.html', medicos=medicos)

@medico_bp.route('/crear', methods=['GET', 'POST'])
def crear_medico():
    """Vista para crear médico"""
    form = MedicoForm()
    if form.validate_on_submit():
        exito, resultado = MedicoController.crear_medico(
            form.nombre.data,
            form.especialidad.data,
            form.email.data
        )
        if exito:
            flash('Médico registrado con éxito', 'success')
            return redirect(url_for('medicos.listar_medicos'))
        else:
            flash(f'Error: {resultado}', 'danger')
    return render_template('medicos/crear.html', form=form)

@medico_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_medico(id):
    """Vista para editar médico"""
    medico = MedicoController.buscar_medico_por_id(id)
    if not medico:
        flash('Médico no encontrado', 'danger')
        return redirect(url_for('medicos.listar_medicos'))
    
    form = MedicoForm(obj=medico)
    if form.validate_on_submit():
        exito, mensaje = MedicoController.actualizar_medico(
            id,
            form.nombre.data,
            form.especialidad.data,
            form.email.data
        )
        if exito:
            flash('Médico actualizado con éxito', 'success')
            return redirect(url_for('medicos.listar_medicos'))
        else:
            flash(f'Error: {mensaje}', 'danger')
    return render_template('medicos/editar.html', form=form, medico=medico)

@medico_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_medico(id):
    """Vista para eliminar médico"""
    exito, mensaje = MedicoController.eliminar_medico(id)
    if exito:
        flash('Médico eliminado con éxito', 'success')
    else:
        flash(f'Error: {mensaje}', 'danger')
    return redirect(url_for('medicos.listar_medicos'))

@medico_bp.route('/ver/<int:id>')
def ver_medico(id):
    """Vista para ver detalles de un médico"""
    medico = MedicoController.buscar_medico_por_id(id)
    if not medico:
        flash('Médico no encontrado', 'danger')
        return redirect(url_for('medicos.listar_medicos'))
    return render_template('medicos/ver.html', medico=medico)

@medico_bp.route('/especialidad', methods=['GET', 'POST'])
def buscar_por_especialidad():
    """Vista para buscar médicos por especialidad"""
    especialidad = request.form.get('especialidad', '')
    
    if request.method == 'POST' and especialidad:
        medicos = MedicoController.buscar_medicos_por_especialidad(especialidad)
        return render_template('medicos/listar.html', 
                              medicos=medicos, 
                              busqueda=True, 
                              especialidad=especialidad)
    
    return redirect(url_for('medicos.listar_medicos'))