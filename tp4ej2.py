#############
# Hernán Palumbo - @coriolisgp
# Ejercicio 2
# UNRN Andina - Introducción a la Ingeniería en Computación
##############

from tp4ej1 import ingreso_entero_reintento

def suma_lenta(primer_numero, segundo_numero):
    suma = primer_numero
    if segundo_numero >= 0:
        while segundo_numero > 0:
            suma += 1
            segundo_numero -= 1
    else:
        while segundo_numero < 0:
            suma -= 1
            segundo_numero += 1
    return suma

def prueba():
    try:
        primer_numero = ingreso_entero_reintento('Ingrese un numero', 5)
        segundo_numero = ingreso_entero_reintento('Ingrese un numero', 5)
        print(suma_lenta(primer_numero,segundo_numero))
    except Exception as err:
        print('No se puede realizar la prueba, los valores no son validos')

if __name__ == "__main__":
    prueba()