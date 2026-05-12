from database.conexion import conectar_base_datos, cerrar_conexion

def obtener_productos():
    conexion = conectar_base_datos()
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT id,nombre,precio FROM productos")
        productos = cursor.fetchall()
        return productos
    finally:
        cerrar_conexion(conexion)
