from flask_wtf import FlaskForm
from wtforms import StringField, DateField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, Optional, Length, Regexp

class PacienteForm(FlaskForm):
    """Formulario para crear/editar pacientes"""
    nombre = StringField('Nombre', validators=[
        DataRequired(message="El nombre es obligatorio"), 
        Length(max=100, message="El nombre no puede exceder los 100 caracteres")
    ])
    
    apellido = StringField('Apellido', validators=[
        DataRequired(message="El apellido es obligatorio"), 
        Length(max=100, message="El apellido no puede exceder los 100 caracteres")
    ])
    
    cedula = StringField('Cédula', validators=[
        DataRequired(message="La cédula es obligatoria"), 
        Length(max=20, message="La cédula no puede exceder los 20 caracteres"),
        Regexp(r'^\d+$', message="La cédula debe contener solo números")
    ])
    
    fecha_nacimiento = DateField('Fecha de Nacimiento', 
                                format='%Y-%m-%d',
                                validators=[DataRequired(message="La fecha de nacimiento es obligatoria")])
    
    email = EmailField('Email', validators=[
        Optional(), 
        Email(message="El formato del email no es válido"), 
        Length(max=100, message="El email no puede exceder los 100 caracteres")
    ])
    
    submit = SubmitField('Guardar')

class BusquedaCedulaForm(FlaskForm):
    """Formulario para buscar pacientes por cédula"""
    cedula = StringField('Cédula', validators=[
        DataRequired(message="Ingrese la cédula para buscar"),
        Regexp(r'^\d+$', message="La cédula debe contener solo números")
    ])
    
    submit = SubmitField('Buscar')