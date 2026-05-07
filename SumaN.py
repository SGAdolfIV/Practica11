def suma_naturales(n):
   
    if n == 0:
        return 0
    
    else:
        return n + suma_naturales(n - 1)

numero = 2
resultado = suma_naturales(numero)
print(f"La suma de los primeros {numero} números es: {resultado}")
