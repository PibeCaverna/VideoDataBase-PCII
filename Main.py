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
from utils.sign_in import UIlogin                   #Función para logearse con tkinter              |
#---------------------------------------------------------------------------------------------------#
from mysql.connector.errors import DatabaseError    #Error de base de datos para mysql              |
#---------------------------------------------------------------------------------------------------#
Dberror = False
print("conectando...")
try: conexion = mysql.connector.connect(**DBCREDENTIALS)
except DatabaseError: Dberror = True

if Dberror == False:
    Ventana = Tk()
    Ventana.title("Notflix")
    Ventana.geometry("800x600")
    Perfiles = [(None,None),(None,None),(None,None),(None,None),(None,None),(None,None)]

    #Página de login
    Frame_login = Frame()
    logwidgets = (
                  Label(Frame_login,text="Ingreso",font=("Arial",30,"bold")),
                  Label(Frame_login,text="Correo electrónico: ",font=("Arial",16,"bold")),
                  Label(Frame_login,text="Contraseña:",font=("Arial",16,"bold")),
                  Entry(Frame_login,font=("Arial",16)),         #acá entra el email
                  Entry(Frame_login,show="*",font=("Arial",16)),#acá entra la contraseña
                  Button(Frame_login,
                         text="Ingresar",
                         command=UIlogin(logwidgets[3].get(),logwidgets[4].get(),Perfiles,conexion,Frame_login,Frame_Uselect),
                         font=("Arial",16,"bold"))
                )#Tupla con los widgets de la página de login
    
    logwidgets[0].grid(row=0,column=0,columnspan=2,sticky="news",pady=30)
    logwidgets[1].grid(row=1,column=0)
    logwidgets[2].grid(row=3,column=0)
    logwidgets[3].grid(row=2,column=0,pady=20)
    logwidgets[4].grid(row=4,column=0,pady=20)
    logwidgets[5].grid(row=5,column=0,columnspan=2,pady=30)
    
    #Selector de Usuarios
    Frame_Uselect = Frame()
    UselectWidget = (
                     Label(Frame_Uselect,text="Seleccione su Usuario",font=("Arial",30,"bold")),
                     Button(Frame_Uselect,text=Perfiles[0][1],command=print(Perfiles[0][0])),
                     Button(Frame_Uselect,text=Perfiles[1][1],command=print(Perfiles[1][0])),
                     Button(Frame_Uselect,text=Perfiles[2][1],command=print(Perfiles[2][0])),
                     Button(Frame_Uselect,text=Perfiles[3][1],command=print(Perfiles[3][0])),
                     Button(Frame_Uselect,text=Perfiles[4][1],command=print(Perfiles[4][0])),
                     Button(Frame_Uselect,text=Perfiles[5][1],command=print(Perfiles[5][0]))
                    )
    UselectWidget[0].grid(row=0,column=1)
    UselectWidget[1].grid(row=1,column=0)
    UselectWidget[2].grid(row=1,column=2)
    UselectWidget[3].grid(row=2,column=0)
    UselectWidget[4].grid(row=2,column=2)
    UselectWidget[5].grid(row=3,column=0)
    UselectWidget[6].grid(row=3,column=2)
 
    #Inicia el programa visual en la página de login
    Frame_login.pack()
    Ventana.mainloop()
