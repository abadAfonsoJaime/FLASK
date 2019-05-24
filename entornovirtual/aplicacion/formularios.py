# from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SubmitField
from wtforms.validators import Required
'''
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()
csrf.validate_csrf.secret_key=False

app = Flask(__name__)
csrf.init_app(app)
'''


class FormCalculadora(FlaskForm):
	num1 = IntegerField( "Número1", validators=[Required("Tienes que introducir el dato")] )
	num2 = IntegerField( "Número2", validators=[Required("Tienes que introducir el dato")] )
	operador = SelectField( 
		"Operador",
		choices = [
			("+", "Sumar"),
			("-", "Restar"),
			("*", "Multiplicar"),
			("/", "Dividir"),
		]
	) # Los choice values and labels se declaran como una lista de tuplas 
	submit = SubmitField('Submit!')