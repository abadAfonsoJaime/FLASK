from flask import Flask # el constructor Flask permite crear una aplicación Flask
app = Flask(__name__) # la variable app es una aplicación wsgi

# Con esto ya podemos subir una aplicación web a cualquier servido compatible con wsgi

@app.route('/') # decorador para definir la ruta a la que accedemos
def hello_world(): # la función se ejecuta cuando accedemos a la página principal '/'
	return 'Hello Matrix!' # la función devuelve un string 
# todo el bloque, lo que realmente hace es devolver una respuesta http con su body y cabeceras 


if __name__ == '__main__': # Si ejecutamos el programa con Python 3
	app.run('0.0.0.0', 8080, debug=True)
	# La función run crea un servidor de desarrollo escuchando por cualquier dirección IP, en el puerto 8080
	# Significa que se puede acceder desde localhost o acceder a nuestra máquina desde un servidor externo

# (Press CTRL+C to quit)


'''
El decorador router nos permite filtrar la petición HTTP recibida, 
de tal forma que si la petición se realiza a la URL / se ejecutará la función

En adelante, el app.run() lo ejecutaremos con el manage
'''