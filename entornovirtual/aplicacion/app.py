from flask import Flask, render_template, redirect, url_for, request # Constructor
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from aplicacion import config
from aplicacion.forms import FormCategoria, FormArticulo
from werkzeug.utils import secure_filename

app = Flask(__name__) # Aplicación WSGI
app.config.from_object(config) # Cargamos las variables de configuración
Bootstrap(app)
db = SQLAlchemy(app) # Objeto db con el constructor SQLAlchemy que representa la database

from aplicacion.model import Articulos, Categorias # esta importación debe hacerse después del objeto db


@app.route('/') # Decorador
@app.route('/categoria/<id>')
def init(id='0'):
	cat = Categorias.query.get(id)

	if id == '0':
		articulos = Articulos.query.all()
	else:
		articulos = Articulos.query.filter_by(CategoriaId=id)

	allCategorias = Categorias.query.all()
	return render_template("index.html", articulos=articulos, categorias=allCategorias, cat=cat) 


@app.route('/categorias')
def categorias():
	allCategorias = Categorias.query.all()
	return render_template("categorias.html", categorias=allCategorias)


@app.route('/categorias/new', methods=["get", "post"])
def categorias_new():
	form = FormCategoria(request.form)
	if form.validate_on_submit():
		cat = Categorias(nombre=form.nombre.data)
		db.session.add(cat)
		db.session.commit()
		return redirect( url_for("categorias") )
	else:
		return render_template("categorias_new.html", form=form)


@app.route('/articulos/new', methods=["get", "post"])
def articulos_new():
	form = FormArticulo()

	# utilizamos un generador para rellenar los choices
	categorias = [ (c.id, c.nombre) for c in Categorias.query.all()[1:] ]
	# Recorremos las categorias y las guardamos en una lista de tuplas para inicializar el CategoriaId
	form.CategoriaId.choices = categorias

	if form.validate_on_submit():
		try:
			f = form.photo.data
			nombre_fichero = secure_filename(f.filename)
			f.save( app.root_path + "/static/media/" + nombre_fichero )
		except:
			nombre_fichero = ""
		art = Articulos()
		# cogemos los valores del formulario y rellenamos el objeto art
		form.populate_obj(art)
		art.image = nombre_fichero
		db.session.add(art)
		db.session.commit()
		return redirect( url_for("init") )
	else:
		return render_template("articulos_new.html", form=form)

		
def page_not_found(error):
	return render_template("notFound.html", error="Página no puto encontrada..."), 404


'''
Si no se gestiona desde el manage.py

from flask import Flask # Constructor
app = Flask(__name__) # Aplicación WSGI

@app.route('/') # Decorador
def hello_world():
	return 'Hello Matrix!' 

if __name__ == '__main__':
	app.run('0.0.0.0', 8080, debug=True)
'''
