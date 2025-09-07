"""9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
poder procesar 100 números cambiando solo un valor)."""

suma = 0

cantidad = 100 

for i in range(cantidad):
    num = int(input(f"Ingrese el número {i+1}: "))
    suma += num  

media = suma / cantidad

print("\n--- Resultado ---")
print("La media de los", cantidad, "números es:", media)