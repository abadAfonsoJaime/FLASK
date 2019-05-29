from flask import session
from aplicacion.app import app

def login_user(Usuario):
	session["id"] = Usuario.id
	session["username"] = Usuario.username
	session["admin"] = Usuario.admin

def logout_user():
	session.pop("id", None)
	session.pop("username", None)
	session.pop("admin", None)

def is_login():
	if "id" in session:
		return True
	else:
		return False

def is_admin():
	return session.get("admin", False)
	''' El método get() hará: Si existe la variable de session,
	 devuelve el valor de "admin" y si no, devuevle False '''

@app.context_processor
def login():
	if "id" in session:
		return {'is_login':True}
	else:
		return {'is_login':False}

@app.context_processor
def admin():
	return { 'is_admin':session.get("admin", False) }