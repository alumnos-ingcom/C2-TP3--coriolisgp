#############
# Hernán Palumbo - @coriolisgp
# Ejercicio 1
# UNRN Andina - Introducción a la Ingeniería en Computación
##############

class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass

def ingreso_entero(mensaje):
    """
    Esta funcion muestra un mensaje y agrega la # para indicar el ingreso
    de un número entero.
    """
    ingreso = input(mensaje + " #")
    try:
        entero = int(ingreso)
        return entero
    except ValueError as err:
        raise IngresoIncorrecto("No era un número!") from err
    

def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
    while cantidad_reintentos > 0:
        try:
            entero = ingreso_entero(mensaje)
            return entero
        except IngresoIncorrecto as err:
            print(err)
            cantidad_reintentos = cantidad_reintentos - 1
            print(f'Le quedan {cantidad_reintentos} intentos')
    if cantidad_reintentos <= 0:
        print('Se quedo sin intentos, chauchau')
            

def ingreso_entero_restringido(mensaje, valor_minimo=0, valor_maximo=10):
    try:
        a = ingreso_entero(mensaje)
        if a > valor_maximo or a < valor_minimo:
            raise IngresoIncorrecto('Valor fuera de rango')
    except IngresoIncorrecto as err:
        print(err)
        
def prueba():
    ingreso_entero_restringido('Ingrese un Entero')
    ingreso_entero_reintento('Ingrese un Entero')

if __name__ == "__main__":
    prueba()