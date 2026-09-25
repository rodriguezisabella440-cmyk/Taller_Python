#Variables
print("===Tiendaa Donde Ely ===")

print("por favor ingrese la siguiente informacion:  \n")
Cliente =input("Nobmbre de cliente: ")
Producto =input("Nombre de producto: ")
Cantidad =int(input("Cantidad :"))
Precio =float(input("Precio: "))

#Variable para preguntar si la compra es a domicilio
Domicilio =input("La compra es para domicilio (SI - No): ")
#Condicional verificar que respondio el usuario

#.upper() convierte el mayusculo .lower() minuscula
if Domicilio.upper() =="NO" : 
    print("===RESUMEN DE COMPRA===")
    print(f"""
    -Cliente :{Cliente}
    -Producto :{Producto}
    -Cantidad :{Cantidad}
    -Precio: {Precio}
    -Subtotal: {Cantidad*Precio}
          
          ❤️Gracias por su compra.
          """)

elif Domicilio.upper() =="SI" : 
     Direccion=input("Ingrese el Municipio de envio (MEDELLÍN,ITAGUI,BELLO) :")
     
     valor_domicilio=0 
     if Direccion.lower()=="medellin": 
          valor_domicilio =5000
     elif Direccion.lower()=="itagui":
          valor_domicilio=1000
     elif Direccion.lower()=="bello": 
          valor_domicilio=8000
     else: 
         print("Direccion Invalida")
     
     #Mostrar resumen de la venta 
     print("===RESUMEN DE COMPRA===")
     print(f"""
    -Cliente :{Cliente}
    -Producto :{Producto}
    -Cantidad :{Cantidad}
    -Precio: {Precio}
    -Subtotal: {Cantidad*Precio}
    -Domicilio: {valor_domicilio}
    -Total Pagar: {valor_domicilio + {Cantidad*Precio}}
              
              ❤️Gracias por su compra.
              """)  
else:
    print("Opcion invalida")         
                            