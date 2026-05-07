def imprimir_arreglo(arreglo, indice=0):
    # a) CASO BASE: Si el índice llega al final del arreglo, termina.
    if indice == len(arreglo):
        return
    
    # b) CASO RECURSIVO:
    # 1. Realiza la acción (imprimir)
    print(arreglo[indice])
    imprimir_arreglo(arreglo, indice + 1)

numeros = [11, 22, 33, 42, 53]
imprimir_arreglo(numeros)
"""
es exactamente la resolucion del problema anterior
"""