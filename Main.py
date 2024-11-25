#---------------------------------------------------------------------------------------------------#
from settings import *                              #importa todas las estructuras de opciones.py   |
#---------------------------------------------------------------------------------------------------#
import mysql.connector                              #Biblioteca para conectar a servers mysql       |
from tkinter import *                               #Tkinter, para gui                              |
#---------------------------------------------------------------------------------------------------#
from utils.kickstart import kickstart               #Función para crear las tablas                  |
from utils.querymakers import searchtitles          #Función para buscar series y pelis por título  |
from utils.querymakers import abouttitle            #Función para buscar los datos de un título     |
from utils.querymakers import creditos              #Función para buscar los créditos de un título  |
#---------------------------------------------------------------------------------------------------#
from models.gui import InterfazUsuario              #Clase de la interfaz gráfica                   |
#---------------------------------------------------------------------------------------------------#
from mysql.connector.errors import DatabaseError    #Error de base de datos para mysql              |
#---------------------------------------------------------------------------------------------------#
Dberror = False
print("conectando...")
try: conexion = mysql.connector.connect(**DBCREDENTIALS)
except DatabaseError: Dberror = True

if Dberror == False:
    GUI = InterfazUsuario(conexion)
    GUI.startgui()
