from jinja2 import Template
# Las instrucciones se indican con --> {%

# for
temp9 = '''
<ul>
{% for eleme in elems -%}
<li>{{ loop.index }} - {{ elem }}</li>
{% endfor -%}
'''
print( Template(temp9).render(elems=["amarillo", "rojo", "verde"]) )
# también existen variables 
	# --> loop.index[0] = indica la iteración actual pero empezando a contar dede cero
	# --> loop.first = devuelve True si estamos en la primera iteración
# if
temp10 = '''
{% if elems %}
<ul>
{% for elem in elems -%}
	{% if elem is divisibleby 2 -%}
		<li>{{ elem }} es par.</li>
	{% else -%}
		<li>{{ elem }} es impar.</li>
	{% endif -%}
{% endfor -%}
</ul>
{% endif %}
'''
print( Template(temp10).render(elems=[1,2,3,4,5,6]) )