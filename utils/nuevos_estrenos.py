#Devuelve las series que y peliculas que fueron agregadas hace menos de 15 dias
#Toma 5 de cada una, luego se decide cuales se muestran
def get_producciones_recientes(conexion):
    pelis = get_pelis_recientes(conexion)
    series = get_series_recientes(conexion)


    return pelis, series

#devuelve las pelis que fueron agregadas hace menos de 15 dias
def get_pelis_recientes(conexion):   
    consulta = """
        SELECT id_video, nombre_video 
        FROM Peliculas NATURAL JOIN Videos
        WHERE fecha_agreg_peli >= CURDATE() - INTERVAL 15 DAY
        Limit 5
    """

    with conexion.cursor() as cursor:
        cursor.execute(consulta)
        resultado = cursor.fetchall()
    return resultado

#devuelve las series que fueron agregadas hace menos de 15 dias
def get_series_recientes(conexion):

    consulta = """
        SELECT id_serie, nombre_serie 
        FROM Series
        WHERE fecha_agreg_serie >= CURDATE() - INTERVAL 15 DAY
        Limit 5
    """

    with conexion.cursor() as cursor:
        cursor.execute(consulta)
        resultado = cursor.fetchall()
    return resultado
