import math
#1 Factorial
""" def factorial(n):
    if n == 0:
      return 1
    else: 
        return n * (factorial(n-1))
    
#print(factorial(4))

def factorial_numeros_previos(n):
 if n == 0:
     return 1
 else:
     print(factorial(n))
     factorial_numeros_previos(n-1)
print(factorial_numeros_previos(4))

 """
"""  #2 Fibonacci
def fibonacci(n):
    if n == 0:
      return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def fibonacci_indicados(n1,n2):
    if  n1 > n2:
      return 0
    else:
        print(fibonacci(n1))
        fibonacci_indicados(n1 + 1, n2) ## el n2 es el limite superior e indica hasta donde se va a calcular el fibonacci. funciona como un contador, como el hasta en el for.
        
        """ 
        
#3 
""" def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia_recursiva(base, exponente - 1)

print(potencia_recursiva(4, 2)) """
""" base_usuario = int(input("Ingresa la base: "))
exponente_usuario = int(input("Ingresa el exponente: "))
resultado = potencia_recursiva(base_usuario, exponente_usuario)
print(f"{base_usuario} elevado a {exponente_usuario} es igual a {resultado}")
 """
#4
""" def decimal_a_binario(n):
    if n == 0:
        return ""
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
print(decimal_a_binario(10))  # Ejemplo de uso

 """
"""  
#5 
def palindromo(palabra):
    if len(palabra) <= 1:
        return True ## acá es porque si la palabra es de un solo caracter o vacía, es un palíndromo.
    else:
        if palabra[0] != palabra[-1]: # esto es para chequear si el primer y último caracter son iguales.
            #con recursividad
            return False
        else:  
            return palindromo(palabra[1:-1]) """ ## va chequeando los caracteres desde las puntas hacia adentro.
            
#6
""" def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return (n // 10) + suma_digitos(n // 10)## el n // 10 es para ir sacando los dígitos de a uno, y el n % 10 es para sumar el último dígito.

suma_digitos(51) """
        
#7
""" def contar_bloques(n):
    if n == 0:
        return 0
    else:
        return n + contar_bloques(n - 1) # le restamos uno que es la cantidad de bloques del bloque actual y sumamos la cantidad de bloques del bloque anterior.
print(contar_bloques(4)) """

#8
def contar_digito(n,digito):
    if n == 0:
        return 0
    else:
        