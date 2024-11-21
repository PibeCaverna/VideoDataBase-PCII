from settings import *                              #importa todas las estructuras de opciones.py
import mysql.connector                              #biblioteca para conectar a servers mysql
from utils.kickstart import kickstart               #función para crear las tablas
from mysql.connector.errors import DatabaseError    #Error de base de datos para mysql

Dberror = False
print("conectando...")
try: conexion = mysql.connector.connect(**DBCREDENTIALS)
except DatabaseError: Dberror = True

if not(Dberror):
    print("conectado!")
    print("creando tablas")
    kickstart(conexion)
    conexion.close()
    print("Adios!")
else: print("error de conexión")
