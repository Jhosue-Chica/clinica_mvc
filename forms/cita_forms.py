from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField, DateField, DateTimeField, TimeField
from wtforms.validators import DataRequired, Optional, Length
from datetime import datetime

class CitaForm(FlaskForm):
    """Formulario para crear/editar citas"""
    id_paciente = SelectField('Paciente', coerce=int, validators=[
        DataRequired(message="Debe seleccionar un paciente")
    ])
    
    id_medico = SelectField('Médico', coerce=int, validators=[
        DataRequired(message="Debe seleccionar un médico")
    ])
    
    fecha = DateField('Fecha', 
                     format='%Y-%m-%d',
                     validators=[DataRequired(message="La fecha es obligatoria")])
    
    hora = TimeField('Hora',
                    format='%H:%M',
                    validators=[DataRequired(message="La hora es obligatoria")])
    
    motivo = TextAreaField('Motivo de la consulta', validators=[
        Optional(), 
        Length(max=255, message="El motivo no puede exceder los 255 caracteres")
    ])
    
    submit = SubmitField('Guardar')

class BusquedaFechaForm(FlaskForm):
    """Formulario para buscar citas por fecha"""
    fecha_inicio = DateField('Fecha de inicio', 
                           format='%Y-%m-%d',
                           validators=[DataRequired(message="La fecha de inicio es obligatoria")])
    
    fecha_fin = DateField('Fecha de fin (opcional)', 
                         format='%Y-%m-%d',
                         validators=[Optional()])
    
    submit = SubmitField('Buscar')