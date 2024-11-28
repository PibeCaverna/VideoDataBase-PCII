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
from utils.secciones import Sections
from utils.nuevos_estrenos import get_producciones_recientes

class InterfazUsuario:
    def __init__(self,conexion):
        #Ventana principal
        self._VentanaRaiz   = Tk()
        #Datos a usar
        self._incompleteseries = []
        self._incompletemovies = []
        self.Searched = {}  
        self._currentProfile = None
        self._esinfante = None
        #Frames a usar
        self._FrameLogin    = Frame()
        self._FrameUselect  = Frame()
        self._PFrame        = Frame()   #Frame Padre a la UI del servicio
        self._FrameSearch   = LabelFrame(self._PFrame,relief="sunken",font=("Arial",30,"bold"),text="Busqueda")
        self._FrameMpage    = LabelFrame(self._PFrame,relief="solid" ,font=("Arial",30,"bold"),text="Inicio")
        self._FrameData     = LabelFrame(self._PFrame,relief="sunken",font=("Arial",30,"bold"),text="Detalles")
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
        self.DetailWidgets = ()
                              
                              
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

            self._incompletemovies, self._incompleteseries  = Sections(id_perfil,self._conexion)
            perec, serec = [],[]#get_producciones_receintes(self._conexion)

            #Widgets del menú principal
            self.MenuWidgets =( Label(self._FrameMpage,font=("Arial",20,"bold"),text="Continuar Series:"),
                                Listbox(self._FrameMpage,font=("Arial",20),height=5),
                                Label(self._FrameMpage,font=("Arial",20,"bold"),text="Continuar Peliculas: "),
                                Listbox(self._FrameMpage,font=("Arial",20),height=5),
                                Label(self._FrameMpage,font=("Arial",20,"bold"),text="Adiciones Recientes: "),
                                Listbox(self._FrameMpage,font=("Arial",20),height=5),
                            )
            for i in range(5):

                try: self.MenuWidgets[1].insert(1,self._incompleteseries[0][i])
                except IndexError: pass
                try: self.MenuWidgets[3].insert(1,self._incompletemovies[0][i])
                except IndexError: pass
            for T in perec:
                self.MenuWidgets[5].insert(0,"[m]"+"["+str(T[0])+"]-"+T[1])
            for T in serec:
                self.MenuWidgets[5].insert(0,"[s]"+"["+str(T[0])+"]-"+T[1])

            self.MenuWidgets[0].grid(row=0,column=0)
            self.MenuWidgets[1].grid(row=1,column=0)
            self.MenuWidgets[2].grid(row=2,column=0)
            self.MenuWidgets[3].grid(row=3,column=0)
            self.MenuWidgets[4].grid(row=4,column=0)
            self.MenuWidgets[5].grid(row=5,column=0)
            #Widgets del menú de busqueda
            self.SearchWidgets = (  
                                    Entry(self._FrameSearch,font=("Arial",20)),
                                    Button(self._FrameSearch,font=("Arial",20,"bold"),text="〇",command=self.search),
                                    Listbox(self._FrameSearch,font=("Arial",20),yscrollcommand=True,height=16),
                                    Scrollbar(self._FrameSearch,orient="vertical")
                                  )
                             
            self.SearchWidgets[0].grid(row=0,column=0)
            self.SearchWidgets[1].grid(row=0,column=1)
            self.SearchWidgets[2].grid(row=1,column=0)
            self.SearchWidgets[3].grid(row=1,column=1)
            self.SearchWidgets[2].config(yscrollcommand=self.SearchWidgets[3].set)
            self.SearchWidgets[3].config(command=self.SearchWidgets[2].yview)
            
            #Definición de los eventos a la hora de clickear en las listas
            self.MenuWidgets[1].event_generate("<<ListboxSelect>>")
            self.MenuWidgets[3].event_generate("<<ListboxSelect>>")
            self.MenuWidgets[5].event_generate("<<ListboxSelect>>")
            self.SearchWidgets[2].event_generate("<<ListboxSelect>>")
            self.MenuWidgets[1].bind("<<ListboxSelect>>",self.miseriedata)
            self.MenuWidgets[3].bind("<<ListboxSelect>>",self.mipelidata)
            self.MenuWidgets[5].bind("<<ListboxSelect>>",self.newdata)
            self.SearchWidgets[2].bind("<<ListboxSelect>>",self.searchdata)



            self._PFrame.pack()
        return None
    def miseriedata(self, evento):
        print("seriedata")
        pelis, series = Sections(self._currentProfile,self._conexion)
        print(series)
        for s in series:
            print(s)
            self.MenuWidgets[1].insert(END, s[0][0])

    def mipelidata(self, evento):
        print("pelidata")
        pelis, series = Sections(self._currentProfile,self._conexion)
        print(pelis)
        for p in pelis:
            self.MenuWidgets[1].insert(END, p[0][0])

    def newdata(self, evento):
        # print (get_producciones_recientes(self._conexion))
        pelis, series = get_producciones_recientes(self._conexion)
        for p in pelis:
            self.MenuWidgets[5].insert(END, p[1])    #inserto el nombre

        for s in series:
            self.MenuWidgets[5].insert(END, s[1])    #inserto el nombre
        
    def searchdata(self, evento):
        print("searchdata")
            
    
    def search(self):
        self.SearchWidgets[2].delete(0,END)
        self.Searched = searchtitles(self.SearchWidgets[0].get(),self._conexion,self._esinfante)
        for k,v in self.Searched.items():
            try: self.SearchWidgets[2].insert(1,"["+k+"]"+"["+str(v[0][0])+"]"+"-"+abouttitle(v[0][0],self._conexion)["title"])
            except IndexError: pass
        return None
    
    def MoreData(self,id,tipo="g"):
        if tipo == "g":
            self.DetailWidgets = (Text(self._FrameData),
                                  Text(self._FrameData),
                                  Text(self._FrameData),
                                  Text(self._FrameData)
                                    )
            self.DetailWidgets[0].grid(row=0,column=0)
            self.DetailWidgets[1].grid(row=0,column=1)
            self.DetailWidgets[2].grid(row=0,column=2)
            self.DetailWidgets[3].grid(row=0,column=3)

            dataamostrar = abouttitle(id,self._conexion)
            creditosamostrar = creditos(id,self._conexion) 

            self.DetailWidgets[0].insert(0,dataamostrar["desc"])
            self.DetailWidgets[0].insert(0,dataamostrar["title"]+"\n")
            for A in craditosamostrar["Actores"]:
                self.DetailWidgets[1].insert[0,"    "+A+"\n"]
            self.DetailWidgets[1].insert(0,"Reparto:\n")
            for D in craditosamostrar["Directores"]:
                self.DetailWidgets[2].insert[0,"    "+D+"\n"]
            self.DetailWidgets[2].insert(0,"Dirección:\n")
            for P in craditosamostrar["Productores"]:
                self.DetailWidgets[3].insert[0,"    "+P+"\n"]
            self.DetailWidgets[1].insert(0,"Producción:\n")
            

        elif tipo == "m":
            pass
        elif tipo == "s":
            pass
        elif tipo == "c":
            pass
        else: raise ValueError('Argumento de tipo incorrecto')

        return None

