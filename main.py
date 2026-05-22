from consultas import obtener_productos, obtener_ventas, obtener_cantidad_de_productos_vendidos, obtener_precio_total_vendido, producto_mas_vendido, producto_menos_vendido, producto_que_mas_ingresos_genero, producto_que_menos_ingresos_genero, cantidad_por_categoria, ventas_por_categoria, ventas_por_fecha
from analisis.analisis import porcentaje_ventas_por_categoria, promedio_por_venta, categoria_dominante
from analisis.estadisticas import media, mediana, desviacion_estandar, valor_maximo, valor_minimo
import numpy as np

productos = obtener_productos()
ventas = obtener_ventas()
cantidad_por_producto = obtener_cantidad_de_productos_vendidos()
total_vendido = obtener_precio_total_vendido()
el_producto_mas_vendido = producto_mas_vendido()
el_producto_menos_vendido = producto_menos_vendido()
producto_mas_ingresos = producto_que_mas_ingresos_genero()
producto_menos_ingresos = producto_que_menos_ingresos_genero()
datos_cantidad_por_categoria = cantidad_por_categoria()
datos_ventas_por_categoria = ventas_por_categoria()
datos_ventas_por_fecha = ventas_por_fecha()
porcentaje_categoria = porcentaje_ventas_por_categoria()
promedio_venta = promedio_por_venta()
datos_categoria_dominante = categoria_dominante()

#Todos los productos
# print("Productos:")
# for producto in productos:
#     print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[2]}")

#Todos las ventas
# print("\nVentas:")
# for venta in ventas:    
#     print(f"ID: {venta[0]}, Producto ID: {venta[1]}, Cantidad: {venta[2]}, Fecha: {venta[3]}")

#Cantidad de productos vendidos por producto
# print("\nCantidad de productos vendidos por producto:")
# for producto in cantidad_por_producto:
#     print(f"Producto: {producto[0]}, Cantidad Vendida: {producto[1]}")

#Precio total vendido por producto
# print("\nPrecio total vendido por producto:")
# for producto in total_vendido:
#     print(f"Producto: {producto[0]}, Total Vendido: {producto[1]}")

# #Cantidad de productos vendidos por categoría
# print("\nCantidad de productos vendidos por categoría:")
# for categoria in cantidad_por_categoria:
#     print(f"Categoría: {categoria[0]}, Cantidad Vendida: {categoria[1]}")

#Ventas por categoría
print("\nVentas por categoría:")
for categoria in datos_ventas_por_categoria:
    print(f"Categoría: {categoria[0]}, Total Vendido: {categoria[1]}")

# #Ventas por fecha
# print("\nVentas por fecha:")
# for fecha in ventas_por_fecha:
#     print(f"Fecha: {fecha[0]}, Total Vendido: {fecha[1]}")

print("\nAnálisis de ventas:")


# #Producto más vendido
# print("\nProducto más vendido:")
# print(f"Producto: {producto_mas_vendido[0]}, Cantidad Vendida: {producto_mas_vendido[1]}")

# #Producto menos vendido
# print("\nProducto menos vendido:")
# print(f"Producto: {producto_menos_vendido[0]}, Cantidad Vendida: {producto_menos_vendido[1]}")

# #Producto que más ingresos generó
# print("\nProducto que más ingresos generó:")
# print(f"Producto: {producto_mas_ingresos[0]}, Ingresos: {producto_mas_ingresos[1]}")

# #Producto que menos ingresos generó
# print("\nProducto que menos ingresos generó:")
# print(f"Producto: {producto_menos_ingresos[0]}, Ingresos: {producto_menos_ingresos[1]}")

# #Porcentaje de ventas por categoría
# print("\nPorcentaje de ventas por categoría:")
# porcentaje_categoria = porcentaje_ventas_por_categoria()
# for categoria, porcentaje in porcentaje_categoria:
#     print(f"{categoria}: {porcentaje:.2f}%")

# #Promedio por venta
# promedio_por_venta = promedio_por_venta()
# print(f"\nPromedio por venta: ${promedio_por_venta:.2f}")

# #Categoría dominante
# categoria_dominante = categoria_dominante()
# print(f"\nCategoría dominante: {categoria_dominante[0]}, Generado: ${categoria_dominante[1]}")

#estadisticas
ventas = []
for venta in datos_ventas_por_categoria:
    venta_num = int(venta[1])
    ventas.append(venta_num)
np_ventas = np.array(ventas)

media_ventas = media(np_ventas)
mediana_ventas = mediana(np_ventas)
desviacion_ventas = desviacion_estandar(np_ventas)
valor_maximo_ventas = valor_maximo(np_ventas)
valor_minimo_ventas = valor_minimo(np_ventas)

print("\nEstadísticas de ventas por categoría:")
print(f"Media: {media_ventas:.2f}")
print(f"Mediana: {mediana_ventas:.2f}")
print(f"Desviación Estándar: {desviacion_ventas:.2f}")
print(f"Valor Máximo: {valor_maximo_ventas}")
print(f"Valor Mínimo: {valor_minimo_ventas}")
