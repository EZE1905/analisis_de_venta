import psycopg2

def conectar_base_datos():
    try:
        conexion = psycopg2.connect(
            database="sistema_ventas",
            user="postgres",
            password="ezesql",
            host="localhost",
            port="5432"
        )
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
    return conexion

def cerrar_conexion(conexion):
    if conexion:
        conexion.close()