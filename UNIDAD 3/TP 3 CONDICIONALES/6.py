import random
from statistics import mean, median, mode, StatisticsError
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
try:
    moda = mode(numeros_aleatorios)
except StatisticsError:
    moda = None

print("Lista de números:", numeros_aleatorios)
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

if moda is not None:
    if media > mediana > moda:
        print("La distribución tiene sesgo positivo (a la derecha).")
    elif media < mediana < moda:
        print("La distribución tiene sesgo negativo (a la izquierda).")
    elif media == mediana == moda:
        print("La distribución no tiene sesgo.")
    else:
        print("No se puede determinar un sesgo claro con estos valores.")
else:
    print("No se puede calcular la moda única, por lo que no se puede determinar el sesgo.")