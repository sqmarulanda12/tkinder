#importar libreria

from tkinter import *
#importar la libreria para el manejo de imagenes
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3
from subprocess import call
import sys

class login:

    db_name = 'E:/ADSO/trimestre_5/trabajos_yuly/tiendita/DB.db'

    def __init__(self,ventana_login):

    #----------aibutos de la ventana------------------#

            self.window = ventana_login
            #titulo de la ventana
            self.window.title("Ingreso al sistema")
            #tamaño de la ventana
            self.window.geometry("380x420")
            #icono de la imagen
            self.window.iconbitmap("icono.ico")
            # no se modifique la ventana
            self.window.resizable(0,0)
            #color de la ventana
            self.window.config(bd=10)

    #------------------------ Titulo de la ventana----------------------#
            titulo = Label(ventana_login, text="INICIAR SESION",fg="blue",font=("comic Sans Ms", 13, "bold"),pady=10).pack()


    #---------------------------- LOGO DEL LOGIN ------------------------#
            image_login = Image.open("login.png")
            #tamaño de la imagen
            nueva_imagen = image_login.resize((40,40))
            #renderizar imagen
            render = ImageTk.PhotoImage(nueva_imagen)
            #label para cargar la imagen
            label_imagen = Label(ventana_login, image=render)
            #renderizamos el label
            label_imagen.image = render
            #ubicamos el label
            label_imagen.pack(pady=5)



#---------------------------- MARCO DEL LOGIN ------------------------#

            marco = LabelFrame(ventana_login,text="Ingrese sus datos",font=("Comic Sans Ms",10,"bold"))
            marco.pack()

        #----------------------------FORMULARIO DEL LOGIN ------------------------#
            #label del  usuario
            label_usuario = Label(marco, text="Usuario: ",font=("Comic Sans Ms",10,"bold")).grid(row=0,column=0,sticky='s',padx=5,pady=10)
            #cajon para digitar el usuario
            self.usuario = Entry(marco,width=25)
            #focus ubica el cursor en el entre de self.usuario
            self.usuario.focus()
            self.usuario.grid(row=0, column=1,padx=5,pady=10)

            #label del password
            label_password = Label(marco,text="password",font=("Comic Sans Ms",10,"bold")).grid(row=1,column=0,sticky='s',padx=5,pady=10)
            #cajon para digitar la contraseña
            #show cambia el texto por *
            self.password = Entry(marco,width=25,show="*")

            self.password.grid(row=1,column=1,padx=5,pady=10)


        #---------------------------- FRAME PARA LOS BOTONES DEL LOGIN ------------------------#
            frame_botones = Frame(ventana_login)
            frame_botones.pack()

        #---------------------------- BOTONES DEL LOGIN ---------------------------------------#
            boton_ingresar = Button(frame_botones,text="INGRESAR", command=self.login,height=2,width=12,bg="green",fg="white",font=("Comic Sans MS",10,"bold")).grid(row=0,column=1,padx=10,pady=15)
            boton_registrar = Button(frame_botones,text="REGISTRESE", command=self.llamar_registrar,height=2,width=12,bg="blue",fg="white",font=("Comic Sans MS",10,"bold")).grid(row=0,column=2,padx=10,pady=15)
            boton_registrar = Button(frame_botones,text="PRODUCTOS", command=self.llamar_productos,height=2,width=12,bg="orange",fg="white",font=("Comic Sans MS",10,"bold")).grid(row=0,column=2,padx=10,pady=15)

            label_olvido = Label(frame_botones,text="olvidaste tu contraseña",font=("Comic Sans MS",10,"bold")).grid(row=1,columnspan=2,sticky='s')
            boton_recuperar = Button(frame_botones,text="recupera tu contraseña",height=2,width=24,bg="blue",fg="white",font=("Comic Sans MS",10,"bold")).grid(row=2,column=1,columnspan=2,padx=10,pady= 15 )




    def llamar_registrar(self):

            ventana_login.destroy()

            call([sys.executable, 'registro.py'])

    def llamar_productos(self):
            ventana_login.destroy()

            call([sys.executable, 'producto.py'])




    def login(self):
        if (self.validar_formulario_completo()):
                usuario = self.usuario.get()
                password = self.password.get()
                dato = self.validar_login(usuario,password)
                if (dato != []):
                    messagebox.showinfo("BIENVENIDO","Datos ingresados Correctamente")
                    self.productos()

                else:
                    messagebox.showerror("Error de ingreso","Usuario o Password incorrectos")

    def validar_formulario_completo(self):
            if len(self.usuario.get())!= 0 and len (self.password.get())!= 0:
                return True
            else:
                messagebox.showerror("Error de ingreso", "Ingrese los datos nuevamente")

    def validar_login(self,usuario,password):
            with sqlite3.connect(self.db_name) as conexion:
                cursor = conexion.cursor()
                sql = f"SELECT * FROM Usuarios WHERE usuario={usuario} AND password={password}"
                cursor.execute(sql)
                validacion = cursor.fetchall()
                cursor.close()
                return validacion



if __name__ =='__main__':
    #ventana de objetos
    ventana_login = Tk()
    aplication = login(ventana_login)
    ventana_login.mainloop()
