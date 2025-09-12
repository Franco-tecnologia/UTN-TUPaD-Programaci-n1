"""8) Crear una matriz con las notas de 5 estudiantes en 3 materias. 
• Mostrar el promedio de cada estudiante. 
• Mostrar el promedio de cada materia. """

notas = [
    [7, 8, 9],
    [6, 7, 8],
    [9, 9, 10],
    [5, 6, 7],
    [8, 7, 9]
]

print("Promedio de cada estudiante:")
for i, estudiante in enumerate(notas, start=1):
    promedio_estudiante = sum(estudiante) / len(estudiante)
    print(f"Estudiante {i}: {promedio_estudiante:.2f}")


print("\nPromedio de cada materia:")
num_materias = len(notas[0])
for j in range(num_materias):
    promedio_materia = sum(notas[i][j] for i in range(len(notas))) / len(notas)
    print(f"Materia {j+1}: {promedio_materia:.2f}")