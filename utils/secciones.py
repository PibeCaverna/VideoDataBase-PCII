

def Sections(id_profile,conexion):
    No_terminadas =  Get_videos_no_finalizados(id_profile,conexion)



def Get_videos_no_finalizados(id_profile,conexion):
    consulta = """Select nombre_perfil, id_perfil
                  From Usuarios U, Perfiles P 
                  Where U.id_usuario = P.id_usuario and P.id_usuario = %s"""

    with conexion.cursor() as cursor:
        cursor.execute(consulta , id_profile)
    return cursor.fetchall()

