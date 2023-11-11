"""Escribir un programa que cree un diccionario de traducción español-inglés. 
El usuario introducirá las palabras en español e inglés separadas por dos puntos, 
y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. 
Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. 
Si una palabra no está en el diccionario debe dejarla sin traducir."""

#Esta funcion crea un diccionario de traduccion español-ingles a partir de la entrada del usuario.
def crear_diccionario():
    print("Ingresa las palabras y sus traducciones en el formato palabra:traduccion.")
    print("Presiona Enter sin escribir nada para terminar.")

    diccionario = {}
    entrada = input("Ingrese una palabra y su traduccion (o presiona Enter para terminar): ")

    while entrada:
        try:
            palabra, traduccion = entrada.split(":")  #Dividimos la entrada en palabra y traduccion
            diccionario[palabra.strip()] = traduccion.strip()  #Agregamos al diccionario (eliminando espacios extras)
        except ValueError:
            print("Formato incorrecto. Debe ser palabra:traduccion")  #Si hay un error de formato, mostramos un mensaje

        entrada = input("Ingrese una palabra y su traduccion (o presiona Enter para terminar): ")

    return diccionario

#Esta funcion toma una frase en español y la traduce palabra por palabra usando el diccionario.
def traducir_frase(frase, diccionario):
    palabras = frase.split()  #Dividimos la frase en una lista de palabras
    traduccion = [diccionario.get(palabra, palabra) for palabra in palabras]  #Usamos el diccionario para traducir
    return " ".join(traduccion)  #Unimos las palabras traducidas en una frase

def main():
    diccionario = crear_diccionario()

    print("\nDiccionario creado:")
    for palabra, traduccion in diccionario.items():
        print(f"{palabra} : {traduccion}")  #Mostramos el diccionario creado

    frase_espanol = input("\nIngresa una frase en español para ser traducida: ")
    frase_traducida = traducir_frase(frase_espanol, diccionario)  #Traducimos la frase

    print("\nFrase traducida:")
    print(frase_traducida)  #Mostramos la frase traducida

if __name__ == "__main__":

    main()