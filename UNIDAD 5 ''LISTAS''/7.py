"""7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una 
semana. 
• Calcular el promedio de las mínimas y el de las máximas. 
• Mostrar en qué día se registró la mayor amplitud térmica."""

temperaturas = [
    [12, 20],
    [15, 25],
    [10, 22],
    [14, 28],
    [13, 21],
    [11, 24],
    [16, 27]
]

suma_min = sum(fila[0] for fila in temperaturas)
suma_max = sum(fila[1] for fila in temperaturas)

promedio_min = suma_min / len(temperaturas)
promedio_max = suma_max / len(temperaturas)

print(f"Promedio de temperaturas mínimas: {promedio_min:.2f}°C")
print(f"Promedio de temperaturas máximas: {promedio_max:.2f}°C")

amplitudes = [fila[1] - fila[0] for fila in temperaturas]
max_amplitud = max(amplitudes)
dia_max_amplitud = amplitudes.index(max_amplitud) + 1 

print(f"Mayor amplitud térmica: {max_amplitud}°C en el día {dia_max_amplitud}")