"""Escribir un programa que cree un diccionario vacío y lo vaya llenando 
con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. 
Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario."""

#Definimos una funcion llamada agregar_informacion que recibe un diccionario, una clave y un valor, y agrega esa informacion al diccionario.
def agregar_informacion(diccionario, clave, valor):
    diccionario[clave] = valor  # Asignamos el valor a la clave en el diccionario
    print(diccionario)  #Imprimimos el diccionario actualizado

#Definimos una funcion llamada ingresar_informacion que permite al usuario ingresar informacion,
def ingresar_informacion():
    informacion_persona = {}  #Creamos un diccionario vacio para almacenar la informacion
    continuar = True  # Variable para controlar el bucle

    while continuar:
        clave = input("Ingresa el tipo de informacion (o presiona Enter para terminar): ")

        if clave:
            valor = input(f"Ingresa el valor de {clave}: ")
            agregar_informacion(informacion_persona, clave, valor)
        else:
            continuar = False  #Si el usuario presiona Enter, salimos del bucle

    return informacion_persona  #Devolvemos el diccionario con la informacion

if __name__ == "__main__":

    ingresar_informacion()