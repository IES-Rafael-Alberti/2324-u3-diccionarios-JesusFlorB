"""Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio 
y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, 
con el siguiente formato

Lista de la compra	
Artículo 1	Precio
Artículo 2	Precio
Artículo 3	Precio
…	…
Total	Coste"""


#Esta funcion permite al usuario agregar un articulo y su precio a la cesta de la compra.
#Retorna True si se agrega un articulo, o False si el usuario decide terminar la entrada de datos.
def agregar_articulo(cesta):
    articulo = input("Ingresa el nombre del articulo (o presiona Enter para terminar): ")

    if articulo:
        precio = float(input(f"Ingresa el precio de {articulo}: "))
        cesta[articulo] = precio
        return True

    return False

#Esta funcion imprime por pantalla la lista de la compra y el coste total.
def mostrar_lista_compra(cesta):
    print("Lista de la compra")
    total = 0

    for articulo, precio in cesta.items():
        print(f"{articulo}\t{precio}")
        total += precio

    print(f"Total\t{total}")

def main():
    cesta = {}
    continuar = True

    while continuar:
        continuar = agregar_articulo(cesta)

    mostrar_lista_compra(cesta)

if __name__ == "__main__":

    main()