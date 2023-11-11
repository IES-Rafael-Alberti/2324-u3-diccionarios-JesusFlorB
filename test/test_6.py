from src.ejercicio6 import agregar_informacion, ingresar_informacion

def test_agregar_informacion():
    diccionario = {}
    agregar_informacion(diccionario, 'Nombre', 'Maria')
    agregar_informacion(diccionario, 'Edad', '43')
    assert diccionario == {'Nombre': 'Maria', 'Edad': '43'}