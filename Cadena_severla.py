def imprimir_severla(cadena):
    # a) CASO BASE: Si la cadena está vacía, no hay nada que imprimir
    if len(cadena) == 0:
        return
    # b) CASO RECURSIVO:
    # Primero llamamos a la función con toda la cadena menos el primer carácter
    imprimir_severla(cadena[1:])
    
    # Al regresar de la recursión (en el camino de vuelta), imprimimos
    # Esto garantiza que el primer carácter sea el ÚLTIMO en imprimirse
    print(cadena[0], end="")
# Ejemplo de uso
texto = "Alreves"
print(f"Original: {texto}")
print("Al revés: ", end="")
imprimir_severla(texto)
print() # Salto de línea final