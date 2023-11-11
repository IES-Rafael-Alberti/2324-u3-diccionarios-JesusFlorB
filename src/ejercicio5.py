"""Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} 
y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, 
donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. 
Al final debe mostrar también el número total de créditos del curso."""

#Definimos una funcion que recibe un diccionario de asignaturas y sus creditos y muestra los creditos de cada asignatura.
def mostrar_creditos(asignaturas):
    for asignatura, creditos in asignaturas.items():
        print(f"{asignatura} tiene {creditos} creditos")

#Definimos una funcion que recibe un diccionario de asignaturas y sus creditos y retorna el numero total de créditos.
def calcular_total_creditos(asignaturas):
    total_creditos = sum(asignaturas.values())
    return total_creditos

def main():
    #Definimos el diccionario con los creditos de las asignaturas
    creditos_asignaturas = {'Matematicas': 6, 'Fisica': 4, 'Quimica': 5}

    #Mostramos los creditos de cada asignatura
    mostrar_creditos(creditos_asignaturas)

    #Calculamos y mostramos el numero total de creditos
    total_creditos = calcular_total_creditos(creditos_asignaturas)
    print(f"El total de creditos del curso es: {total_creditos}")

if __name__ == "__main__":

    main()