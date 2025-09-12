"""5) Crear una lista con los nombres de 8 estudiantes presentes en clase. 
• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. 
• Mostrar la lista final actualizada."""


estudiantes = ["Ana", "Luis", "María", "Pedro", "Sofía", "Carlos", "Lucía", "Juan"]

print("Lista inicial de estudiantes:")
print(estudiantes)

accion = input("\n¿Desea agregar o eliminar un estudiante? (agregar/eliminar): ").lower()
if accion == "agregar":
    nuevo = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
    print(f"{nuevo} fue agregado a la lista.")

elif accion == "eliminar":
    borrar = input("Ingrese el nombre del estudiante a eliminar: ")
    if borrar in estudiantes:
        estudiantes.remove(borrar)
        print(f"{borrar} fue eliminado de la lista.")
    else:
        print(f"{borrar} no se encuentra en la lista.")

else:
    print("Opción no válida. No se realizaron cambios.")


print("\nLista final de estudiantes:")
print(estudiantes)