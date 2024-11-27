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
from utils.secciones import Get_videos_no_finalizados


class InterfazUsuario:
    def __init__(self,conexion):
        #Ventana principal
        self._VentanaRaiz   = Tk()
        self._VentanaRaiz.geometry("800x600")
        #Datos a usar
        self._incompleteseries = []
        self._incompletemovies = []
        self._currentProfile = None
        self._esinfante = None
        #Frames a usar
        self._FrameLogin    = Frame()
        self._FrameUselect  = Frame()
        self._PFrame        = Frame()   #Frame Padre a la UI del servicio
        self._FrameSearch   = LabelFrame(self._PFrame,width=400,height=300,relief="sunken",font=("Arial",30,"bold"),text="Busqueda")
        self._FrameMpage    = LabelFrame(self._PFrame,width=400,height=300,relief="solid" ,font=("Arial",30,"bold"),text="Inicio")
        self._FrameData     = LabelFrame(self._PFrame,width=800,height=300,relief="sunken",font=("Arial",30,"bold"),text="Detalles")
        #la conexion
        self._conexion      = conexion
        #widgets
        self._logwidgets    = ( Label(self._FrameLogin,justify="center",text="Ingreso",font=("Arial",30,"bold")),
                                Label(self._FrameLogin,justify="center",text="Correo electrónico: ",font=("Arial",16,"bold")),
                                Label(self._FrameLogin,justify="center",text="Contraseña:",font=("Arial",16,"bold")),
                                Entry(self._FrameLogin,font=("Arial",16)),         #acá entra el email
                                Entry(self._FrameLogin,show="*",font=("Arial",16)),#acá entra la contraseña
                                Button( self._FrameLogin,
                                        text="Ingresar",
                                        command=self.LoginHandler,
                                        font=("Arial",16,"bold")))
        self.UselectWidget = ()
        self.MenuWidgets = ()
        self.SearchWidgets = ()

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
        '''Maneja el proceso de iniciar sesión mediante una gui, si la cuenta no existe o la 
        contraseña es incorrecta, salta una ventana con la notificación correspondiente.
        La creación de cuentas mediante la app queda fuera del scope del proyecto'''
        try: resultado = Autentification(self._logwidgets[3].get(),self._logwidgets[4].get(),self._conexion)
        except ValueError: messagebox.showinfo("Usuario Inexistente","Contacte a su administrador")
        if resultado is None: messagebox.showinfo("Error", "Contraseña incorrecta")
        else:
            Perfiles = fetchprofiles(resultado,self._conexion)
            self.UselectWidget = (
                             Label(self._FrameUselect,justify="center",text="Seleccione su Usuario",font=("Arial",30,"bold")),
                             Button(self._FrameUselect,text=Perfiles[0][1],font=("Arial",20,"bold"),command=(lambda: self.pfp(Perfiles[0][0],Perfiles[0][0]))),
                             Button(self._FrameUselect,text=Perfiles[1][1],font=("Arial",20,"bold"),command=(lambda: self.pfp(Perfiles[1][0],Perfiles[1][0]))),
                             Button(self._FrameUselect,text=Perfiles[2][1],font=("Arial",20,"bold"),command=(lambda: self.pfp(Perfiles[2][0],Perfiles[2][0]))),
                             Button(self._FrameUselect,text=Perfiles[3][1],font=("Arial",20,"bold"),command=(lambda: self.pfp(Perfiles[3][0],Perfiles[3][0]))),
                             Button(self._FrameUselect,text=Perfiles[4][1],font=("Arial",20,"bold"),command=(lambda: self.pfp(Perfiles[4][0],Perfiles[4][0]))),
                             Button(self._FrameUselect,text=Perfiles[5][1],font=("Arial",20,"bold"),command=(lambda: self.pfp(Perfiles[5][0],Perfiles[5][0])))
                            )
            self.UselectWidget[0].grid(row=0,column=0,columnspan=2)
            self.UselectWidget[1].grid(row=1,column=0)
            self.UselectWidget[2].grid(row=1,column=1)
            self.UselectWidget[3].grid(row=2,column=0)
            self.UselectWidget[4].grid(row=2,column=1)
            self.UselectWidget[5].grid(row=3,column=0)
            self.UselectWidget[6].grid(row=3,column=1)
            
            self._FrameLogin.pack_forget()
            self._FrameUselect.pack()
            return None

    def pfp(self,id_perfil,esinfante):
        '''Clavo la busqueda, los  vistos recientemente y la data extra en la misma pantalla.
        Queda medio amontonado, pero es funcional'''
        if id_perfil is None: return None   #La creación de perfiles desde la app se encuentra
        else:                               #fuera del scope del proyecto
            self._currentProfile = id_perfil
            self._esinfante = esinfante
            self._FrameUselect.pack_forget()
            
            self._FrameMpage.grid(row=0,column=0)
            self._FrameSearch.grid(row=0,column=1)
            self._FrameData.grid(row=1,column=0,columnspan=2)

            #self._incompleteseries , self._incompletemovies = Get_videos_no_finalizados(id_perfil,self._conexion)
            self._incompleteseries = ["Dexter","Breaking Bad","Floricienta","Masha y el Oso","Vikingos","Afuera"]
            self._incompletemovies = ["Matrix","Frozen","Sonic","Minecraft","Esperando la carroza","Afuera"]

            #Widgets del menú principal
            self.MenuWidgets =( Label(self._FrameMpage,font=("Arial",20,"bold"),text="Continuar Series:"),
                                Listbox(self._FrameMpage,font=("Arial",20,"bold"),height=5),
                                Label(self._FrameMpage,font=("Arial",20,"bold"),text="Continuar Peliculas: "),
                                Listbox(self._FrameMpage,font=("Arial",20,"bold"),height=5),
                            )

            for i in range(5):
                self.MenuWidgets[1].insert(i,self._incompleteseries[i])
                self.MenuWidgets[3].insert(i,self._incompletemovies[i])
            
            self.MenuWidgets[0].grid(row=0,column=0)
            self.MenuWidgets[1].grid(row=1,column=0)
            self.MenuWidgets[2].grid(row=2,column=0)
            self.MenuWidgets[3].grid(row=3,column=0)
            
            #Widgets del menú de busqueda
            self.SearchWidgets = (  
                                    Entry(self._FrameSearch,font=("Arial",20)),
                                    Button(self._FrameSearch,font=("Arial",20,"bold"),text="〇",command=self.search),
                                    Listbox(self._FrameSearch,font=("Arial",20))
                                  )
                             
            self.SearchWidgets[0].grid(row=0,column=0)
            self.SearchWidgets[1].grid(row=0,column=1)
            self.SearchWidgets[2].grid(row=1,column=0)

            self._PFrame.pack()
            
        print(id_perfil)
    
    def search():
        self.SearchWidgets[3].insert(1,"pepe")
        return None
