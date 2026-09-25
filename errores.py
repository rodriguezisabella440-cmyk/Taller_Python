"""
while True:
    try:
        nota=float(input("Ingrese una nota"))
    except ValueError: 
        print("Ingrese una nota valida")
"""
  
  
"""      

while True:
    try: 
        cantidad_notas = int(input("Cuantas notas quieres registrar: "))   
        
        #Crear for - para solicitar las notas.
        lista_notas=[]
        for i in range(cantidad_notas): 
            try: 
                notas= float(input("ingrese nota: "))
                lista_notas.append(notas) 
            except ValueError: 
                print("Nota invalida")
                
        print("Nota registradas: ", lista_notas)
        promedio=sum(lista_notas)/len(lista_notas)
        print(f"Promedio: {promedio}")
        
        if promedio<=2: 
            print("Muy mal")
        
        elif promedio<=3: 
            print("basico")
       
        elif promedio<=4: 
            print("aceptable")
        
        elif promedio<=5:
            print("bien")
        
        else:
            print("Nota invalida")
        
    except ValueError: 
        print("Ingrese una cantidad valida")
 """       
 
#EJERCICIO 1: 

try: 
    numero =int(input("Ingrese un numero entero: "))
    print(f"El numero ingresado es:{numero}") 
        
except ValueError:
        print("error: debe ingresar un numero entero valido")
        
#Ejercicio 2: 

try: 
    dividiendo =float(input("Ingrese el dividendo: "))
    divisor =float(input("Ingrese el divisor: "))
    resultado = dividiendo/divisor 
    print(f"Resultado: {dividiendo} / {divisor} = {resultado}")
    
except ZeroDivisionError: 
    print("Error: no es posible dividir entre cero.")
except ValueError: 
    print("Error: ingrese unicamente valores numericos.")
    
#Ejercicio 3: 

try: 
    edad =int(input("Ingrese su edad: "))
except ValueError: 
    print("Error:La edad debe ser un numero entero.")
    
else:
    if edad > 18: 
        print("Acceso permitido")
        
    else: 
        print("Acceso denegado: debe ser mayor de edad.")
    
finally:
    print("Verificacion finalizada")
    

#Ejercicio 4: 
while True:
    try:
        nota = float(input("Ingrese una nota entre 0.0 y 5.0: "))
        if nota < 0.0 or nota > 5.0:
            raise ValueError("La nota debe estar entre 0.0 y 5.0.")
        break   # sale del ciclo si el valor es válido
    except ValueError as e:
        print(f"Entrada inválida: {e}. Intente de nuevo.")

print(f"Nota registrada: {nota}")

    
#Ejercicio 5: 
def calcular_promedio(notas):
    if len(notas) == 0:
        raise ValueError("La lista de notas no puede estar vacía.")
    return sum(notas) / len(notas)

try:
    n      = int(input("¿Cuántas notas va a ingresar? "))
    notas  = []
    for i in range(n):
        nota = float(input(f"  Nota {i + 1}: "))
        notas.append(nota)
    promedio = calcular_promedio(notas)
    print(f"Promedio: {round(promedio, 2)}")
except ValueError as e:
    print(f"Error: {e}")
    
      
            
    
   