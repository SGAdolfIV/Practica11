def suma_n(n):
   
    if n == 0:
        return 0
    
    else:
        return n + suma_n(n - 1)

numero = 5
resultado = suma_n(numero)
print(f"La suma de los primeros {numero} números es: {resultado}")
"""
a) el caso base es cuando n=1 pues 1 es el primer natural
b) el caso recursivo es cuando T(n)=n+T(n-1)
ecuacion de recurrencia T(n)=T(n-1)+1
r=1
aoT(n) + ... * akT(n-k)=0
aoT(n) + ... + akT(n-k)= b^np(n)
T(n)-T(n-1)=1
x^k=T(n). k=1
x-1=1
(x-1)(x-1)=0
T(n)=c1(1)^n+c2n(1)^n
Complejidad de O(T(n))=n es lineal
"""
