import random
from statistics import mean
#1
""" for i in range (0,101):
    print(i) """
    
#2
""" 
numero = int(len(input("ingrese un numero: ")))

print(f"el número ingresado contiene {numero} digitos")
 """
 
#3
""" numeroUno = int(input("Ingrese el primer número: "))
numeroDos = int(input("Ingrese el segundo número: "))
cont = 0
for i in range(numeroUno + 1, numeroDos):
    cont += i
print(cont) """

#4
""" cont = 0
numero = int(input("ingrese un número: "))
while numero > 0:
    
    cont += numero 
    numero = int(input("ingrese un número: "))
    if numero == 0:
        print(f"Se detuvo al ingresar 0: la suma actual es {cont}") """

#5#
""" 
numeroSecreto = random.randint(0,9)
numero = int(input("ingrese un numero del 0 al 9: "))

cont = 1
while numeroSecreto != numero:
    cont += 1
    numero = int(input("ingrese un numero del 0 al 9: "))
print(f"adivinaste, te llevó {cont} intentos")     """

#6#
""" 
for i in range(101,-1, -1):
    if i % 2 == 0:
        print(i) """
        
#7#
""" 
numero = int(input("ingrese un numero: "))
cont = 0
if numero > 0:
 for i in range (0, numero + 1):
    cont += i    
    
print(cont) """

#8
""" pares = 0
impares = 0
negativo = 0
positivo = 0

for i in range (100):
    numero = int(input("ingrese un numero: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero > 0:
        positivo += 1
    else:
        negativo += 1
        

print(f"los pares son {pares}")
print(f"los impares son {impares}")
print(f"los positivos son {positivo}")
print(f"los negativos son {negativo}")         """

#9
# suma = 0
""" numeroProm = []
for i in range (100):
    numero = int(input("ingrese un numero: "))
    numeroProm.append(numero)
prom = mean(numeroProm)
    
print (f"El promedio de los valores es {prom}")

 """
 
#10

""" numero = (input("ingrese un numero: "))

inversion = numero[::-1]
print(f"el numero invertido es {inversion} ") """