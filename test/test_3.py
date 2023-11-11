from src.ejercicio3 import obtener_precio_fruta

def test_obtener_precio_fruta():
    assert obtener_precio_fruta('Platano', 2) == 2.70
    assert obtener_precio_fruta('Manzana', 1) == 0.8
    assert obtener_precio_fruta('Pera', 3) == 2.55
    assert obtener_precio_fruta('Naranja', 2) == 1.40
    assert obtener_precio_fruta('Sandia', 2) is None