import numpy as np

def media(informacion):
    media = np.mean(informacion)
    return media
def mediana(informacion):
    mediana = np.median(informacion)
    return mediana
def desviacion_estandar(informacion):
    desviacion_estandar = np.std(informacion)
    return desviacion_estandar
def valor_maximo(informacion):
    info_dominante = np.max(informacion)
    return info_dominante
def valor_minimo(informacion):
    info_menor = np.min(informacion)
    return info_menor
