"""3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar 
los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio, 
cantidad) y lo agregue al archivo sin borrar el contenido existente."""

with open("productos.txt", "r") as archivo:
    print(" Lista de productos actuales:\n")
    for linea in archivo:
        linea = linea.strip()
        nombre, precio, cantidad = linea.split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

print("\n Agregar un nuevo producto:")
nombre_nuevo = input("Ingrese el nombre del producto: ")
precio_nuevo = input("Ingrese el precio: ")
cantidad_nueva = input("Ingrese la cantidad: ")

with open("productos.txt", "a") as archivo:
    archivo.write(f"{nombre_nuevo},{precio_nuevo},{cantidad_nueva}\n")

print("\n Producto agregado correctamente al archivo 'productos.txt'.")