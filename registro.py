#importar las librerias

from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import sys
from subprocess import call

class Registro:

    db_name = 'C:/Users/AdminZona1/Downloads/trimestre_5/trabajos_yuly/tiendita/base_datos_proyecto2503319.db'
    def __init__(self,ventana_registro):


        #---------------------Atributos de la ventana------------------------#
        self.window = ventana_registro
        #titulo de la ventana
        self.window.title("FORMULARIO DE REGISTRO")
        #tamaño de la ventana
        self.window.geometry("500x830")
        #icono de la imagen
        self.window.iconbitmap("icono.ico")
        # no se modifique la ventana
        self.window.resizable(0,0)
        #color de la ventana
        self.window.config(bd=10)
        #color de la ventana
        self.window.config(bd=10)

        #-------------------- Titulo de la ventana-----------------------------#

        titulo = Label(ventana_registro, text="REGISTRO DEL USUARIO",fg="blue",font=("Comic Sans Ms", 13, "bold"),pady=5).pack()


    #--------------------- IMAGEN DEL REGISTRO-----------------------------#

        image_registro = Image.open("registro_1.png")
        nueva_imagen = image_registro.resize((80,80))
        #renderizar imagen
        render = ImageTk.PhotoImage(nueva_imagen)
        #label para cargar la imagen
        label_imagen = Label(ventana_registro, image=render)
        #renderizamos el label
        label_imagen.image = render
        #ubicamos el label
        label_imagen.pack(pady=5)

    #------------------------- Crear un Marco-------------------------------#
        marco = LabelFrame(ventana_registro,text="Datos personales",font=("Comic Sans Ms", 13, "bold"),fg="blue")
        marco.config(bd=2,pady=5)
        marco.pack()

    #------------------------- Crear un Marco usuario, nombre, apellido,etc-------------------------------#
        label_usuario = Label(marco, text="Usuario: ",font=("Comic Sans Ms",10,"bold")).grid(row=0,column=0,sticky='s',padx=5,pady=8)
        self.usuario = Entry(marco,width=25)
        self.usuario.focus()
        self.usuario.grid(row=0, column=1,padx=5,pady=5)

        label_nombre = Label(marco, text="Nombre: ",font=("Comic Sans Ms",10,"bold")).grid(row=1,column=0,sticky='s',padx=5,pady=8)
        self.nombre = Entry(marco,width=25)
        self.nombre.focus()
        self.nombre.grid(row=1, column=1,padx=5,pady=5)

        label_apellido = Label(marco, text="Apellido: ",font=("Comic Sans Ms",10,"bold")).grid(row=2,column=0,sticky='s',padx=5,pady=8)
        self.apellido = Entry(marco,width=25)
        self.apellido.focus()
        self.apellido.grid(row=2, column=1,padx=5,pady=5)

        label_genero = Label(marco, text="Genero: ",font=("Comic Sans Ms",10,"bold")).grid(row=3,column=0,sticky='s',padx=5,pady=8)
        self.genero = ttk.Combobox(marco, values=["Masculino" , "femenino","prefiero no decirlo"],width=22, state="readonly")
        #para que aparezca en posicion 0
        self.genero.current(0)
        self.genero.grid(row=3,column=1, padx=5,pady=8)


        label_correo = Label(marco, text="Correo: ",font=("Comic Sans Ms",10,"bold")).grid(row=4,column=0,sticky='s',padx=5,pady=8)
        self.correo = Entry(marco,width=25)
        self.correo.focus()
        self.correo.grid(row=4, column=1,padx=5,pady=5)



        label_edad = Label(marco, text="Edad: ",font=("Comic Sans Ms",10,"bold")).grid(row=5,column=0,sticky='s',padx=5,pady=8)
        self.edad = Entry(marco,width=25)
        self.edad.focus()
        self.edad.grid(row=5, column=1,padx=5,pady=5)

        label_password = Label(marco,text="Password",font=("Comic Sans Ms",10,"bold")).grid(row=6,column=0,sticky='s',padx=5,pady=10)
        self.password = Entry(marco,width=25,show="*")
        self.password.grid(row=6,column=1,padx=10,pady=8)

        label_password_confia = Label(marco,text="Confirma tu password",font=("Comic Sans Ms",10,"bold")).grid(row=7,column=0,sticky='s',padx=5,pady=10)
        self.password_confia = Entry(marco,width=25,show="*")
        self.password_confia.grid(row=7,column=1,padx=10,pady=8)

    #------------------------- MARCO DE PREGUNTAS DEL REGISTRO---------------------------------------------------------------------------------------#

        marco_pregunta = LabelFrame(ventana_registro,text="Pregunta de seguridad",font=("Comic Sans Ms",10,"bold"),padx=10)
        marco_pregunta.config(bd=2, pady=5)
        marco_pregunta.pack()

#------------------------- PREGUNTAS DEL REGISTRO-------------------------------------------------------------------------------#

        combo_pregunta = Label(marco_pregunta, text="Pregutas: ",font=("Comic Sans Ms",10,"bold")).grid(row=0,column=0,sticky='s',padx=10,pady=8)
        self.combo_pregunta  = ttk.Combobox(marco_pregunta, values=["nombre de tu primera mascota" , "nombre de tu colegio","nombre de un tio"],width=30, state="readonly")
        self.combo_pregunta.current(0)
        self.combo_pregunta.grid(row=0,column=1,padx=10,pady=8)


        label_respuesta = Label(marco_pregunta, text="Coloca tu Respuesta: ",font=("Comic Sans Ms",10,"bold")).grid(row=1,column=0,sticky='s',padx=5,pady=8)
        self.respuesta = Entry(marco_pregunta,width=25)
        self.respuesta.focus()
        self.respuesta.grid(row=1, column=1,padx=5,pady=5)


        label_usuario_respuesta = Label(marco_pregunta, text="Esta respuesta permite recuperar la contraseña ",font=("Comic Sans Ms",10,"bold")).grid(row=2,column=0,columnspan= 2 ,sticky='s',padx=5,pady=8)

    #---------------------------- FRAME PARA LOS BOTONES DEL REGISTRO ------------------------#
        frame_botones = Frame(ventana_registro)
        frame_botones.pack()


#---------------------------- BOTONES DEL REGISTRO ---------------------------------------#

        boton_registrar = Button(frame_botones,text="Registrar ",command=self.registrar_usuario,height=2,width=7,bg="blue",fg="white",font=("Comic Sans MS",9,"bold")).grid(row=0,column=1,padx=10,pady=15)
        boton_limpiar = Button(frame_botones,text="limpiar ", command=self.limpiar_formulario, height=2,width=7,bg="purple",fg="white",font=("Comic Sans MS",9,"bold")).grid(row=0,column=2,padx=10,pady=15)
        boton_login = Button(frame_botones,text="login ", command=self.llamar_login ,height=2,width=7,bg="pink",fg="white",font=("Comic Sans MS",9,"bold")).grid(row=0,column=3,padx=10,pady=15)
        boton_cancelar = Button(frame_botones,text="cancelar ",command=ventana_registro.quit,height=2,width=7,bg="aquamarine",fg="white",font=("Comic Sans MS",9,"bold")).grid(row=0,column=4,padx=10,pady=15)


#---------------------------- METODOS DEL REGISTRO ---------------------------------------#
    def registrar_usuario(self):
        if self.validar_formulario() and self.validar_password() and self.validar_usuario():
            #sentencia Sql
            query = 'INSERT INTO Usuarios VALUES (NULL,?,?,?,?,?,?,?,?)'
            #Captura de parametros del formulario

            parametros = (self.usuario.get(), self.nombre.get(),self.apellido.get(),self.genero.get(),self.correo.get(),self.edad.get(),self.password.get(),self.respuesta.get())
            #invocacion del metodo para la ejecucion de la consulta

            self.ejecutar_consulta(query,parametros)
            #ventana Emergente informativa para mostrar el registro exitoso del usuario

            messagebox.showinfo("Registro EXITOSO", f'bienvenid@{self.nombre.get()} {self.apellido.get()}')
            self.limpiar_formulario()


    def validar_formulario(self):
        if len(self.usuario.get()) != 0 and (self.nombre.get()) != 0 and (self.apellido.get()) != 0 and (self.genero.get()) != 0 and (self.correo.get()) != 0 and (self.edad.get()) != 0 and (self.password.get()) != 0 and (self.respuesta.get()) != 0:
            return True
        else:
            messagebox.showerror("ERROR EN EL REGISTRO", "complete las todas las areas antes de continuar")



        # metodo para verificar que las contraseñas sean iguales
    def validar_password(self):
        if (str(self.password.get()) == str(self.password_confia.get())):
            return True

    def validar_usuario(self):
        usuario = self.usuario.get()
        dato = self.buscar_usuario(usuario)
        if (dato == []):
            return True

        else:
            messagebox.showerror = ("ERROR EN EL REGISTRO","EL USUARIO YA EXISTE")
#-----------------------------------    Conexion de laas base de datos--------------------------------------#

    def buscar_usuario(self,usuario):
        #conexion a la base de datos

        with sqlite3.connect(self.db_name) as conexion:
            cursor = conexion.cursor()
            sql = "SELECT * FROM Usuarios WHERE usuario = {}".format(usuario)
            cursor.execute(sql)
            usuario_consulta = cursor.fetchall()
            cursor.close()
            return usuario_consulta

    def ejecutar_consulta(self, query, parametros=()):
        with sqlite3.connect(self.db_name) as conexion:
            cursor = conexion.cursor()
            result = cursor.execute(query,parametros)
            conexion.commit()
            return result

    def limpiar_formulario(self):

        self.usuario.delete(0,END)
        self.nombre.delete(0,END)
        self.apellido.delete(0,END)
        self.combo_genero.delete(0,END)
        self.edad.delete(0,END)
        self.correo.delete(0,END)
        self.password.delete(0,END)
        self.password_confia.delete(0,END)
        self.combo_pregunta.delete(0,END)
        self.respuesta.delete(0,END)


    def llamar_login(self):
        ventana_registro.destroy()


        call([sys.executable,'login.py'])




if __name__ =='__main__':
    #ventana de objetos
    ventana_registro = Tk()
    application = Registro(ventana_registro)
    ventana_registro.mainloop()
