

def Sections(id_profile,conexion):
    No_terminadas =  Get_videos_no_finalizados(id_profile,conexion)



def Get_videos_no_finalizados(id_profile,conexion):

    #obtengo todas las peliculas sin terminar
    consulta_pelis = """Select id_pelicula 
                  From Videos V, Perfiles Pe, Peliculas M, Progreso Pr  
                  Where %s = Pr.id_perfil and Pr.id_video = V.id_videoand and V.id_video = M.id_video and Pr.progreso < 100 and Pr.progreso > 0"""
    #obtengo todas las series de las que todabia falta terminar algun capitulo
    consulta_cap_por_terminar = """Select id_Series
                  From Videos V, Perfiles Pe, Capitulos C, Progreso Pr, Series S  
                  Where %s = Pr.id_perfil and Pr.id_video = V.id_video and V.id_video = C.id_video and C.id_serie = S.id_serie and Pr.progreso < 100 and Pr.progreso > 0"""

    consulta_serie_por_terminar = """Select Distinct id_Series
                  From Videos V, Perfiles Pe, Capitulos C, Progreso Pr, Series S  
                  Where %s = Pr.id_perfil and Pr.id_video = V.id_video and V.id_video = C.id_video and C.id_serie = S.id_serie"""

    consulta_ultimo_cap = """Select Pr.progreso 
                            From Videos V, Perfiles Pe, Capitulos C, Progreso Pr, Series S  
                            Where %s = Pr.id_perfil and Pr.id_video = V.id_video and V.id_video = C.id_video and C.id_serie = S.id_serie and C.id_serie = %s
                            Order by C.temporada DES, C.num_capitulo DES
                            Limit 1
                            """
                             

  #  consulta__Pelis = """Select id_video
  #                       From Perfiles Pe, Peliculas M, Videos V, Progreso Pr 
  #                       Where Pe.id_perfil = Pr.id_perfil and = Pr.id_video = V.id_video and V.id_video = M.id_video"""

    
    with conexion.cursor() as cursor:
        cursor.execute(consulta_pelis , id_profile)
        pelis = cursor.fetchall()
        cursor.execute(consulta_cap_por_terminar , id_profile)
        caps = cursor.fetchall()
        cursor.execute(consulta_serie_por_terminar , id_profile)
        series_vistas = cursor.fetchall()
        series_por_terminar = []
        for x in series_vistas:
            cursor.execute(consulta_ultimo_cap , id_profile, x)
            last_cap = cursor.fetchall()

            if last_cap != 100 and x not in caps: #si el ultimo cap de una serie vista no esta terminado guarda el id d la serie, si
                                                  #esta no esta ya guardad en la lista de caps
                series_por_terminar.append(x)

        return (pelis, )






