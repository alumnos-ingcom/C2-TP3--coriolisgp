#############
# Hernán Palumbo - @coriolisgp
# Ejercicio 8
# UNRN Andina - Introducción a la Ingeniería en Computación
##############

from tp4ej1 import IngresoIncorrecto, ingreso_entero
from tp4ej6 import maximo, minimo 


def ordenar_mayor_a_menor(uno, dos, tres):
    list = [uno, dos, tres]
    num_max = maximo(list)
    list.remove(num_max)
    num_min = minimo(list)
    list.remove(num_min)
    return (num_max, list[0], num_min)

def ordenar_menor_a_mayor(uno, dos, tres):
    list = [uno, dos, tres]
    num_max = maximo(list)
    list.remove(num_max)
    num_min = minimo(list)
    list.remove(num_min)
    return (num_min, list[0], num_max)

def prueba():
    try:
        numero_uno = ingreso_entero('Ingrese un numero: ')
        numero_dos = ingreso_entero('Ingrese un numero: ')
        numero_tres = ingreso_entero('Ingrese un numero: ')
        print(ordenar_menor_a_mayor(numero_uno, numero_dos, numero_tres))
        print(ordenar_mayor_a_menor(numero_uno, numero_dos, numero_tres))
    except IngresoIncorrecto as err:
        print(err)

if __name__ == "__main__":
    prueba()



