lista = [1,2,3,4,5,6,7,8,9,10]
def busqueda_binaria(elementos, objetivo):
    izquierda = 0
    derecha = len(elementos)-1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if elementos[medio] == objetivo:
            return medio
        elif elementos[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1  


objetivo = 6
resultado = busqueda_binaria(lista, objetivo)
print('El elemento esta en el indice',resultado)
