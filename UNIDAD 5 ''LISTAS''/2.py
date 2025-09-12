"""2) Pedir al usuario que cargue 5 productos en una lista. 
• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted(). 
• Preguntar al usuario qué producto desea eliminar y actualizar la lista. """

productos = []
for i in range(5):
    producto = input(f"Ingrese el producto {i+1}: ")
    productos.append(producto)
productos_ordenados = sorted(productos)
print("\nLista de productos ordenada alfabéticamente:")
print(productos_ordenados)
eliminar = input("\n¿Qué producto desea eliminar?: ")

if eliminar in productos_ordenados:
    productos_ordenados.remove(eliminar)
    print("\nProducto eliminado correctamente.")
else:
    print("\nEse producto no está en la lista.")

print("Lista actualizada de productos:")
print(productos_ordenados)