# ------------------------------------------------
from wtforms import Form
from flask_wtf import FlaskForm

from wtforms import StringField, IntegerField
from wtforms import EmailField
# Aqui de los validadores importamos el dato obligatorio y el email
from wtforms import validators


class UserForm(Form):
  nombre = StringField('nombre', validators=[
    validators.DataRequired(message='El campo es requerido'),
    validators.length(min=4, max=10, message='Ingresa un nombre valido')
  ])
  apaterno = StringField('apaterno', validators=[
    validators.DataRequired(message='El campo es requerido'),
    validators.length(min=4, max=15, message='Ingresa un apellido valido')
  ])
  amaterno = StringField('amaterno', validators=[
    validators.DataRequired(message='El campo es requerido'),
    validators.length(min=4, max=15, message='Ingresa un apellido valido')
  ])
  email = EmailField('email', [ validators.Email(message='Ingrese un correo valido')])
  edad = IntegerField('edad', validators=[
    validators.DataRequired(message='El campo es requerido')
  ])
  
