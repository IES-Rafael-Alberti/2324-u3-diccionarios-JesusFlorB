"""Escribir un programa que gestione las facturas pendientes de cobro de una empresa. 
Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. 
El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. 
Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. 
Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. 
Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro."""

def añadir_factura(facturas, num_factura, coste):
    """
    Añade una nueva factura al diccionario de facturas.

    Args:
        facturas (dict): Diccionario que contiene las facturas.
        num_factura (str): Numero de la factura.
        coste (float): Coste de la factura.
    """
    facturas[num_factura] = coste  #Asigna el coste a la factura con el numero especificado

def pagar_factura(facturas, cobrado, num_factura):
    """
    Paga una factura existente y actualiza el monto cobrado.

    Args:
        facturas (dict): Diccionario que contiene las facturas.
        cobrado (float): Monto total cobrado hasta el momento.
        num_factura (str): Numero de la factura a pagar.

    Returns:
        float: Monto total cobrado despues de pagar la factura.
    """
    if num_factura in facturas:
        cobrado += facturas[num_factura]  #Aumenta el monto cobrado con el coste de la factura pagada
        del facturas[num_factura]  #Elimina la factura del diccionario
    return cobrado  #Devuelve el monto total cobrado actualizado

def mostrar_estado(cobrado, pendiente):
    """
    Muestra el estado de cobro actual.

    Args:
        cobrado (float): Monto total cobrado hasta el momento.
        pendiente (float): Monto total pendiente de cobro.
    """
    print(f"Cantidad cobrada hasta el momento: {cobrado}")  #Muestra el monto cobrado
    print(f"Cantidad pendiente de cobro: {pendiente}")  #Muestra el monto pendiente de cobro

if __name__ == '__main__':
    
    facturas = {}  #Diccionario para almacenar las facturas y sus costes
    cobrado = 0  #Variable para rastrear la cantidad total cobrada
    opcion = ''  #Variable para almacenar la opción del usuario

    while opcion != '3':
        print("\n¿Que desea hacer?")
        print("1. Añadir nueva factura")
        print("2. Pagar factura existente")
        print("3. Terminar")
        opcion = input("Ingrese el numero de la opcion: ")  #Solicita una opcion al usuario

        if opcion == '1':
            num_factura = input("Ingrese el numero de factura: ")
            coste = float(input("Ingrese el coste de la factura: "))
            añadir_factura(facturas, num_factura, coste)  #Llama a la funcion para añadir factura
            mostrar_estado(cobrado, sum(facturas.values()))  #Muestra el estado de cobro
        elif opcion == '2':
            num_factura = input("Ingrese el numero de factura a pagar: ")
            cobrado = pagar_factura(facturas, cobrado, num_factura)  #Llama a la funcion para pagar factura
            mostrar_estado(cobrado, sum(facturas.values()))  #Muestra el estado financiero actualizado
        elif opcion == '3':
            print("Saliendo del programa...")  #Mensaje de salida del programa
        else:
            print("Opcion no valida. Por favor, elija una opcion valida.")  #Mensaje de error para opciones no validas
