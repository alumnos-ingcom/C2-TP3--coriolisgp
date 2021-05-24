#############
# Hernán Palumbo - @coriolisgp
# Ejercicio 8
# UNRN Andina - Introducción a la Ingeniería en Computación
##############

from tp4ej1 import IngresoIncorrecto
from tp4ej6 import maximo, minimo 


def ordenar_mayor_a_menor(uno, dos, tres):
    list = [uno, dos, tres]
    try:
        num_max = maximo(list)
        list.remove(num_max)
        num_min = minimo(list)
        list.remove(num_min)
        return (num_max, list[0], num_min)
    except Exception as err:
        raise err

def ordenar_menor_a_mayor(uno, dos, tres):
    list = [uno, dos, tres]
    try:
        num_max = maximo(list)
        list.remove(num_max)
        num_min = minimo(list)
        list.remove(num_min)
        return (num_min, list[0], num_max)
    except Exception as err:
        raise IngresoIncorrecto('Los valores ingresados no se pueden comparar porque no son numeros')

def prueba():
    try:
        print(ordenar_menor_a_mayor(-10, 100, 3))
        print(ordenar_mayor_a_menor(-10, 100, 3))
    except Exception as err:
        print(err)

if __name__ == "__main__":
    prueba()



