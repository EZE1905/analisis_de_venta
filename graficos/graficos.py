import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from consultas import ventas_por_categoria,obtener_cantidad_de_productos_vendidos,ventas_por_fecha
from analisis.analisis import porcentaje_ventas_por_categoria

df = pd.DataFrame(ventas_por_categoria(), columns=["categoria", "total_vendido"])

# Crear un gráfico de barras para mostrar las ventas por categoría
sns.barplot(x="categoria", y="total_vendido", data=df)
plt.title("Ventas por Categoría")
plt.xlabel("Categoría")
plt.ylabel("Total Vendido")
plt.show()

# Crear un gráfico de pastel para mostrar el porcentaje de ventas por categoría

df_pie = pd.DataFrame(porcentaje_ventas_por_categoria(), columns=["categoria", "porcentaje"])
plt.pie(df_pie["porcentaje"], labels=df_pie["categoria"], autopct="%1.1f%%", startangle=140)
plt.title("Porcentaje de Ventas por Categoría")
plt.axis("equal")  # Para asegurar que el gráfico sea circular
plt.show()

# Crear un gráfico de barras para mostrar la cantidad de productos vendidos por producto
df_cantidad = pd.DataFrame(obtener_cantidad_de_productos_vendidos(), columns=["producto", "cantidad_vendida"])
sns.barplot(x="producto", y="cantidad_vendida", data=df_cantidad)
plt.title("Cantidad de Productos Vendidos por Producto")
plt.xlabel("Producto")
plt.ylabel("Cantidad Vendida")
plt.xticks(rotation=45)  # Rotar las etiquetas del eje x para mejor legibilidad
plt.show()

# Crear un gráfico de líneas para mostrar las ventas por fecha
df_fecha = pd.DataFrame(ventas_por_fecha(), columns=["fecha", "total_vendido"])
df_fecha["fecha"] = pd.to_datetime(df_fecha["fecha"])  # Convertir la columna de fecha a formato datetime
sns.lineplot(x="fecha", y="total_vendido", data=df_fecha)
plt.title("Ventas por Fecha")
plt.xlabel("Fecha")
plt.ylabel("Total Vendido")
plt.show()