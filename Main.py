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
    
    #Página de login
    Frame_login = Frame()
    
    Label_titu = Label(Frame_login,text="Ingreso",font=("Arial",30,"bold")) 
    Label_mail = Label(Frame_login,text="Correo electrónico: ",font=("Arial",16,"bold")) 
    Label_pass = Label(Frame_login,text="Contraseña:",font=("Arial",16,"bold")) 
    Entry_mail = Entry(Frame_login,font=("Arial",16))
    Entry_pass = Entry(Frame_login,show="*",font=("Arial",16))
    BotonLogin = Button(Frame_login,
                        text="Ingresar",
                        command=lambda:print(UIlogin(Entry_mail.get(),Entry_pass.get(),conexion)),
                        font=("Arial",16,"bold"))
    
    Label_titu.grid(row=0,column=0,columnspan=2,sticky="news",pady=30)
    Label_mail.grid(row=1,column=0)
    Label_pass.grid(row=3,column=0)
    Entry_mail.grid(row=2,column=0,pady=20)
    Entry_pass.grid(row=4,column=0,pady=20)
    BotonLogin.grid(row=5,column=0,columnspan=2,pady=30)
    
    Frame_login.pack()
    #Página de login, ver como destruirla a posteriori
    Ventana.mainloop()
