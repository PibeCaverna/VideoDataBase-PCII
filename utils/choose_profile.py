def choose_profile( id_u,conexion):
    Profiles = get_profiles( id_u,conexion)
    profil_choosen = Get_user_profile(Profiles)#esta funcion debe devolver la id del prefil seleccionado
    return profil_choosen #es la id del perfil elegido por el usuario

def get_profiles( id_u,conexion):#devuelve una lista con los nombres de cada perfil de una cuenta
    consulta = """Select nombre_perfil, id_perfil
                  From Usuarios U, Perfiles P 
                  Where U.id_usuario = P.id_usuario and P.id_usuario = %s"""

    with conexion.cursor() as cursor:
        cursor.execute(consulta , id_u)
    return cursor.fetchall()

def Get_user_profile(Profiles):
    print("ingrese el numero del perfil que quiera")
    for i in range(len(Profiles)):
        print(i,Profiles[i])
    return input()

