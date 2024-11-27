import mysql.connector                              #biblioteca para conectar a servers mysql

def searchtitles(cadena,conexion, infante = 0):
    '''Dada una cadena, retorna un diccionario de ids de series o peliculas cuyo título la contiene
    Estructura -> {"movie" : <ids peliculas>, "serial" : <ids series>}'''
    filtroinfantil = ""
    if infante == 1: filtroinfantil = " AND atp = 1"
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

def abouttitle(id,conexion,tipo="g",infante = 0):
    '''dada una id, retorna un diccionario con toda la información relevante al tipo seleccionado
        TIPOS
            | g -> Genérico. nombre, descripcion 
            | p -> Película. agrega saga
            | s -> Serie. agrega cantidad de cápitulos
            | c -> Cápitulo. agrega serie y temporada 
    '''
    filtroinfantil = ""
    if infante == 1: filtroinfantil = " AND atp = 1"
    if tipo == "m":
        query = '''
                SELECT nombre_video, descripcion_video, nombre_saga, descripcion_saga 
                FROM Videos  NATURAL JOIN Peliculas NATURAL JOIN Sagas
                WHERE id_video = '''+str(id)+filtroinfantil
        with conexion.cursor() as cursor:
            cursor.execute(query)
            resultado = cursor.fetchall()
        return {"title" : resultado[0][0],         #Título de la peli
                "desc" : resultado[0][1],          #Descripción de la peli
                "saga" : resultado[0][2],          #Saga de la peli
                "sagadata" : resultado[0][3]}      #Descripción de la saga
    elif tipo == "s":
        query = '''
                SELECT nombre_serie, descripcion_serie, count(id_video) as capitulos
                FROM Series NATURAL JOIN Capitulos
                WHERE id_video = '''+str(id)+filtroinfantil+'''
                GROUP BY id_serie
                '''
        with conexion.cursor() as cursor:
            cursor.execute(query)
            resultado = cursor.fetchall()
        return {"title" : resultado[0][0],         #Título de la serie
                "desc" : resultado[0][1],          #Descripción de la serie
                "qcap" : resultado[0][2],}         #Cantidad de cápitulos de la serie
    elif tipo == "c":
        query = '''
                SELECT nombre_video, descripcion_video, temporada, nombre_serie
                FROM Videos NATURAL JOIN Capitulos NATURAL JOIN Series
                WHERE id_video = '''+str(id)+filtroinfantil
        with conexion.cursor() as cursor:
            cursor.execute(query)
            resultado = cursor.fetchall()
        return {"title" : resultado[0][0],         #Titulo del cápitulo
                "desc" : resultado[0][1],          #Descripción del cápitulo
                "season" : resultado[0][2],        #Temporada del cápitulo
                "s" : resultado[0][3]}             #Serie del cápitulo
    elif tipo == "g":
        query = '''
                SELECT nombre_video, descripcion_video
                FROM Videos
                WHERE id_video = '''+str(id)+filtroinfantil
        with conexion.cursor() as cursor:
            cursor.execute(query)
            resultado = cursor.fetchall()
        return {"title" : resultado[0][0],         #Título del video
                "desc" : resultado[0][1],}         #Descripciónd del video
    else: raise ValueError('Argumento de tipo incorrecto')

def creditos(id,conexion,tipo = "g"):
    ''' Dada una id para un tipo de contenido admitido, busca todos los créditos que le corresponden
    en un diccionario de claves Actores, Directores y Productores.
    los parámetros de tipo "g", "p" y "c" evaluan todos los videos
    el parámetro de tipo "s" evalua las series
    otros prámetros de tipo dan error de valor
    Salida:
    salida["Actores"][i] = (nombre_artista,apellido_artista,pseudonimo_artista,nombre_personaje)
    salida["Directores"][i] = (nombre_artista,apellido_artista,pseudonimo_artista)
    salida["Productores"][i] = (nombre_artista,apellido_artista,pseudonimo_artista)
    '''
    creditosretorno = {}
    if tipo in ["g","m","c"]:
        query = '''
                SELECT rol, nombre_artista, apellido_artista, pseudonimo_artista, nombre_personaje
                FROM Creditos NATURAL JOIN Artistas
                WHERE id_video = '''+id+'''
                GROUP BY rol
                '''
    elif tipo == "s":
        query = '''
                SELECT rol, nombre_artista, apellido_artista, pseudonimo_artista, nombre_personaje
                FROM Creditos NATURAL JOIN Artistas NATURAL JOIN Series
                WHERE id_serie = '''+id+'''
                GROUB BY rol
                '''
    else: raise ValueError('Argumento de tipo incorrecto')

    with conexion.cursor() as cursor:
        cursor.execute(query)
        rawcred = cursor.fetchall()
    for rol in rawcred():
        if rol[0][0] == "Actor":
            creditosretorno[rol[0][0]+"es"] = [persona[1:] for persona in rol]
        else: creditosretorno[rol[0][0]+"es"] = [persona[1:4] for persona in rol]

    return creditosretorno
