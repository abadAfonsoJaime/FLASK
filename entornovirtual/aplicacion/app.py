from flask import Flask, render_template, redirect, url_for, request, abort # Constructor
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from aplicacion import config
from aplicacion.forms import *
from werkzeug.utils import secure_filename
import os

app = Flask(__name__) # Aplicación WSGI
app.config.from_object(config) # Cargamos las variables de configuración
Bootstrap(app)
db = SQLAlchemy(app) # Objeto db con el constructor SQLAlchemy que representa la database

from aplicacion.model import * # esta importación debe hacerse después del objeto db
from aplicacion.login import *


@app.route('/') # Decorador
@app.route('/categoria/<id>')
def init(id='0'):
	cat = Categorias.query.get(id)

	if id == '0':
		allArticulos = Articulos.query.all()
	else:
		allArticulos = Articulos.query.filter_by(CategoriaId=id)

	allCategorias = Categorias.query.all()
	return render_template("index.html", articulos=allArticulos, categorias=allCategorias, cat=cat) 


@app.route('/categorias')
def categorias():
	allCategorias = Categorias.query.all()
	return render_template("categorias.html", categorias=allCategorias)


@app.route('/categorias/new', methods=["get", "post"])
def categorias_new():
	if not is_admin():
		abort(404)

	form = FormCategoria(request.form)
	if form.validate_on_submit():
		cat = Categorias(nombre=form.nombre.data)
		db.session.add(cat)
		db.session.commit()
		return redirect( url_for("categorias") )
	else:
		return render_template("categorias_new.html", form=form)


@app.route('/categorias/<id>/edit', methods=["get", "post"])
def categorias_edit(id):
	if not is_admin():
		abort(404)

	cat = Categorias.query.get(id)
	if cat is None: # check if the url <id> parameter has been changed
		abort(404)

	form = FormCategoria(request.form, obj=cat)
	if form.validate_on_submit():
		form.populate_obj(cat)
		db.session.commit()
		return redirect( url_for("categorias") )

	return render_template("categorias_new.html", form=form)


@app.route('/categorias/<id>/delete', methods=["get", "post"])
def categorias_delete(id):
	if not is_admin():
		abort(404)

	cat = Categorias.query.get(id)
	if cat is None:
		abort(404)

	form = FormSiNo()
	if form.validate_on_submit():
		if form.si.data:
			db.session.delete(art)
			db.session.commit()

		return redirect( url_for("categorias") )

	return render_template("categorias_delete.html", form=form, cat=cat)


@app.route('/articulos/new', methods=["get", "post"])
def articulos_new():
	if not is_admin():
		abort(404)

	form = FormArticulo()

	# utilizamos un generador para rellenar los choices
	allCategorias = [ (c.id, c.nombre) for c in Categorias.query.all()[1:] ]
	# Recorremos las categorias y las guardamos en una lista de tuplas para inicializar el CategoriaId
	form.CategoriaId.choices = allCategorias

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


@app.route('/articulos/<id>/edit', methods=["get", "post"])
def articulos_edit(id):
	art = Articulos.query.get(id)
	if art is None: # check if the url <id> parameter has been changed
		abort(404)

	form = FormArticulo(obj=art) # objeto formulario con los valores del artículo seleccionado
	allCategorias = [ (c.id, c.nombre) for c in Categorias.query.all()[1:] ]
	form.CategoriaId.choices = allCategorias

	if form.validate_on_submit():
		# Borramos la imagen anterior si hemos subido una nueva
		if form.photo.data: # Si hemos subido una nueva imagen
			os.remove(app.root_path + "/static/media/" + art.image)
			try:
				f = form.photo.data
				nombre_fichero = secure_filename(f.filename)
				f.save(app.root_path + "/static/media/" + nombre_fichero)
			except:
				nombre_fichero = ""
		else:
			nombre_fichero = art.image

		# Rellenamos el formulario a partir de los datos del artículo
		form.populate_obj(art)
		art.image = nombre_fichero
		db.session.commit()
		return redirect( url_for("init") )

	return render_template("articulos_new.html", form=form)


@app.route('/articulos/<id>/delete', methods=["get", "post"])
def articulos_delete(id):
	art = Articulos.query.get(id)
	if art is None:
		abort(404)

	form = FormSiNo()
	if form.validate_on_submit():
		if form.si.data:
			if art.image != "":
				os.remove(app.root_path + "/static/media" + art.image)

			db.session.delete(art)
			db.session.commit()

		return redirect( url_for("init") )

	return render_template("articulos_delete.html", form=form, art=art)


@app.route('/login', methods=["get", "post"])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = Usuarios.query.filter_by( username=form.username.data ).first()
		if user != None and user.verify_password(form.password.data):
			login_user(user)
			return redirect( url_for('init') )

		form.username.errors.append("Usuario o contraseña incorrectas.")
	return render_template("login.html", form=form)


@app.route('/logout')
def logout():
	logout_user()
	return redirect( url_for('login') )


@app.route('/registro', methods=["get", "post"])
def registro():
	# control de registros
	if is_login():
		return redirect( url_for("init") )

	form = FormUsuario()
	if form.validate_on_submit():

		existe_usuario = Usuarios.query.filter_by(username=form.username.data).first()
		if existe_usuario == None:

			user = Usuarios()
			form.populate_obj(user)
			user.admin = False
			db.session.add(user)
			db.session.commit()
			return redirect( url_for("init") )

		form.username.errors.append("El nombre de usuario ya existe")

	return render_template("usuarios_new.html", form=form)


@app.route('/perfil/<username>', methods=["get", "post"])
def perfil(username):
	if not is_login:
		abort(404)

	user = Usuarios.query.filter_by(username=username).first()
	if user is None:
		abort(404)

	form = FormUsuario(request.form, obj=user)
	del form.password
	if form.validate_on_submit():
		form.populate_obj(user)
		db.session.commit()
		return redirect( url_for("init") )

	return render_template("usuarios_new.html", form=form, perfil=True)


@app.route('/changepassword/<username>', methods=["get", "post"])
def change_password(username):
	user = Usuarios.query.filter_by(username=username).first()
	if user is None:
		abort(404)

	form = FormChangePassword()
	if form.validate_on_submit():
		form.populate_obj(user)
		db.session.commit()
		return redirect( url_for("init") )

	return render_template("change_password.html", form=form)


@app.errorhandler(404)	
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
