



"""""
#Crear Variable
print("por favor ingrese los siguientes datos")

var_nombre = input("nombre:")
var_edad = int(input("edad:"))

#Crear condicon 
if var_edad >= 18 :
 print(f"{var_nombre} Eres mayor de edad.")
  
else:
 print(f"{var_nombre} Eres menor de edad.")
"""""

"""""
#Crear Variable
print("por favor ingrese los siguientes datos")

var_nombre = input("nombre del estudiante:")
var_notafinal = float(input("nota final"))

#Crear Condicion
if var_notafinal < 0 or var_notafinal >5: 
   print("Nota invalida.")
   
elif var_notafinal >= 3.5 :
    print(f"EStudiante {var_nombre} GANO 🎉")
    
else: 
    print(f"EStudiante {var_nombre} PERDIO ❌")
"""

""" #Ejercicio 1 Positivo, negativo o cero
  
print("por favor ingrese los siguientes datos")

numero = float(input("Ingrese un numero"))

if numero < 0:
    print(f" {numero} es positivo")
    
elif numero > 0: 
     print(f" {numero} es negativo")
     
else: 
    print("el numero es cero")"""

""" #Ejercicio 2: MAyoria de edad 

edad = int(input("ingrese su edad:"))

if edad >= 18:
    print("Es mayor de edad")

else: 
    print("Es menor de edad") """
    
"""#Ejercicio 3: Par o impar 

numero = int(input("Ingrese un numero: "))

if numero % 2 == 0:
    print(f"{numero} es par")
    
else:
    print(f"{numero} es impar")"""
    
"""#Ejercicio 4: Clasificacion de nota academica 

nota = float(input("Ingrese la nota obtneida (0.0 a 5.0)"))

if nota > 4.5: 
    print("Desempeño superior")
    
elif nota > 3.5:
    print("Desempeño alto")
    
elif nota > 3.0: 
    print("Desempeño bajo") """ 
    
""" #Ejercicio 5: El mayor de tres numeros 

n1 = float(input("ingrese el primer numero"))
n2 = float(input("Ingrese el segundo numero"))
n3 = float(input("Ingrese el tercer numero"))

if n1 > n2 and n1 > n3: 
    mayor = n1
    
elif n2 > n1 and n2 > n3: 
    mayor = n2
    
else:
    mayor = n3 
    
print(f"El mayor de los tres numero es: {mayor}") """ 

# Taller 2 Ejercicios para resolver 
#1

print("Por favor ingrese los siguientes datos")

nombre = input("Escribre tu nombre")
Edad = int(input("Escribe tu edad"))


if Edad < 0:
    print("error")

elif Edad >= 18:
     print(f"{nombre} es mayor de edad")
     
else: 
    print(f"{nombre} te faltan {18-Edad} años para ser mayor")
    
  #2
  
nombre = input("escribe tu nombre:")   
Notafinal = float(input("Ingrese su nota final entre 0.0 a 5.0: "))
  
if Notafinal < 3.0 :
   print("insuficiente") 
   
elif Notafinal < 3.4 : 
    print("Aceptable")
    
elif Notafinal < 3.5 : 
    print("Bueno")
    
elif Notafinal <  4.5 : 
    print("Excelente")
    
else: 
    print(f"{nombre}{Notafinal}")
    
     


    
    
    
    

    

