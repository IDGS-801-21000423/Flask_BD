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
  
class UserForm2(Form):
  id = IntegerField('id', [validators.number_range(min=1, max=20, message='Valor no valido')])
  nombre = StringField('nombre', validators=[
    validators.DataRequired(message='El nombre es requerido'),
    validators.length(min=4, max=20, message='Requiere min=4, max=10')
  ])
  apaterno = StringField('apaterno', validators=[
    validators.DataRequired(message='El apellido es requerido')
  ])
  email = EmailField('correo', validators=[ 
    validators.Email(message='El email es requerido')
  ])
  