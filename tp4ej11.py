#############
# Hernán Palumbo - @coriolisgp
# Ejercicio 11
# UNRN Andina - Introducción a la Ingeniería en Computación
##############
from tp4ej1 import IngresoIncorrecto

def es_palindromo(texto):
    try:
        texto = str(texto)
        es_palindromo = False
        texto = texto.upper()
        texto_dadovuelta = texto[::-1]
        if texto == texto_dadovuelta:
            es_palindromo = True
        return es_palindromo
    except Exception as err:
        raise IngresoIncorrecto('El valor ingresado no es un texto, o no se puede convertir a texto')
        
def prueba():
    try:
        print(es_palindromo('menem'))
    except Exception as err:
        print(err)

if __name__ == "__main__":
    prueba()