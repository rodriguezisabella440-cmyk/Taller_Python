"""
lista_producto=[] #lista en blanco
cantidad=int(input("cantidad de productos a comprar: "))

for i in range(cantidad): 
    producto=input(f"Nombre del product{i+1}: ")
    #Agregar producto a la lista
    lista_producto.append(producto)
print(f"productos comprados: {lista_producto}")  

""" 
lista_perros=[]
lista_gatos=[]
while True: 
    pregunta=int(input("""
    1. Registrar Perros 🐕‍🦺
    2. Registrar Gaticos 🐈‍⬛
    3. Listado de Perritos 🐾
    4. Listado de Gaticos 🐈              
    5. Salir
    """))

    if pregunta ==1: 
     perro =input("Ingrese el nombre del perro")
     lista_perros.append(perro)
     print("perrito registrado")
    
    elif pregunta ==2: 
        gato =input("Ingrese nombre del gato: ")
        lista_gatos.append(gato)
        print("Gatico registrad")
        
    elif pregunta ==3: 
         print("listado de perros", lista_perros)
    
    elif pregunta ==4: 
       print("listado gaticos", lista_gatos)
    
    elif pregunta ==5:
         print("Saliendo del sistema")
         break
     
    else: 
        print("Opcion Invalida")
        break 
     
    