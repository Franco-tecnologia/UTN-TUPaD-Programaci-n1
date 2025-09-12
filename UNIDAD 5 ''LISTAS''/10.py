"""10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
• Mostrar el total vendido por cada producto. 
• Mostrar el día con mayores ventas totales. 
• Indicar cuál fue el producto más vendido en la semana. """

ventas = [
    [10, 12, 15, 14, 11, 13, 16],  
    [8, 9, 7, 10, 12, 11, 9],      
    [5, 7, 6, 8, 5, 6, 7],        
    [20, 18, 22, 19, 21, 20, 23]   
]


print("Total vendido por producto:")
totales_productos = []
for i, producto in enumerate(ventas, start=1):
    total = sum(producto)
    totales_productos.append(total)
    print(f"Producto {i}: {total} unidades")


totales_dias = [sum(ventas[p][d] for p in range(len(ventas))) for d in range(7)]
max_ventas_dia = max(totales_dias)
dia_max_ventas = totales_dias.index(max_ventas_dia) + 1 
print(f"\nDía con mayores ventas totales: Día {dia_max_ventas} ({max_ventas_dia} unidades)")

max_ventas_producto = max(totales_productos)
producto_mas_vendido = totales_productos.index(max_ventas_producto) + 1

print(f"Producto más vendido en la semana: Producto {producto_mas_vendido} ({max_ventas_producto} unidades)")