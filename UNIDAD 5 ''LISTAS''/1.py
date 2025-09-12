"""1) Crear una lista con las notas de 10 estudiantes. 
• Mostrar la lista completa. 
• Calcular y mostrar el promedio. 
• Indicar la nota más alta y la más baja. """

notas = [7, 8, 5, 9, 6, 10, 4, 8, 7, 9]

print("Notas de los estudiantes:", notas)

promedio = sum(notas) / len(notas)
print("Promedio de notas:", promedio)

nota_max = max(notas)
nota_min = min(notas)

print("Nota más alta:", nota_max)
print("Nota más baja:", nota_min)