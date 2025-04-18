#1#
""" def imprimir_hola_mundo():
    return print("Hola Mundo")
    
imprimir_hola_mundo() """

#2#
""" def saludar_usuario(nombre):
 return print(f"Hola {nombre}")
 
saludar_usuario("Arturo") """

#3#
""" nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su residencia: ")

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
    
informacion_personal(nombre, apellido, edad, residencia)
   
    """
#4
""" radio = float(input("Ingrese el radio del círculo: "))

def calcular_area_circulo(radio):
    pi = 3.14159
    area = pi * (radio ** 2)
    return print(f" El área del circulo es: {area}")  

def calcular_perimetro_circulo(radio):
    pi = 3.14159
    perimetro = 2 * pi * radio
    return print(f"El perimetro del circulo es: {perimetro}")

calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)
   
  """
#5
""" segundos = int(input("Ingrese la cantidad de segundos: "))

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

resultado = segundos_a_horas(segundos)
print(f"{segundos} segundos son {resultado} horas")
 """
 
#6 
""" numero = int(input("Ingrese un número: "))
def tabla_multiplicar(numero):
    for i in range(1, 11):
        tabla = numero * i
        print(f"{numero} x {i} = {tabla}")
   

tabla_multiplicar(numero)
         """
         
#7#
""" numeroUno = int(input("Ingrese el primer número: "))
numeroDos = int(input("Ingrese el segundo número: "))

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División: {division}")
    
operaciones_basicas(numeroUno, numeroDos) """

#8
""" peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros(por ejemplo: 1.72): "))
print(f"Peso: {peso}, Altura: {altura}")  
def calcular_peso(peso, altura):
    imc = peso / (altura ** 2)
    print(f"Su IMC es: {imc:.2f}") 
    
       
calcular_peso(peso, altura) """
#9
""" grados = float(input("Ingrese la temperatura en grados Celsius: "))
def celcius_a_fahrenheit(grados):
    fahrenheit = (grados * 9/5) + 32
    print(f"{grados} grados Celsius son {fahrenheit} grados Fahrenheit")

celcius_a_fahrenheit(grados) """
#10

""" a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
def calcular_promedio(a,b,c):
    promedio = (a + b + c) / 3
    print(f"El promedio entre {a}, {b} y {c} es: {promedio:.2f}")
    
calcular_promedio(a,b,c) """