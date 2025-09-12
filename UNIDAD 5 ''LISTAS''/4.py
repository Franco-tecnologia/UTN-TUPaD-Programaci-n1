"""4) Dada una lista con valores repetidos: 
datos = [1,3,5,3,7,1,9,5,3]
• Crear una nueva lista sin elementos repetidos. 
• Mostrar el resultado.""" 

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

sin_repetidos = []
for numero in datos:
    if numero not in sin_repetidos:
        sin_repetidos.append(numero)

print("Lista original:", datos)
print("Lista sin repetidos:", sin_repetidos)