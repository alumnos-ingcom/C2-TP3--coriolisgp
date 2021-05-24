#############
# Hernán Palumbo - @coriolisgp
# Ejercicio 9
# UNRN Andina - Introducción a la Ingeniería en Computación
##############

from tp4ej1 import IngresoIncorrecto

def es_primo(numero):
    try:
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
    except Exception as err:
        raise IngresoIncorrecto('El valor ingresado no es un número')
        
def prueba():
    try:
        print(es_primo(13))
    except Exception as err:
        print(err)

if __name__ == "__main__":
    prueba()



