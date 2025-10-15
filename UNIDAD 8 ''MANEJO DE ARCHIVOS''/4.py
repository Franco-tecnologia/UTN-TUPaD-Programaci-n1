"""4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en 
una lista llamada productos, donde cada elemento sea un diccionario con claves: 
nombre, precio, cantidad."""

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

print(" Lista de productos cargados en memoria:\n")
for p in productos:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

print("\n Estructura interna de la lista:")
print(productos)