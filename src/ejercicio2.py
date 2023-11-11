"""Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>."""

def obtener_informacion_usuario():
    #Creamos un diccionario vacio para almacenar la informacion del usuario.
    informacion_usuario = {}

    #Solicitamos al usuario que ingrese su informacion y la guardamos en el diccionario.
    informacion_usuario['nombre'] = input("Ingrese su nombre: ")
    informacion_usuario['edad'] = input("Ingrese su edad: ")
    informacion_usuario['direccion'] = input("Ingrese su direccion: ")
    informacion_usuario['telefono'] = input("Ingrese su numero de telefono: ")

    #Devolvemos el diccionario con la informacion del usuario.
    return informacion_usuario

if __name__ == "__main__":

    informacion = obtener_informacion_usuario()
    #Imprimimos un mensaje con la informacion ingresada.
    print(f"{informacion['nombre']} tiene {informacion['edad']} años, vive en {informacion['direccion']} y su numero de telefono es {informacion['telefono']}.")