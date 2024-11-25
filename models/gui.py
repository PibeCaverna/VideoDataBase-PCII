import mysql.connector                              #Biblioteca para conectar a servers mysql       |
from tkinter import *                               #Tkinter, para gui                              |
from tkinter import messagebox                      #Para ventanas popup                            |
#---------------------------------------------------------------------------------------------------#
from utils.kickstart import kickstart               #Función para crear las tablas                  |
from utils.querymakers import searchtitles          #Función para buscar series y pelis por título  |
from utils.querymakers import abouttitle            #Función para buscar los datos de un título     |
from utils.querymakers import creditos              #Función para buscar los créditos de un título  |
from utils.sign_in import Autentification
from utils.sign_in import fetchprofiles


class InterfazUsuario:
    def __init__(self,conexion):
        #Ventana principal
        self._VentanaRaiz   = Tk()
        #Frames a usar
        self._FrameLogin    = Frame()
        self._FrameUselect  = Frame()
        self._FrameSearch   = Frame()
        self._FrameMpage    = Frame()
        self._FrameData     = Frame()
        #la conexion
        self._conexion      = conexion
        #widgets
        self._logwidgets    = ( Label(self._FrameLogin,text="Ingreso",font=("Arial",30,"bold")),
                                Label(self._FrameLogin,text="Correo electrónico: ",font=("Arial",16,"bold")),
                                Label(self._FrameLogin,text="Contraseña:",font=("Arial",16,"bold")),
                                Entry(self._FrameLogin,font=("Arial",16)),         #acá entra el email
                                Entry(self._FrameLogin,show="*",font=("Arial",16)),#acá entra la contraseña
                                Button( self._FrameLogin,
                                        text="Ingresar",
                                        command=self.LoginHandler,
                                        font=("Arial",16,"bold")))

    def startgui(self):
        self._logwidgets[0].grid(row=0,column=0)
        self._logwidgets[1].grid(row=1,column=0)
        self._logwidgets[2].grid(row=3,column=0)
        self._logwidgets[3].grid(row=2,column=0)
        self._logwidgets[4].grid(row=4,column=0)
        self._logwidgets[5].grid(row=5,column=0)
        self._FrameLogin.pack()
        self._VentanaRaiz.mainloop()

    def LoginHandler(self):
        try: resultado = Autentification(self._logwidgets[3].get(),self._logwidgets[4].get(),self._conexion)
        except ValueError: messagebox.showinfo("Usuario Inexistente","Contacte a su administrador")
        if resultado is None: messagebox.showinfo("Error", "Contraseña incorrecta")
        else:
            Perfiles = fetchprofiles(resultado,self._conexion)
            UselectWidget = (
                             Label(self._FrameUselect,text="Seleccione su Usuario",font=("Arial",30,"bold")),
                             Button(self._FrameUselect,text=Perfiles[0][1],command=(lambda: self.pfp(Perfiles[0][0]))),
                             Button(self._FrameUselect,text=Perfiles[1][1],command=(lambda: self.pfp(Perfiles[1][0]))),
                             Button(self._FrameUselect,text=Perfiles[2][1],command=(lambda: self.pfp(Perfiles[2][0]))),
                             Button(self._FrameUselect,text=Perfiles[3][1],command=(lambda: self.pfp(Perfiles[3][0]))),
                             Button(self._FrameUselect,text=Perfiles[4][1],command=(lambda: self.pfp(Perfiles[4][0]))),
                             Button(self._FrameUselect,text=Perfiles[5][1],command=(lambda: self.pfp(Perfiles[5][0])))
                            )
            UselectWidget[0].grid(row=0,column=1)
            UselectWidget[1].grid(row=1,column=0)
            UselectWidget[2].grid(row=1,column=2)
            UselectWidget[3].grid(row=2,column=0)
            UselectWidget[4].grid(row=2,column=2)
            UselectWidget[5].grid(row=3,column=0)
            UselectWidget[6].grid(row=3,column=2)
            
            self._FrameLogin.pack_forget()
            self._FrameUselect.pack()
            return None
    def pfp(self,id_perfil):
        print(id_perfil)

