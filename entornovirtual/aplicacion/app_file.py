from flask import Flask, render_template, redirect, url_for #, request
from flask_bootstrap import Bootstrap
from os import listdir
from aplicacion.uploadFile import UploadForm
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
Bootstrap(app)

@app.route('/')
def inicio():
	
	lista = []
	for file in listdir(app.root_path + "/static/media"):
		lista.append(file)

	return render_template( "inicio_fileupload.html", lista=lista )

@app.route( '/upload', methods=['get', 'post'] )
def upload():
	form = UploadForm() # carga request.form y request.file
	if form.validate_on_submit(): # Si el formulario es válido:
		f = form.photo.data # Creamos un objeto fichero a parir del formulario
		filename = secure_filename(f.filename) # Creamos un nombre de fichero que sea compatible con el sistema de archivo
		f.save(app.root_path + "/static/media/" + filename) # Y lo guardamos en el directorio adecuado
		return redirect( url_for('inicio') ) # Finalmente realizamos una redirección al inicio de la página
	return render_template('file_form.html', form=form)

@app.errorhandler(404)
def page_not_found(error):
	return render_template("error.html", error="Página no encontrada..."), 404