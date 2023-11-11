from src.ejercicio8 import crear_diccionario, traducir_frase
from unittest.mock import patch

def test_crear_diccionario():
    with patch('builtins.input', side_effect=['manzana:apple', 'sandia:watermelon', 'una:one', 'y:and', '']):
        diccionario = crear_diccionario()
        assert diccionario == {'manzana': 'apple', 'sandia': 'watermelon', 'una': 'one', 'y': 'and'}

def test_traducir_frase():
    diccionario = {'manzana': 'apple', 'sandia': 'watermelon', 'una': 'one', 'y': 'and'}
    frase_traducida = traducir_frase('una manzana y una sandia', diccionario)
    assert frase_traducida == 'one apple and one watermelon'