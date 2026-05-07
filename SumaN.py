def suma_n(n):
   
    if n == 0:
        return 0
    
    else:
        return n + suma_n(n - 1)

numero = 2
resultado = suma_n(numero)
print(f"La suma de los primeros {numero} números es: {resultado}")
