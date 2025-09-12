"""6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el 
último pasa a ser el primero)."""

numeros = [1, 2, 3, 4, 5, 6, 7]

print("Lista original:", numeros)

rotada = [numeros[-1]] + numeros[:-1]

print("Lista rotada a la derecha:", rotada)