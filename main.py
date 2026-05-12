from consultas import obtener_productos, obtener_ventas, obtener_cantidad_de_productos_vendidos, obtener_precio_total_vendido, producto_mas_vendido, producto_menos_vendido, producto_que_mas_ingresos_genero, producto_que_menos_ingresos_genero

productos = obtener_productos()
ventas = obtener_ventas()
cantidad_por_producto = obtener_cantidad_de_productos_vendidos()
total_vendido = obtener_precio_total_vendido()
producto_mas_vendido = producto_mas_vendido()
producto_menos_vendido = producto_menos_vendido()
producto_mas_ingresos = producto_que_mas_ingresos_genero()
producto_menos_ingresos = producto_que_menos_ingresos_genero()

# print("Productos:")
# for producto in productos:
#     print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[2]}")

# print("\nVentas:")
# for venta in ventas:    
#     print(f"ID: {venta[0]}, Producto ID: {venta[1]}, Cantidad: {venta[2]}, Fecha: {venta[3]}")

# print("\nCantidad de productos vendidos por producto:")
# for producto in cantidad_por_producto:
#     print(f"Producto: {producto[0]}, Cantidad Vendida: {producto[1]}")

# print("\nPrecio total vendido por producto:")
# for producto in total_vendido:
#     print(f"Producto: {producto[0]}, Total Vendido: {producto[1]}")

print("\nProducto más vendido:")
print(f"Producto: {producto_mas_vendido[0]}, Cantidad Vendida: {producto_mas_vendido[1]}")

print("\nProducto menos vendido:")
print(f"Producto: {producto_menos_vendido[0]}, Cantidad Vendida: {producto_menos_vendido[1]}")

print("\nProducto que más ingresos generó:")
print(f"Producto: {producto_mas_ingresos[0]}, Ingresos: {producto_mas_ingresos[1]}")

print("\nProducto que menos ingresos generó:")
print(f"Producto: {producto_menos_ingresos[0]}, Ingresos: {producto_menos_ingresos[1]}")
