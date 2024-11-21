import mysql.connector                              #biblioteca para conectar a servers mysql

def searchtitles(cadena,conexion, infante = False):
    '''Dada una cadena, retorna un diccionario de ids de series o peliculas cuyo título la contiene
    Estructura -> {"movie" : <ids peliculas>, "serial" : <ids series>}'''
    filtroinfantil = ""
    if infante: filtroinfantil = " atp = True"
    moviequery ='''
                SELECT id_video
                FROM Videos NATURAL JOIN Peliculas
                WHERE nombre_video LIKE '''+"\'"+cadena+"%\'"+filtroinfantil
    seriesquery ='''
                SELECT id_serie
                FROM Series
                WHERE nombre_serie LIKE '''+"\'"+cadena+"%\'"+filtroinfantil
    with conexion.cursor() as cursor:
        cursor.execute(moviequery)
        m = cursor.fetchall()
    with conexion.cursor() as cursor: #No se si es necesario. puede llegar a ser redundante
        cursor.execute(seriesquery)
        s = cursor.fetchall()
    return {"m" : m,
            "s" : s}

def abouttitle(id,conexion,tipo="g",infante = False):
    '''dada una id, retorna un diccionario con toda la información relevante al tipo seleccionado
        TIPOS
            | g -> Genérico. nombre, descripcion 
            | p -> Película. agrega saga
            | s -> Serie. agrega cantidad de cápitulos
            | c -> Cápitulo. agrega serie y temporada 
    '''
    filtroinfantil = ""
    if infante: filtroinfantil = " atp = True"
    if tipo == "p":
        query = '''
                SELECT nombre_video descripcion_video nombre_saga descripcion_saga 
                FROM Videos  NATURAL JOIN Peliculas NATURAL JOIN Sagas
                WHERE id_video = '''+id+filtroinfantil
        with conexion.cursor() as cursor:
            cursor.execute(query)
            resultado = cursor.fetchall()
        return {"title" : resultado[0],         #Título de la peli
                "desc" : resultado[1],          #Descripción de la peli
                "saga" : resultado[2],          #Saga de la peli
                "sagadata" : resultado[3]}      #Descripción de la saga
    elif tipo == "s":
        query = '''
                SELECT nombre_serie descripcion_serie count(id_video) as capitulos
                FROM Series NATURAL JOIN Capitulos
                WHERE id_serie = '''+id++filtroinfantil'''
                GROUP BY id_serie
                '''
        with conexion.cursor() as cursor:
            cursor.execute(query)
            resultado = cursor.fetchall()
        return {"title" : resultado[0],         #Título de la serie
                "desc" : resultado[1],          #Descripción de la serie
                "qcap" : resultado[2],}         #Cantidad de cápitulos de la serie
    elif tipo == "c":
        query = '''
                SELECT nombre_video descripcion_video temporada nombre_serie
                FROM Videos NATURAL JOIN Capitulos NATURAL JOIN Series
                WHERE id_video = '''+id+filtroinfantil
        with conexion.cursor() as cursor:
            cursor.execute(query)
            resultado = cursor.fetchall()
        return {"title" : resultado[0],         #Titulo del cápitulo
                "desc" : resultado[1],          #Descripción del cápitulo
                "season" : resultado[2],        #Temporada del cápitulo
                "s" : resultado[3]}             #Serie del cápitulo
    elif tipo == "g":
        query = '''
                SELECT nombre_video descripcion_video
                FROM Videos
                WHERE id_video = '''+id+filtroinfantil
        with conexion.cursor() as cursor:
            cursor.execute(query)
            resultado = cursor.fetchall()
        return {"title" : resultado[0],         #Título del video
                "desc" : resultado[1],}         #Descripciónd del video
    else: raise ValueError('Argumento de tipo incorrecto')

#def credits(id,conexion,tipo = "g"):
#    if tipo in ["g","p","c"]:
#        query = '''
#                SELECT rol nombre_artista 
#                '''
