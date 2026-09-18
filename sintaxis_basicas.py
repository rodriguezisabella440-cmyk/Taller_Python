#Creacion de variable
nombre = "Isabella" #Variable String (texto)
documento =123 #Variable tipo entero
direccion = "Medellin Crr 48a"

tiene_deuda = True

#mostrar informacion en pantalla
print(nombre)

print("CONCATENACIÓN USANDO +")
print("=" * 30)

#Opcion 1: Usando + NO recomendado
print("Mi nombre es:" + nombre + "Mi documento es:" + str (documento))

#Opcion 2: Usando coma
print("\nCONCATENACIÓN USANDO ,")
print("=" * 30)
print("Mi nombre es:" , nombre , "Mi documento es:" , documento , "direccion es:", direccion , "Tienes deuda?" , tiene_deuda)

print("\nCONCATENACIÓN USANDO F-STRINGS")
print("=" * 30)

print(f"Nombre : {nombre} Documento : {documento} Direccion : {direccion} Tienes deuda: {tiene_deuda}")


print(f"""
 - Nombre : {nombre}    
 - Documento : {documento} 
 - Direccion : {direccion}
 - Tienes deuda : {tiene_deuda}
 
 """)

print(f"\n Hola, {nombre}")
print(f"Bienvenida {nombre} a Python.\n")

