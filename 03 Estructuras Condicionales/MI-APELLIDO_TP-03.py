from statistics import mean, median, mode
import random
#1
""" 
edadUser = int(input("ingrese su edad:"))
if edadUser > 18:
    print(f"Es mayor de edad") """
    
#2
""" nota = float(input("Ingrese su nota: "))

if nota >= 6:
    print(f"Aprobado")
else:
    print(f"desaprobado") """
    
#3
""" numeroSolicitado = int(input("ingrese un número: "))
if numeroSolicitado % 2 == 0:
    print(f"Ha ingresado un número par")
else:
    print(f"Por favor, ingrese un número par")    """ 
    
#4
""" edad = int(input("ingrese su edad: "))

if edad < 12:
    print(f"niño/a")
elif edad >= 12 and edad < 18:
    print(f"adolescente")
elif edad >= 18 and edad < 30:
      print(f"adulto joven")
elif edad >= 30:
      print(f"adulto") """
      
#5#
""" contraseña = input("Por favor, ingrese una contraseña de entre 8 y 14 caracteres: ")

if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres") """
    
#6#
""" numeros_aleatorios = [random.randint(1,100) for i in range(50)]

media = mean(numeros_aleatorios)
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)

if media > mediana > moda:
    print("sesgo positivo")
elif media < mediana < moda:
    print("sesgo negativo")
elif media == mediana == moda:
    print("Sesgo simetrico")
else:
    print("sesgo no claro")

print(f"Lista de numeros: {numeros_aleatorios}")
print(f"Media: {media}")
print(f"Moda: {moda}")
print(f"Median: {mediana}") """
#7#
""" vocales = ["A","E","I","O","U","a","e","i","o","u"]

frase = input("Ingrese una frase o palabra: ")

if frase[-1] in vocales:
    print((frase + "!"))
else:
    print(frase)    
 """
 
 #8
""" nombre = input("Ingrese su nombre:")
numeroNom = int(input("Ingrese un número del 1 al 3:"))

if numeroNom == 1:
    print(nombre.upper())
elif numeroNom == 2:
    print(nombre.lower())
elif numeroNom == 3:
    print(nombre.title())
else:
    print("Por favor: ingrese un número del 1 al 3:") """
    
    
#9
""" terremoto = float(input("ingrese magnitud de terremoto: "))

if terremoto < 3:
   print("Muy leve(imperceptible)")
elif terremoto >= 3 and terremoto < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= terremoto <= 5:
    print("moderado (sentido por personas, pero no causa daños generalmente)")
elif  5 <= terremoto < 6:
    print("fuerte (puede causar daños en estructuras leves)")
elif 6 <= terremoto < 7:
    print("Muy fuerte (puede causar daños significativos)")
elif terremoto >= 7:
    print("Extremo")  """

#10
meses_validos = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
                 "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
hemisferio = input("Ingrese su hemisferio (norte, sur): ").lower()
mes = input("Ingrese mes del año: ").strip().lower()
dia = int(input("Ingrese día: "))
             
if mes in meses_validos:
    numero_mes = meses_validos.index(mes) + 1
    if hemisferio == "norte":
        if numero_mes in [1, 2] or (numero_mes == 3 and dia < 21) or (numero_mes == 12 and dia >= 21):
            print("invierno")
        elif (numero_mes == 3 and dia >= 21) or numero_mes in [4, 5] or (numero_mes == 6 and dia < 21):
            print("primavera")
        elif (numero_mes == 6 and dia >= 21) or numero_mes in [7, 8] or (numero_mes == 9 and dia < 23):
            print("verano")
        elif (numero_mes == 9 and dia >= 23) or numero_mes in [10, 11] or (numero_mes == 12 and dia < 21):
            print("otoño")
else:
    print("Mes inválido")
