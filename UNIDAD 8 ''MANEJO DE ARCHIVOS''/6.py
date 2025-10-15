"""6. Guardar los productos actualizados: Después de haber leído, buscado o agregado 
productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los 
productos actualizados desde la lista."""

productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        nombre, precio, cantidad = linea.split(",")
        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append(producto)

print(" Productos actuales:\n")
for p in productos:
    print(f"- {p['nombre']} (${p['precio']}, stock: {p['cantidad']})")

print("\n Agregar un nuevo producto:")
nombre_nuevo = input("Nombre: ")
precio_nuevo = float(input("Precio: "))
cantidad_nueva = int(input("Cantidad: "))

productos.append({
    "nombre": nombre_nuevo,
    "precio": precio_nuevo,
    "cantidad": cantidad_nueva
})

print("\n Producto agregado correctamente.")

with open("productos.txt", "w") as archivo:
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

print("\n Archivo 'productos.txt' actualizado con todos los productos.")