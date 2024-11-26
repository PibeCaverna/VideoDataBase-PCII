

def Sections(id_profile,conexion):
    pelis_no_terminadas, series_no_terminadas =  Get_videos_no_finalizados(id_profile,conexion)

    return get_pelis_name(pelis_no_terminadas, conexion), series_no_terminadas(id_series, conexion)



def Get_videos_no_finalizados(id_profile,conexion):

    #obtengo todas las peliculas sin terminar
    consulta_pelis = """Select id_video 
                        From Videos V, Perfiles Pe, Peliculas M, Progresos Pr  
                        Where %s = Pr.id_perfil and Pr.id_video = V.id_video and and V.id_video = M.id_video and Pr.tiempo_progreso < 100 and Pr.tiempo_progreso > 0"""
    #obtengo todas las series de las que todabia falta terminar algun capitulo
    consulta_cap_por_terminar = """Select id_Series
                                    From Videos V, Perfiles Pe, Capitulos C, Progresos Pr, Series S  
                                    Where %s = Pr.id_perfil and Pr.id_video = V.id_video and V.id_video = C.id_video and C.id_serie = S.id_serie and Pr.tiempo_progreso < 100 and Pr.tiempo_progreso > 0"""
    #devuelve las id de todas las series vistas
    consulta_serie_por_terminar = """Select Distinct id_Series
                  From Videos V, Perfiles Pe, Capitulos C, Progresos Pr, Series S  
                  Where %s = Pr.id_perfil and Pr.id_video = V.id_video and V.id_video = C.id_video and C.id_serie = S.id_serie"""
    #devuelve el progreso del ultimo capitulo de una serie
    consulta_ultimo_cap = """Select Pr.progreso 
                            From Videos V, Perfiles Pe, Capitulos C, Progresos Pr, Series S  
                            Where %s = Pr.id_perfil and Pr.id_video = V.id_video and V.id_video = C.id_video and C.id_serie = S.id_serie and C.id_serie = %s
                            Order by C.temporada DES, C.num_capitulo DES
                            Limit 1
                            """
                             

    
    with conexion.cursor() as cursor:
        cursor.execute(consulta_pelis , (id_profile,))
        pelis = cursor.fetchall()

        cursor.execute(consulta_cap_por_terminar , (id_profile,))
        caps = cursor.fetchall()

        cursor.execute(consulta_serie_por_terminar , (id_profile,))
        series_vistas = cursor.fetchall()

        series_por_terminar = []
        for x in series_vistas: #para cada serie que fue vista, se fija si el ultimo capitulo de esta fue terminado
            cursor.execute(consulta_ultimo_cap , (id_profile, x))
            last_cap = cursor.fetchall()

            if last_cap != 100 and x not in caps: #si el ultimo cap de una serie vista no esta terminado guarda el id de la serie si
                                                  #este no esta ya guardad en la lista de caps
                series_por_terminar.append(x)

        return (pelis, caps + series_por_terminar)


def get_pelis_name(id_pelis, conexion):

    consulta = """Select nombre_video
                  From Videos 
                  Where %s = id_video
                """

    names = []
    with conexion.cursor() as cursor:
        for peli in id_pelis:
           cursor.execute(consulta , (peli,))
           names.append(cursor.fetchall())
    return names

def get_series_name(id_series, conexion):

    consulta = """SELECT nombre_serie
                  FROM  Series 
                  WHERE %s = id_serie
                """

    names = []
    with conexion.cursor() as cursor:
        for serie in id_series:
           cursor.execute(consulta , (serie,))
           names.append(cursor.fetchall())
    return names


