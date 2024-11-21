from settings import *                              #importa todas las estructuras de opciones.py
import mysql.connector                              #Biblioteca para conectar a servers mysql
from utils.kickstart import kickstart               #Función para crear las tablas
from utils.querymakers import searchtitles          #Función para buscar series y pelis por título
from mysql.connector.errors import DatabaseError    #Error de base de datos para mysql

Dberror = False
print("conectando...")
try: conexion = mysql.connector.connect(**DBCREDENTIALS)
except DatabaseError: Dberror = True

if not(Dberror):
    print("conectado!")
    print("creando tablas")
    kickstart(conexion)
    print(searchtitles("Apa",conexion))
    conexion.close()
    print("Adios!")
else: print("error de conexión")
