import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from consultas import ventas_por_categoria

df = pd.DataFrame(ventas_por_categoria(), columns=["categoria", "total_vendido"])

# Crear un gráfico de barras para mostrar las ventas por categoría
sns.barplot(x="categoria", y="total_vendido", data=df)
plt.title("Ventas por Categoría")
plt.xlabel("Categoría")
plt.ylabel("Total Vendido")
plt.show()
