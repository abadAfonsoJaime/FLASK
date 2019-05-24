from flask_script import Manager
# from aplicacion.app_jinja_logic import app
# from aplicacion.app_html import app
# from aplicacion.app_inherit_html import app
from aplicacion.app_bootstrap import app

manager = Manager(app) # Creamos un objeto Manager pásandole la app al constructor
app.config['DEBUG'] = True # Ensure debugger will load

if __name__ == '__main__':
	manager.run()