from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, IntegerField, TextAreaField, SelectField, PasswordField
from wtforms.fields.html5 import EmailField
from flask_wtf.file import FileField
from wtforms.validators import Required
# En este fichero se definen los modelos correspondientes a cada formulario 

class FormCategoria(FlaskForm):
	nombre = StringField( "Nombre:", validators=[Required("Tienes que introducir el dato")] )
	submit = SubmitField( "Enviar" )
		

class FormArticulo(FlaskForm):
	nombre 		= StringField( "Nombre:", validators=[Required("Tienes que introducir el dato")] )
	precio 		= DecimalField( "Precio:", default=0, validators=[Required("Campo obligatorio")] )
	IVA 		= IntegerField( "IVA:", default=21, validators=[Required("Campo obligatorio")] )
	descripcion = TextAreaField("Descripción:")
	photo 		= FileField("Selecciona imagen:")
	stock 		= IntegerField( "Stock:", default=1, validators=[Required("Campo obligatorio")] )
	CategoriaId = SelectField( "Categoría:", coerce=int ) # coerce indica el tipo de dato que va a devolver
	submit 		= SubmitField("Enviar")


class FormSiNo(FlaskForm):
	si = SubmitField('Si')
	no = SubmitField('No')


class LoginForm(FlaskForm):
	username 	= StringField( "Login", validators=[Required()] )
	password 	= PasswordField("Password", validators=[Required()])
	submit 		= SubmitField("Entrar")


class FormUsuario(FlaskForm):
	username 	= StringField( "Login", validators=[Required()] ) # usuario
	password 	= PasswordField( "Password", validators=[Required()] ) # usuario
	nombre 		= StringField( "Nombre Completo" ) # Usuario
	email 		= EmailField( "Email" ) # usuario@usuario.es
	submit 		= SubmitField( "Aceptar" )


class FormChangePassword(FlaskForm):
	password 	= PasswordField( "Password", validators=[Required()] )
	submit 		= SubmitField( "Aceptar" )		