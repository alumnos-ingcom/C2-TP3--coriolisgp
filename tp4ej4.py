#############
# Hernán Palumbo - @coriolisgp
# Ejercicio 4
# UNRN Andina - Introducción a la Ingeniería en Computación
##############
class ErrorComparacion(Exception):
    pass

def compara(numero, otro_numero):
    try:
        if numero < otro_numero:
            valor_comparacion = -1
        elif numero > otro_numero:
            valor_comparacion = 1
        else:
            valor_comparacion = 0
        return valor_comparacion
    except Exception as err:
        raise ErrorComparacion('Los valores ingresados no se pueden comparar') from err

def prueba():
    try:
        numero = 6
        otro_numero = 1
        print(compara(numero, otro_numero))
    except ErrorComparacion as err:
        print(err)

if __name__ == "__main__":
    prueba()