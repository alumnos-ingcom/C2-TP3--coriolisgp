#############
# Hernán Palumbo - @coriolisgp
# Ejercicio 7
# UNRN Andina - Introducción a la Ingeniería en Computación
##############

from tp4ej1 import IngresoIncorrecto


def division_lenta(dividendo, divisor):
    if divisor != 0:
        if dividendo >= divisor:
            resta = dividendo
            resultado = 0
            while resta >= divisor:
                resta = resta - divisor
                resultado += 1
            return (resultado, resta)
        else:
            raise IngresoIncorrecto('El dividendo no puede ser menor que el divisor')
    else:
        raise IngresoIncorrecto('El divisor no puede ser cero!')

def prueba():
    try:
        print(division_lenta(20, 2))
    except IngresoIncorrecto as err:
        print(err)

if __name__ == "__main__":
    prueba()