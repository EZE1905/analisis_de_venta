from consultas import ventas_por_categoria
import numpy as np

ventas_por_categoria = ventas_por_categoria()
ventas = []
for venta in ventas_por_categoria:
    venta_num = int(venta[1])
    ventas.append(venta_num)
    np_ventas = np.array(ventas)

def media(informacion):
    media = np.mean(informacion)
    return media
def mediana(informacion):
    mediana = np.median(informacion)
    return mediana
def desviacion_estandar(informacion):
    desviacion_estandar = np.std(informacion)
    return desviacion_estandar
def dominante(informacion):
    categoria_dominante = np.max(informacion)
    return categoria_dominante
def categoria_menor(informacion):
    categoria_menor = np.min(informacion)
    return categoria_menor
