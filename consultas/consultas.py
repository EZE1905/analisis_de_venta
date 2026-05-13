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

def obtener_ventas():
    conexion = conectar_base_datos()
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT id,producto_id,cantidad,fecha FROM ventas")
        ventas = cursor.fetchall()
        return ventas
    finally:
        cerrar_conexion(conexion)

def obtener_cantidad_de_productos_vendidos():
    conexion = conectar_base_datos()
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT productos.nombre, SUM(ventas.cantidad) FROM ventas JOIN productos ON ventas.producto_id = productos.id GROUP BY productos.nombre")
        cantidad = cursor.fetchall()
        return cantidad
    finally:
        cerrar_conexion(conexion)

def obtener_precio_total_vendido():
    conexion = conectar_base_datos()
    cursor = conexion.cursor()
    try: 
        cursor.execute("SELECT productos.nombre, SUM(ventas.cantidad * productos.precio) FROM ventas JOIN productos ON ventas.producto_id = productos.id GROUP BY productos.nombre")
        total_vendido = cursor.fetchall()
        return total_vendido
    finally:        
        cerrar_conexion(conexion)

def producto_mas_vendido():
    conexion = conectar_base_datos()
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT productos.nombre, SUM(ventas.cantidad) AS total_vendido FROM ventas JOIN productos ON ventas.producto_id = productos.id GROUP BY productos.nombre ORDER BY total_vendido DESC LIMIT 1")
        producto_mas_vendido = cursor.fetchone()
        return producto_mas_vendido
    finally:
        cerrar_conexion(conexion)

def producto_menos_vendido():
    conexion = conectar_base_datos()
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT productos.nombre, SUM(ventas.cantidad) AS total_vendido FROM ventas JOIN productos ON ventas.producto_id = productos.id GROUP BY productos.nombre ORDER BY total_vendido ASC LIMIT 1")
        producto_menos_vendido = cursor.fetchone()
        return producto_menos_vendido
    finally:
        cerrar_conexion(conexion)

def producto_que_mas_ingresos_genero():
    conexion = conectar_base_datos()
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT productos.nombre, SUM(ventas.cantidad * productos.precio) AS ingresos FROM ventas JOIN productos ON ventas.producto_id = productos.id GROUP BY productos.nombre ORDER BY ingresos DESC LIMIT 1")
        producto_mas_ingresos = cursor.fetchone()
        return producto_mas_ingresos
    finally:
        cerrar_conexion(conexion)

def producto_que_menos_ingresos_genero():
    conexion = conectar_base_datos()
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT productos.nombre, SUM(ventas.cantidad * productos.precio) AS ingresos FROM ventas JOIN productos ON ventas.producto_id = productos.id GROUP BY productos.nombre ORDER BY ingresos ASC LIMIT 1")
        producto_menos_ingresos = cursor.fetchone()
        return producto_menos_ingresos
    finally:
        cerrar_conexion(conexion)

def cantidad_por_categoria():
    conexion = conectar_base_datos()
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT productos.categoria, SUM(ventas.cantidad) AS total_vendido FROM ventas JOIN productos ON ventas.producto_id = productos.id GROUP BY productos.categoria order by total_vendido desc")
        cantidad_por_categoria = cursor.fetchall()
        return cantidad_por_categoria
    finally:
        cerrar_conexion(conexion)

def ventas_por_categoria():
    conexion = conectar_base_datos()
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT productos.categoria, SUM(ventas.cantidad * productos.precio) AS total_vendido FROM ventas JOIN productos ON ventas.producto_id = productos.id GROUP BY productos.categoria order by total_vendido desc")
        ventas_por_categoria = cursor.fetchall()
        return ventas_por_categoria
    finally:
        cerrar_conexion(conexion)

def ventas_por_fecha():
    conexion = conectar_base_datos()
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT DATE(ventas.fecha), SUM(ventas.cantidad * productos.precio) AS total_vendido FROM ventas JOIN productos ON ventas.producto_id = productos.id GROUP BY DATE(ventas.fecha) order by total_vendido desc")
        ventas_por_fecha = cursor.fetchall()
        return ventas_por_fecha
    finally:
        cerrar_conexion(conexion)