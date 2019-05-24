
from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField, FileRequired

class UploadForm(FlaskForm):
	"""docstring for UploadForm"""
	photo = FileField( 'selecciona imagen:', validators=[FileRequired()] )
	submit = SubmitField('Submit')
