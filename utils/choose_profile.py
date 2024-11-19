def choose_profile(conexion, id_u)
    Profiles = get_profiles(conexion, id_u)



def get_profiles(conexion, id_u)
    consulta = """Select nombre_perfil, id_perfil
                  From Usuarios U, Perfiles P 
                  Where U.id_usuario = P.id_usuario and P.id_usuario = %s"""

    with conexion.cursor() as cursor:
    cursor.execute(consulta , id_u)
    return cursor.fetchall()
