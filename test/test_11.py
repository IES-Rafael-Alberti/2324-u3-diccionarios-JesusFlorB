from src.ejercicio11 import informacion_directorio

def test_informacion_directorio():
    directorio = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
    
    clientes_diccionario = informacion_directorio(directorio)

    assert '01234567L' in clientes_diccionario
    assert '71476342J' in clientes_diccionario
    assert '63823376M' in clientes_diccionario
    assert '98376547F' in clientes_diccionario

    luis = clientes_diccionario['01234567L']
    assert luis['nombre'] == 'Luis González'
    assert luis['email'] == 'luisgonzalez@mail.com'
    assert luis['teléfono'] == '656343576'
    assert luis['descuento'] == '12.5'

    macarena = clientes_diccionario['71476342J']
    assert macarena['nombre'] == 'Macarena Ramírez'
    assert macarena['email'] == 'macarena@mail.com'
    assert macarena['teléfono'] == '692839321'
    assert macarena['descuento'] == '8'

    juanjose = clientes_diccionario['63823376M']
    assert juanjose['nombre'] == 'Juan José Martínez'
    assert juanjose['email'] == 'juanjo@mail.com'
    assert juanjose['teléfono'] == '664888233'
    assert juanjose['descuento'] == '5.2'

    carmen = clientes_diccionario['98376547F']
    assert carmen['nombre'] == 'Carmen Sánchez'
    assert carmen['email'] == 'carmen@mail.com'
    assert carmen['teléfono'] == '667677855'
    assert carmen['descuento'] == '15.7'
