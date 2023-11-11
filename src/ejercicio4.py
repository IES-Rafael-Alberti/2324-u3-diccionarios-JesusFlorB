"""Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> 
de aaaa donde <mes> es el nombre del mes."""

#Definimos una funcion para obtener el nombre del mes a partir de su numero.
def obtener_nombre_mes(mes):
    nombres_meses = {
        1: 'enero', 2: 'febrero', 3: 'marzo', 4: 'abril',
        5: 'mayo', 6: 'junio', 7: 'julio', 8: 'agosto',
        9: 'septiembre', 10: 'octubre', 11: 'noviembre', 12: 'diciembre'
    }
    return nombres_meses[mes]

#Definimos una funcion que toma una fecha en formato dd/mm/aaaa y la convierte al nuevo formato.
def formatear_fecha(fecha_original):
    #Dividimos la fecha en dia, mes y año, y convertimos a enteros.
    dia, mes, año = map(int, fecha_original.split('/'))
    
    #Obtenemos el nombre del mes llamando a la funcion anterior.
    nombre_mes = obtener_nombre_mes(mes)
    
    #Componemos la nueva fecha en el formato deseado.
    nueva_fecha = f"{dia} de {nombre_mes} de {año}"
    return nueva_fecha

#Funcion principal que solicita una fecha al usuario y la muestra en el nuevo formato.
def main():
    #Pedimos al usuario que ingrese una fecha en formato dd/mm/aaaa.
    fecha_original = input("Ingresa una fecha en formato dd/mm/aaaa: ")
    
    #Llamamos a la funcion formatear_fecha para obtener la nueva fecha.
    nueva_fecha = formatear_fecha(fecha_original)
    
    #Imprimimos la nueva fecha.
    print(nueva_fecha)


if __name__ == "__main__":
    
    #Llamamos a la funcion main para iniciar el programa.
    main()