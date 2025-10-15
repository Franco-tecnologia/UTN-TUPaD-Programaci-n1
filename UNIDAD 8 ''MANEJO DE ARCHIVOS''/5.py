"""5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un 
producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si 
no existe, mostrar un mensaje de error."""

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

print(" Productos cargados:")
for p in productos:
    print(f"- {p['nombre']} (${p['precio']}, stock: {p['cantidad']})")

nombre_buscar = input("\n Ingrese el nombre del producto a buscar: ").lower()

encontrado = False
for p in productos:
    if p["nombre"].lower() == nombre_buscar:
        print(f"\n Producto encontrado:")
        print(f"Nombre: {p['nombre']}")
        print(f"Precio: ${p['precio']}")
        print(f"Cantidad: {p['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("\n El producto no existe en la lista.")