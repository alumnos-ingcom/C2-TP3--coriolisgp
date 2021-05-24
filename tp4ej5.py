#############
# Hernán Palumbo - @coriolisgp
# Ejercicio 5
# UNRN Andina - Introducción a la Ingeniería en Computación
##############
from tp4ej4 import ErrorComparacion, compara
def signo(numero):
    try:
        numero = int(numero)
        valor_comparacion = compara(numero, 0)
        if valor_comparacion == 1:
            print('positivo')
        elif valor_comparacion == 0:
            print('cero')
        elif valor_comparacion == -1:
            print('negativo')
    except Exception as err:
        raise ErrorComparacion('Valores no validos') from err
        
def prueba():
    try:
        numero = 'a'
        signo(numero)
    except ErrorComparacion as err:
        print(err)

if __name__ == "__main__":
    prueba()