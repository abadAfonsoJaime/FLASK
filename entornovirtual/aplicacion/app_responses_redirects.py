from flask import Flask, make_response, abort, redirect, url_for
app = Flask(__name__)

''' Existen 3 formas posibles de generar las respuesta '''
@app.route('/string/')
def return_string():
	return 'Hello Matrix!'

''' Si queremos cambiar las cabeceras o el código de respuesta utilizamos la función make_response '''
@app.route('/object/')
def return_object():
	headers = {'Content-Type' : 'text/plain'}
	return make_response('Hello Matrix', 200, headers)

@app.route('/tuple/')
def return_tuple():
	return 'Hello, world', 200, {'Content-Type' : 'text/plain'}

@app.route('/login')
def login():
	abort(401) # Unauthorized

''' Para personalizar la respuesto utilizamos el decorador errorhandler '''
@app.errorhandler(404)
def page_not_found(error):
	return 'Página no puto encontrada...', 404

# Redirección
@app.route('/')
def index():
	return redirect( url_for('return_string') )