#############
# Hernán Palumbo - @coriolisgp
# Ejercicio 7
# UNRN Andina - Introducción a la Ingeniería en Computación
##############

from tp4ej1 import IngresoIncorrecto


def division_lenta(dividendo, divisor):
    
    try:
        if dividendo >= divisor:
            resta = dividendo
            resultado = 0
            while resta >= divisor:
                resta = resta - divisor
                resultado += 1
            return (resultado, resta)
        else:
            raise IngresoIncorrecto('El dividendo no puede ser menor que el divisor')
    except TypeError as err:
        raise IngresoIncorrecto('El dividendo y/o el divisor no son numeros') from err

def prueba():
    try:
        print(division_lenta('a', 10))
    except Exception as err:
        print(err)

if __name__ == "__main__":
    prueba()