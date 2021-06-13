#############
# Hernán Palumbo - @coriolisgp
# Ejercicio 4
# UNRN Andina - Introducción a la Ingeniería en Computación
##############

def compara(numero, otro_numero):
    if numero < otro_numero:
        valor_comparacion = -1
    elif numero > otro_numero:
        valor_comparacion = 1
    else:
        valor_comparacion = 0
    return valor_comparacion

def prueba():
    try:
        numero = 10
        otro_numero = 1
        numero_uno = 2
        numero_dos = 2
        print('Este resultado deberia ser 1: ', compara( numero, otro_numero))
        print('Este resultado deberia ser -1: ', compara( otro_numero, numero))
        print('Este resultado deberia ser 0: ', compara(numero_uno, numero_dos))
    except TypeError as err:
        print(err)

if __name__ == "__main__":
    prueba()