#############
# Hernán Palumbo - @coriolisgp
# Ejercicio 9
# UNRN Andina - Introducción a la Ingeniería en Computación
##############

from tp4ej1 import IngresoIncorrecto, ingreso_entero

def es_primo(numero):
    divisor = abs(numero//2)
    es_primo = True
    resto = 1
    while divisor > 1 and resto != 0:
        resto = numero % divisor
        if resto == 0:
            es_primo = False
            break
        divisor -= 1
    return es_primo
        
def prueba():
    try:
        numero = ingreso_entero('Ingrese un numero para verificar si es primo: ')
        print(es_primo(13))
    except IngresoIncorrecto as err:
        print(err)

if __name__ == "__main__":
    prueba()



