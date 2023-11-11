from src.ejercicio5 import calcular_total_creditos

def test_calcular_total_creditos():
    asignaturas = {'Matematicas': 6, 'Fisica': 4, 'Quimica': 5}
    assert calcular_total_creditos(asignaturas) == 15