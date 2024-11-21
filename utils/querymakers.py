import mysql.connector                              #biblioteca para conectar a servers mysql

def searchtitles(cadena,conexion):
    '''Dada una cadena, retorna un diccionario de ids de series o peliculas cuyo título la contiene
    Estructura -> {"movie" : <ids peliculas>, "serial" : <ids series>}'''
    moviequery ='''
                SELECT id_video
                FROM Videos NATURAL JOIN Peliculas
                WHERE nombre_video LIKE '''+"\'"+cadena+"%\'"
    seriesquery ='''
                SELECT id_serie
                FROM Series
                WHERE nombre_serie LIKE '''+"\'"+cadena+"%\'"
    with conexion.cursor() as cursor:
        cursor.execute(moviequery)
        m = cursor.fetchall()
        cursor.execute(seriesquery)
        s = cursor.fetchall()
    return {"movie" : m,
            "serie" : s}
