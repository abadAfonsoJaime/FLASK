import os

SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
PWD = os.path.abspath(os.curdir) # dónde guardamos la ruta en que se esta ejecutando la especificación

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/dbase.db'.format(PWD) # cadena de conexión de base de datos
SQLALCHEMY_TRACK_MODIFICATIONS = False # SQLAlchemy Flag