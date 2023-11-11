from src.ejercicio4 import obtener_nombre_mes, formatear_fecha

def test_obtener_nombre_mes():
    assert obtener_nombre_mes(1) == 'enero'
    assert obtener_nombre_mes(2) == 'febrero'
    assert obtener_nombre_mes(12) == 'diciembre'

def test_formatear_fecha():
    assert formatear_fecha('15/01/2023') == '15 de enero de 2023'
    assert formatear_fecha('22/07/2022') == '22 de julio de 2022'
    assert formatear_fecha('20/12/1993') == '20 de diciembre de 1993'