import mysql.connector
#de no hacer el programa en consola no usar la funcion sign_in(conexion) y llamar directamente a autentification
def Sign_in(conexion):

    Email = input("Enter Email: ")
    password = input("Password: ")
    id_user = Autentification(Email, password,conexion)
    #aca deberia manejar los erroes
    
    return id_user

def Autentification( Email, password,conexion):

    _id, user_password = user_exist( Email,conexion) #si el numbre de usuario existe devuelve el id y la contrasenia del usuario registrado en la tabla
                                                     #si no existe devuelve false o vacio
    if user_password = password
        return _id

    #falta lanzar una exepcion si la contrasenia no corresponde y agregar la hora del intento de logeo, si fue exitoso o fallido,
    # y aumntar ek numero de intentos de logeos a la cuenta

def user_exist( Email,conexion):#hace la quary en la lista de usuarios y consigue la id de ese usuario y su contrasenia
                               #si el usuario no existe lanza una exepcion
    consulta = """Select id_usuario, password
                  From Usuarios 
                  Where E_mail = %s"""

    with conexion.cursor() as cursor:
        cursor.execute(consulta , Email)
    
    return cursor.fetchone()





