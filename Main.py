from settings import *
import mysql.connector
from utils.kickstart import kickstart

conexion = mysql.connector.connect(**DBCREDENTIALS)
print ("Conectado: ", conexion.is_connected())
ecatch = kickstart(conexion)

conexion.close()

