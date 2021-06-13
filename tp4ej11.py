#############
# Hernán Palumbo - @coriolisgp
# Ejercicio 11
# UNRN Andina - Introducción a la Ingeniería en Computación
##############

def es_palindromo(texto):
    texto = str(texto)
    es_palindromo = False
    texto = texto.upper()
    texto_dadovuelta = texto[::-1]
    if texto == texto_dadovuelta:
        es_palindromo = True
    return es_palindromo
        
def prueba():
    palabra = 'menem'
    print(es_palindromo(palabra))

if __name__ == "__main__":
    prueba()