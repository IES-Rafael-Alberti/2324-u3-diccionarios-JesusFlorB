from src.ejercicio7 import agregar_articulo, mostrar_lista_compra
from unittest.mock import patch

def test_agregar_articulo():
    cesta = {}
    with patch('builtins.input', side_effect=['Manzana', '1.50', '']):
        assert agregar_articulo(cesta) == True
    assert cesta == {'Manzana': 1.50}

def test_mostrar_lista_compra(capsys):
    cesta = {'Manzana': 1.50, 'Platano': 0.75}
    mostrar_lista_compra(cesta)
    captured = capsys.readouterr()
    assert captured.out == "Lista de la compra\nManzana\t1.5\nPlatano\t0.75\nTotal\t2.25\n"

def test_agregar_articulo_terminar():
    cesta = {}
    with patch('builtins.input', return_value=''):
        assert agregar_articulo(cesta) == False
    assert cesta == {}