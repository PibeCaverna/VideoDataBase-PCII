import mysql.connector

def kickstart(conexion):
    startup = ""
    kickfile = open("kickstart.sql","r")
    for line in kickfile:
        startup += (line)
    kickfile.close()
    startup = startup.split("#")
    with conexion.cursor() as cursor:
        for query in startup:
            cursor.execute(query)    
