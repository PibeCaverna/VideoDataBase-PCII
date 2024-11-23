import mysql.connector
#de no hacer el programa en consola no usar la funcion sign_in(conexion) y llamar directamente a autentification
def Sign_in(conexion):

    Email = input("Enter Email: ")
    password = input("Password: ")
    id_user = Autentification(Email, password,conexion)
    #aca deberia manejar los erroes
    
    return id_user


def Autentification(Email,password,conexion):
    if(Email != "" and password != ""):
        tup = user_exist(Email,conexion) #si el numbre de usuario existe devuelve el id y la contrasenia del usuario registrado en la tabla
                                                         #si no existe devuelve false o vacio
        if tup is None: raise ValueError('Cuenta inexistente')
        _id = tup[0]
        user_password = tup[1]
        query = ''' 
                INSERT
                INTO Autenticaciones(id_usuario,success)
                VALUES (%s,%s)
                '''
        if user_password == password:               #Si el logeo es exitoso
            with conexion.cursor() as cursor:
                cursor.execute(query,(_id,True))    #guardo la auth como correcta
            return _id                              #devuelvo el id de usuario
        else:                                       #Si el logeo no es exitoso
            with conexion.cursor() as cursor:       
                cursor.execute(query,(_id,False))   #guardo la auth como incorrecta
            return None                             #no devuelvo nada

def user_exist(Email,conexion):#hace la quary en la lista de usuarios y consigue la id de ese usuario y su contrasenia
    consulta =  '''
                SELECT id_usuario, password
                FROM Usuarios
                Where e_mail = '''+"\'"+Email+"\'"
    with conexion.cursor() as cursor:
        cursor.execute(consulta)
        tup = cursor.fetchone()
    return tup

def UIlogin(Mail,Pass,conexion):
    '''Corre la función Autentification, de forma tal que se pueda procesar con un botón de tkinter'''
    try: resultado = Autentification(Mail,Pass,conexion)
    except ValueError: return("Error: No existe el usuario")
    if resultado is None: return("Error, Contraseña incorrecta")
    else: return resultado
    
