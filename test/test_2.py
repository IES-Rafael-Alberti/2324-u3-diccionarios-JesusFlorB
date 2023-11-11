from src.ejercicio2 import obtener_informacion_usuario
from io import StringIO

def test_obtener_informacion_usuario(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO('Jesus\n29\nCalle Palmar\n123456789\n'))

    resultado = obtener_informacion_usuario()

    assert resultado == {'nombre': 'Jesus', 'edad': '29', 'direccion': 'Calle Palmar', 'telefono': '123456789'}

def test_impresion():
    import sys
    from io import StringIO
    original_stdout = sys.stdout
    sys.stdout = StringIO()

    informacion = {'nombre': 'Jesus', 'edad': '29', 'direccion': 'Calle Palmar', 'telefono': '123456789'}
    print(f"{informacion['nombre']} tiene {informacion['edad']} años, vive en {informacion['direccion']} y su numero de telefono es {informacion['telefono']}.")

    resultado = sys.stdout.getvalue().strip()
    assert resultado == 'Jesus tiene 29 años, vive en Calle Palmar y su numero de telefono es 123456789.'
