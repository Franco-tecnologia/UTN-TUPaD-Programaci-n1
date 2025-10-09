"""8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
Permití al usuario: 
• Consultar el stock de un producto ingresado. 
• Agregar unidades al stock si el producto ya existe. 
• Agregar un nuevo producto si no existe."""

productos = {
    "manzanas": 50,
    "naranjas": 30,
    "bananas": 20
}

print(" Stock actual de productos:")
for producto, stock in productos.items():
    print(f"- {producto}: {stock} unidades")

producto = input("\n Ingresá el nombre del producto que querés consultar: ").lower()

if producto in productos:
    print(f" El producto '{producto}' tiene {productos[producto]} unidades en stock.")
    
    opcion = input("¿Querés agregar unidades al stock? (si/no): ").lower()
    if opcion == "si":
        cantidad = int(input("¿Cuántas unidades querés agregar?: "))
        productos[producto] += cantidad
        print(f" Stock actualizado: {producto} → {productos[producto]} unidades.")
    else:
        print("No se modificó el stock.")

else:
    print(f" El producto '{producto}' no existe en el inventario.")
    opcion = input("¿Querés agregarlo al inventario? (si/no): ").lower()
    if opcion == "si":
        cantidad = int(input("Ingresá el stock inicial: "))
        productos[producto] = cantidad
        print(f" Producto agregado: {producto} → {productos[producto]} unidades.")
    else:
        print("El producto no fue agregado.")

print("\n Stock final:")
for producto, stock in productos.items():
    print(f"- {producto}: {stock} unidades")