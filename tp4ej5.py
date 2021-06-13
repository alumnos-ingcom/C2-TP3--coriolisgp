#############
# Hernán Palumbo - @coriolisgp
# Ejercicio 5
# UNRN Andina - Introducción a la Ingeniería en Computación
##############
from tp4ej1 import IngresoIncorrecto, ingreso_entero

from tp4ej4 import compara
def signo(numero):
    numero = int(numero)
    valor_comparacion = compara(numero, 0)
    if valor_comparacion == 1:
        return 'positivo'
    elif valor_comparacion == 0:
        return 'cero'
    elif valor_comparacion == -1:
        return 'negativo'
        
def prueba():
    try:
        numero = ingreso_entero('Ingrese un numero: ')
        print(signo(numero))
    except IngresoIncorrecto as err:
        print(err)

if __name__ == "__main__":
    prueba()