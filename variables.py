
print("Ejercicio1: suma de dos numeros")
print(".."*15)

numero1 = float(input("Ingrese el primer número:"))
numero2 = float(input("Ingrese el segundo numero:"))


print(f"Resultado : {numero1+numero2}")
#------------------------------------------------------------

print("Ejercicio2: Area de un  rectangulo")
print(".."*15)

base=float(input("Ingrese la base del rectangulo:"))
altura=float(input("Ingrese la altura del rectangulo:"))

print(f"El área del rectángulo es:{base*altura}")
#-----------------------------------------------------

print("Ejercicio3: Minutos a horas y minutos")
print(".."*15)

minutos_totales =int(input("Ingrese la cantidad de minutos"))

horas= minutos_totales // 60
minutos = minutos_totales % 60


print(f"{minutos_totales} minutos equivalen a {horas} horas y {minutos} minutos")

#------------------------------------------------------------
print("Ejercicio4: Precio con descuento")
print(".."*15)

precio = float(input("Ingrese el precio del prodructo"))
descuento = float(input("Ingrese el valor de descuento"))

valor_descuento = precio * (descuento/ 100) 
precio_final = precio - valor_descuento

print(f"el precio final a pagar es: {precio_final}")

#---------------------------------------------------------

print("Ejercicio5: Intercambio de variables")
print(".."*15)

a = float(input("Ingrese el valor de a:"))
b = float(input("Ingrese el valor de b"))

auxiliar = a 
a = b 
b = auxiliar 

print(f"Después del intercambio: a = {a} , b = {b}")

peso = float(input("ingrese su peso: "))

print(f" Su peso es: {peso}")



