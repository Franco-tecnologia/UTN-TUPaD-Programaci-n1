"""" 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
 pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos."""""


num1 = int(input("Por favor, ingresa el primer número entero (distinto de 0): "))
num2 = int(input("Por favor, ingresa el segundo número entero (distinto de 0): "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print(f"La suma de {num1} y {num2} es: {suma}")
print(f"La resta de {num1} y {num2} es: {resta}")
print(f"La multiplicación de {num1} y {num2} es: {multiplicacion}")
print(f"La división de {num1} y {num2} es: {division:.2f}")