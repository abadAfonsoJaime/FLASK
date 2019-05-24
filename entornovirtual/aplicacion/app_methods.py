from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def inicio():
	return 'Pagina principal'

@app.route('/articulos')
def articulos():
	return 'Lista de artículos'

@app.route('/artículos/new', methods=["POST"])
def articulos_new():
	return 'Esta URL recibe información de un formulario con el métodod POST'

@app.route('/login', methods=["GET", "POST"])
def login():
	if request.method == "POST": # curl http://localhost:5000/login
		return 'Hemos accedido con POST'
	else: 				# curl -X POST http://localhost:5000/login
		return 'Hemos accedido con GET'
