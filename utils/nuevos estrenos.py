#Devuelve las series que y peliculas que fueron agregadas hace menos de 15 dias
#Toma 5 de cada una, luego se decide cuales se muestran
def get_producciones_receintes(conexion)
    pelis = get_pelis_recientes()
    series = get_series_recientes()


    return pelis, series

#devuelve las pelis que fueron agregadas hace menos de 15 dias
def get_pelis_recientes(conexion)   
    consulta = """
        SELECT * 
        FROM Peliculas
        WHERE fecha_agreg_peli >= CURDATE() - INTERVAL 15 DAY
        Limit 5
    """

    with conexion.cursor() as cursor:
        cursor.execute(consulta)
    return cursor.fetchall()

#devuelve las series que fueron agregadas hace menos de 15 dias
def get_series_recientes(conexion)

    consulta = """
        SELECT * 
        FROM Series
        WHERE fecha_agreg_serie >= CURDATE() - INTERVAL 15 DAY
        Limit 5
    """

    with conexion.cursor() as cursor:
        cursor.execute(consulta)
    return cursor.fetchall()