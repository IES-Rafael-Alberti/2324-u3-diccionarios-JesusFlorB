from src.ejercicio1 import obtener_simbolo_divisa

def test_obtener_simbolo_divisa():
    assert obtener_simbolo_divisa('Euro') == "El simbolo de Euro es €"
    assert obtener_simbolo_divisa('Dollar') == "El simbolo de Dollar es $"
    assert obtener_simbolo_divisa('Yen') == "El simbolo de Yen es ¥"
    assert obtener_simbolo_divisa('Libra') == "La divisa ingresada no esta en el diccionario."