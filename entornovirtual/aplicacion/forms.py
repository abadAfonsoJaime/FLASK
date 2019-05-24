from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, IntegerField, TextAreaField, SelectField
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
