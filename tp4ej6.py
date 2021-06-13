#############
# Hernán Palumbo - @coriolisgp
# Ejercicio 6
# UNRN Andina - Introducción a la Ingeniería en Computación
##############

def minimo(lista):
    minimo = lista[0]
    for numero in lista[1:]:
        if numero < minimo:
            minimo = numero
    return minimo

def maximo(lista):
    maximo = lista[0]
    for numero in lista[1:]:
        if numero > maximo:
            maximo = numero
    return maximo

def prueba():
    try:
        lista = [1,3,4,5,100,6,8,-2]
        print (f'Minimo: {minimo(lista)}')
        print (f'Máximo: {maximo(lista)}')
    except Exception as err:
        print('Valor invalido en la lista' + ' -----> ' + repr(err))

if __name__ == "__main__":
    prueba()