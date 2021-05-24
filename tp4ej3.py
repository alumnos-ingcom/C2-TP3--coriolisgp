#############
# Hernán Palumbo - @coriolisgp
# Ejercicio 3
# UNRN Andina - Introducción a la Ingeniería en Computación
##############
from tp4ej1 import IngresoIncorrecto

def convertir_a_fahrenheit(centigrados):
    try: 
        fahrenheit = centigrados * (9/5) + 32
        return fahrenheit
    except Exception as err:
        raise IngresoIncorrecto('No era un numero, no se puede convertir')

def convertir_a_centigrados(fahrenheit):
    try:
        celsius = (fahrenheit - 32) * (5/9)
        return celsius
    except Exception as err:
        raise IngresoIncorrecto('No era un numero, no se puede convertir')


def prueba():
    valor_a_convertir = 'a'
    try:
        fahrenheit = convertir_a_fahrenheit(valor_a_convertir)
        print(fahrenheit)
        celsius = convertir_a_centigrados(fahrenheit)
        print(celsius)
    except IngresoIncorrecto as err:
        print(err)

if __name__ == "__main__":
    prueba()