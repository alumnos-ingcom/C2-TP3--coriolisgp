#############
# Hernán Palumbo - @coriolisgp
# Ejercicio 3
# UNRN Andina - Introducción a la Ingeniería en Computación
##############
from tp4ej1 import IngresoIncorrecto

def convertir_a_fahrenheit(centigrados):
    fahrenheit = centigrados * (9/5) + 32
    return fahrenheit

def convertir_a_centigrados(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    return celsius


def prueba():
    valor_a_convertir = 30
    fahrenheit = convertir_a_fahrenheit(valor_a_convertir)
    print(fahrenheit)
    celsius = convertir_a_centigrados(fahrenheit)
    print(celsius)
        

if __name__ == "__main__":
    prueba()