

def Sections(id_profile,conexion):
    pelis_no_terminadas, series_no_terminadas = Get_videos_no_finalizados(id_profile, conexion)

    # Obtener nombres de películas y series con el formato "[id]-nombre"
    pelis_formateadas = [f"[{id_peli[0]}]-{get_pelis_name([id_peli], conexion)[0][0][0]}" for id_peli in pelis_no_terminadas]
    series_formateadas = [f"[{id_serie[0]}]-{get_series_name([id_serie], conexion)[0][0][0]}" for id_serie in series_no_terminadas]
    print(pelis_formateadas,series_formateadas)
    return pelis_formateadas, series_formateadas



def Get_videos_no_finalizados(id_profile,conexion):

    #obtengo todas las peliculas sin terminar
    consulta_pelis = """Select V.id_video 
                        from Videos V natural join Peliculas M natural join Progresos Pr natural join Perfiles Pe
                        Where Pe.id_perfil = %d and Pr.progreso < 100 and Pr.progreso > 0"""
    #obtengo todas las series de las que todabia falta terminar algun capitulo
    consulta_cap_por_terminar = """Select S.id_serie
                                    From Videos V natural join Perfiles Pe natural join Capitulos C natural join Progresos Pr natural join Series S  
                                    Where %d = Pe.id_perfil and Pr.progreso < 100 and Pr.progreso > 0"""
    #devuelve las id de todas las series vistas
    consulta_serie_por_terminar = """Select Distinct S.id_serie
                  From Videos V natural join Perfiles Pe natural join Capitulos C natural join Progresos Pr natural join Series S  
                  Where %d = Pe.id_perfil"""
    #devuelve el progreso del ultimo capitulo de una serie dada
    consulta_ultimo_cap = """Select Pr.progreso, C.temporada, C.num_capitulo
                            From Videos V natural join Perfiles Pe natural join Capitulos C natural join Progresos Pr natural join Series S  
                            Where %d = Pe.id_perfil and C.id_serie = %d
                            Order by C.temporada DESC, C.num_capitulo DESC
                            Limit 1
                            """
                             

    
    with conexion.cursor() as cursor:
        cursor.execute(consulta_pelis % (id_profile))
        pelis = cursor.fetchall()

        cursor.execute(consulta_cap_por_terminar % (id_profile))
        caps = cursor.fetchall()

        cursor.execute(consulta_serie_por_terminar % (id_profile))
        series_vistas = cursor.fetchall()

        series_por_terminar = []
        for x in series_vistas: #para cada serie que fue vista, se fija si el ultimo capitulo de esta fue terminado
            cursor.execute(consulta_ultimo_cap % (id_profile, x[0]))
            last_cap = cursor.fetchall()
            if last_cap != 100 and x not in caps: #si el ultimo cap de una serie vista no esta terminado guarda el id de la serie si
                                                  #este no esta ya guardad en la lista de caps
                series_por_terminar.append(x[0])
        print(caps)
        print(pelis)
        return (pelis, caps + series_por_terminar)


def get_pelis_name(id_pelis, conexion):#devuelve una lista con el nombre de todas las palis dentro de id_pelis

    consulta = """Select nombre_video
                  From Videos 
                  Where %s = id_video
                """

    names = []
    with conexion.cursor() as cursor:
        for peli in id_pelis:
           cursor.execute(consulta , peli)
           names.append(cursor.fetchall())
    return names

def get_series_name(id_series, conexion):#devuelve una lista con el nombre de todas las series dentro de id_series

    consulta = """SELECT nombre_serie
                  FROM  Series 
                  WHERE %s = id_serie
                """

    names = []
    with conexion.cursor() as cursor:
        for serie in id_series:
           cursor.execute(consulta , serie)
           names.append(cursor.fetchall())
    return names


