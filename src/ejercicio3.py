"""Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, 
un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. 
Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
Fruta	Precio
Plátano	1.35
Manzana	0.80
Pera	0.85
Naranja	0.70"""

def obtener_precio_fruta(fruta, kilos):
    precios_frutas = {
        'Platano': 1.35,
        'Manzana': 0.80,
        'Pera': 0.85,
        'Naranja': 0.70
    }

    if fruta in precios_frutas:
        #Si la fruta esta en el diccionario, calculamos el precio total.
        precio_por_kilo = precios_frutas[fruta]
        precio_total = kilos * precio_por_kilo
        return precio_total
    else:
        #Si la fruta no esta en el diccionario, retornamos None.
        return None

def main():
    #Pedimos al usuario que ingrese una fruta y la cantidad en kilos.
    fruta = input("Selecciona una fruta (Platano, Manzana, Pera o Naranja): ")
    kilos = float(input("Ingresa la cantidad en kilos: "))

    #Obtenemos el precio llamando a la funcion obtener_precio_fruta.
    precio = obtener_precio_fruta(fruta, kilos)

    if precio is not None:
        #Si el precio no es None, mostramos el resultado.
        print(f"El precio de {kilos} kilos de {fruta} es: {precio} euros.")
    else:
        #Si el precio es None, la fruta no esta en la lista de precios.
        print(f"La fruta {fruta} no esta en la lista de precios.")


if __name__ == "__main__":

    #Llamamos a la funcion principal para ejecutar el programa.
    main()