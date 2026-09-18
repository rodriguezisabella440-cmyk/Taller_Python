"""
for i in range(2,11,2):
    print(f"{i} - dracarys ✌️")
"""
"""
mensaje = input("Escribe tu mensaje :")    
repeticion = (input("Cuantas veces quieres repetir mensaje :"))
"""
"""
for i in range(repeticion):
    print(f"{i+1} - {mensaje}")
"""    

"""
    #Preguntar el nombre del estudiante
    #Preguntar a el profe cuantas notas quiere registrar. 
    #Hacer el promedio de las notas y mostrarlo 
    #Promedio >=3.5 Mostar Estuante Gano - Contrario Perdio
    
print("=== SISTERMA DE CALIFICACION. ===")
estudiante = input("Nombre del estudainte :")
can_notas = int(input("Cuantas notas vas a registrar : "))

promedio = 0
for i in range (can_notas): 
    notas=float(input(f"Ingrese nota {i+1} : "))
    
    if notas in range (0,5):
        print("Nota invalida")
        break 
    
    promedio =promedio + notas
promedio_final = promedio/can_notas

if (promedio_final) >=3.5:
    print(f"El estudiante {estudiante} - promedio {promedio_final} Gano🎉")
    print(f"El esttudiante {estudiante} = Promedio {promedio/can_notas} Gano🎉")
else: 
    print(f"El estudiante {estudiante} - Promedio {promedio_final} perdio ❌")

"""
while True: 
    menu = int (input( """
   seleccione opcion a realizar :
   1. sumar
   2. Restar 
   3. Salir
   :   """ )) 
   
    if menu == 1: 
        n1 = int(input("Ingrese un numero : "))
        n2 = int(input("Ingrese un numero : "))
        print(f"Resultado: {n1+n2}")

    elif menu ==2:
        n1=int(input("Ingrese un numero : "))
        n2=int(input("Ingrese un numero : "))
        print(f"Resultado: {n1-n2}")

    elif menu ==3: 
        print("Saliendo del sistema")
        break 
    else: 
        print("Opcion Invalido")
        
    
    
   
         
     
    
    