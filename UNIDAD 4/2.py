"""2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
dígitos que contiene. """

numero = int(input("Ingrese un número entero: "))

numero = abs(numero)
cantidad_digitos = 0
if numero == 0:
    cantidad_digitos = 1 
else:
    while numero > 0:
        numero = numero // 10 
        cantidad_digitos += 1  

print("La cantidad de dígitos es:", cantidad_digitos)