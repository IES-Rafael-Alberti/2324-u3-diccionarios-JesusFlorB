from src.ejercicio9 import (añadir_factura, pagar_factura)

def test_añadir_factura():
    facturas = {}
    num_factura = "F001"
    coste = 100.0

    añadir_factura(facturas, num_factura, coste)

    assert num_factura in facturas
    assert facturas[num_factura] == coste


def test_pagar_factura():
    facturas = {"F001": 100.0, "F002": 200.0}
    cobrado = 0
    num_factura = "F001"

    cobrado = pagar_factura(facturas, cobrado, num_factura)

    assert cobrado == 100.0
    assert num_factura not in facturas