from src.ejercicio10 import agregar_cliente
from unittest.mock import patch

def test_agregar_cliente():
    base_datos = {}

    with patch('builtins.input', side_effect=['11223344A', 'Jesus Flor', 'Calle Palmar', '666999333', 'jesus@ejemplo.com', 'si']):
        agregar_cliente(base_datos)

    assert len(base_datos) == 1
    assert '11223344A' in base_datos