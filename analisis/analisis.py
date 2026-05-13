import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from database.conexion import conectar_base_datos, cerrar_conexion
from consultas import ventas_por_categoria

def porcentaje_ventas_por_categoria():
    ventas_categoria = ventas_por_categoria()
    total_ventas = sum(venta[1] for venta in ventas_categoria)
    porcentaje = [(categoria[0], (categoria[1] / total_ventas) * 100) for categoria in ventas_categoria]
    return porcentaje

def promedio_por_venta():
    conexion = conectar_base_datos()
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT AVG(ventas.cantidad * productos.precio) FROM ventas JOIN productos ON ventas.producto_id = productos.id")
        promedio = cursor.fetchone()[0]
        return promedio
    finally:
        cerrar_conexion(conexion)

def categoria_dominante():
    ventas_categoria = ventas_por_categoria()
    categoria_dominante = max(ventas_categoria, key=lambda x: x[1])
    return categoria_dominante

