from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, Optional, Length

class MedicoForm(FlaskForm):
    """Formulario para crear/editar médicos"""
    nombre = StringField('Nombre Completo', validators=[
        DataRequired(message="El nombre es obligatorio"), 
        Length(max=100, message="El nombre no puede exceder los 100 caracteres")
    ])
    
    especialidad = StringField('Especialidad', validators=[
        DataRequired(message="La especialidad es obligatoria"), 
        Length(max=100, message="La especialidad no puede exceder los 100 caracteres")
    ])
    
    email = EmailField('Email', validators=[
        Optional(), 
        Email(message="El formato del email no es válido"), 
        Length(max=100, message="El email no puede exceder los 100 caracteres")
    ])
    
    submit = SubmitField('Guardar')

class BusquedaEspecialidadForm(FlaskForm):
    """Formulario para buscar médicos por especialidad"""
    especialidad = StringField('Especialidad', validators=[
        DataRequired(message="Ingrese la especialidad para buscar")
    ])
    
    submit = SubmitField('Buscar')