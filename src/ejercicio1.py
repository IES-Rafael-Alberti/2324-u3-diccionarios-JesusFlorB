"""Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario."""

#Definimos una funcion que toma una divisa como argumento.
def obtener_simbolo_divisa(divisa):
    #Definimos un diccionario con las divisas y simbolos.
    diccionario_divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    
    #Verificamos si la divisa esta en el diccionario.
    if divisa in diccionario_divisas:
        #Si esta en el diccionario, nos devuelve el simbolo correspondiente.
        simbolo = diccionario_divisas[divisa]
        return f"El simbolo de {divisa} es {simbolo}"
    else:
        #Si la divisa no esta en el diccionario, devolvemos aviso.
        return "La divisa ingresada no esta en el diccionario."


if __name__ == "__main__":

    divisa_usuario = input("Ingresa una divisa (Euro, Dollar o Yen): ")
    #Llamamos a la funcion obtener_simbolo_divisa con la divisa ingresada y almacenamos el resultado.
    resultado = obtener_simbolo_divisa(divisa_usuario)
    #Imprimimos el resultado en la pantalla.
    print(resultado)