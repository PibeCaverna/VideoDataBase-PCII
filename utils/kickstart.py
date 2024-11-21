import mysql.connector
from mysql.connector.errors import ProgrammingError

def kickstart(conexion):
    ''' Inicia todas las tablas de kickstart.sql, en caso de que no estén iniciadas.
    Retorna una lista ordenada de booleanos, donde falso indica una query que no se realizo.
    NO SE RECOMIENDA SU USO PARA OTRO TIPO DE QUERY, PUEDE RESULTAR EN CASOS INESPERADOS.'''
    startup = ""
    kickfile = open("kickstart.sql","r")
    sub1 = "CREATE TABLE "
    sub2 = "("
    #Agarra todas las querys de kickstart.sql y las mete en un string
    for line in kickfile:
        startup += (line)
    kickfile.close()
    #Separa todas las querys en una lista. Es importante agregar un # entre cada query para poder separarlas
    startup = startup.split("#")
    with conexion.cursor() as cursor:
        ecatch = []
        for query in startup:
             #le mandamos excepción para buscar un programming error, no se si es demasiado general
             #o si puede haber una solución más elegante
             try:
                cursor.execute(query)
             except ProgrammingError:
                ecatch.append(False)
             else:
                ecatch.append(True)
    return ecatch 
    #ecatch indica con False las tablas que no se crearon y con true las que se crearon
             
