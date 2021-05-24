#############
# Hernán Palumbo - @coriolisgp
# Ejercicio 10
# UNRN Andina - Introducción a la Ingeniería en Computación
##############

from tp4ej1 import IngresoIncorrecto
from tp4ej9 import es_primo

def factores_primos(numero):
    try:
        if numero > 0:
            lista_numeros_primos = []
            tupla_factores_primos = []
            numeros_primos = numero
            while numeros_primos > 1:
                if es_primo(numeros_primos):
                    lista_numeros_primos.append(numeros_primos)
                numeros_primos -= 1
            
            for num_primo in lista_numeros_primos:
                if numero % num_primo == 0:
                    tupla_factores_primos.append(num_primo)
            return tuple(tupla_factores_primos)
        else:
            raise IngresoIncorrecto('El valor ingresado no es un entero positivo')
    except TypeError as err:
        raise IngresoIncorrecto ('El valor ingresado no es un numero') from err
        
def prueba():
    try:
        print(factores_primos(990))
    except Exception as err:
        print(err)

if __name__ == "__main__":
    prueba()

