from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import sys
from subprocess import call

class Recuperar:

	db_name = 'DB.db'
	def __init__(self,ventana_recuperacion):
		#Titulo de la ventana
		self.window = ventana_recuperacion
		self.window.title("Formulario de registro: ")
		self.window.geometry("520x630")
		#self.window.iconbitmap("E:/ADSO/trimestre_5/trabajos_yuly/tiendita/recycle.ico")
		self.window.resizable(0,0)
		self.window.config(bd=10)
		"""Titulo de la ventana"""
		titulo = Label(ventana_recuperacion, text="Registro de usuario", fg="black", font=("Arial", 10, "bold")).pack()
		"""Imagen registro"""
		#imagen_registro = Image.open('E:/ADSO/trimestre_5/trabajos_yuly/tiendita/registro_1.png')
		#nueva_imagen = imagen_registro.resize((40,40))
		#render = ImageTk.PhotoImage(nueva_imagen)
		#label_imagen = Label(ventana_recuperacion, image=render)
		#label_imagen.image = render
		#label_imagen.pack(pady=5)
		"""Marco del registro"""
		marco = LabelFrame(ventana_recuperacion, text="Datos de recuperacion de password", font=("Arial", 10, "bold"))
		marco.config(bd=2, pady=5)
		marco.pack()
		""""Fomrulario de recuperacion """
		label_usuario = Label(marco, text="Usuario" ,font=("Arial", 10, "bold")).grid(row=0,column=0,sticky='s',padx=5,pady=0)
		self.usuario= Entry(marco, width=25)
		self.usuario.focus()
		self.usuario.grid(row=0,column=1,padx=5,pady=5)

		# Marco preguntas de recurso
		marco_pregunta = LabelFrame(ventana_recuperacion, text="Seleccione una pregunta de seguridad y digite la respuesta correcta: ", fg='red',font=("Arial", 10, "bold"),pady=10)
		marco_pregunta.config(bd=2, pady=5)
		marco_pregunta.pack()

		#Preguntas del registro
		label_pregunta = Label(marco_pregunta, text="Pregunta",font=("Arial", 10, "bold")).grid(row=0,column=0,sticky='s',padx=10,pady=8)
		self.combo_pregunta = ttk.Combobox(marco_pregunta, values=["Nombre de su primera mascota", "Nombre de su deporte favorito"],width="30", state="readonly")
		self.combo_pregunta.current(0)
		self.combo_pregunta.grid(row=0,column=1,padx=10,pady=8)
		label_respuesta = Label(marco_pregunta, text="Respuesta: " ,font=("Arial", 10, "bold")).grid(row=1,column=0,sticky='s',padx=5,pady=0)
		self.respuesta= Entry(marco_pregunta, width=25)
		self.respuesta.grid(row=1,column=1,padx=5,pady=5)

		#label password
		label_password = Label(marco, text="Password: " ,font=("Arial", 10, "bold")).grid(row=6,column=0,sticky='s',padx=5,pady=0)
		self.password= Entry(marco, width=25, show="*")
		self.password.grid(row=6,column=1,padx=5,pady=5)

        #label validate_password
		label_validate_password = Label(marco, text="Validar Password: " ,font=("Arial", 10, "bold")).grid(row=7,column=0,sticky='s',padx=5,pady=0)
		self.validate_password= Entry(marco, width=25, show="*")
		self.validate_password.grid(row=7,column=1,padx=5,pady=5)

		label_nota = Label(marco_pregunta, text="Respuesta para recuperar contraseña").grid(row=2,column=0,sticky='s')
		frame_botones = Frame(ventana_recuperacion  )
		frame_botones.pack()

		"""Frame de registro"""

#----metodos de los botones

		boton_recuperar = Button(frame_botones, text="Recuperar",command=self.recuperar_password, height=2, width=9, bg="green", fg="white", font=("Comic Sans MS",8,"bold")).grid(row=1, column=1, padx=10, pady=10)
		boton_login = Button(frame_botones, text="login",command=self.llamar_login_, height=2, width=9, bg="blue", fg="white", font=("Comic Sans MS",8,"bold")).grid(row=1, column=2, padx=10, pady=10)
		boton_cancelar= Button(frame_botones, text="Cancelar",command=ventana_recuperacion.quit, height=2, width=9, bg="red", fg="white", font=("Comic Sans MS",8,"bold")).grid(row=1, column=4, padx=10, pady=10)


	def validar_formulario(self):
		if len(self.usuario.get())!=0  and  len(self.password.get())!=0 and len(self.respuesta.get())!=0:
			return True
		else:
			messagebox.showerror("Error en el registro. ","Diligencie todos los campos del Formulario")

	def validar_password(self):
		if (str(self.password.get()) == str(self.validate_password.get())):
			return True
		else:
			messagebox.showerror("Error en el registro. ", "Diligencie de nuevo su contraseña")

	def validar_usuario(self):
		usuario = self.usuario.get()
		respuesta =self.respuesta.get()
		dato = self.buscar_usuario(usuario, respuesta)
		if (dato != []):
			return True
		else:
			messagebox.showerror("Error en el registro. ", "Los datos no son correctos.")

	def ejecutar_consulta(self,query, parameters =()):
		with sqlite3.connect(self.db_name) as conexion:
			cursor = conexion.cursor()
			result = cursor.execute(query, parameters)
			conexion.commit()
			return result

	def llamar_login_(self):
			ventana_recuperacion.destroy()
			call([sys.executable, 'E:/ADSO/trimestre_5/trabajos_yuly/tiendita/registro.py'])


	def recuperar_password(self):
		if self.validar_formulario() and self.validar_usuario() and self.validar_password():
			query = 'UPDATE Usuarios SET Password_db=(?) WHERE Usuario_db=(?)'
			parameters = (self.usuario.get(), self.password.get())
			self.ejecutar_consulta(query,parameters)
			messagebox.showinfo("CONSTRASEÑA RECUPERADA",f'constraseña actualizada correctamente')
			self.limpiar_formulario()


	def validar_password(self):
		if(str(self.password.get())== str(self.validate_password.get())):
			return True
		else:
			messagebox.showerror("ERROR DE RECUPERACION","las contraseñas no coinciden")


	def buscar_usuario(self,usuario,respuesta):
		with sqlite3.connect(self.db_name) as conexion:
			cursor = conexion.cursor()
			query = f"SELECT * FROM  Usuarios WHERE Usuario_db={usuario} AND Respuesta='{respuesta}'"
			cursor.execute(query)
			dato = cursor.fetchall()#se almacena la respuesta que haga con o sin datos
			cursor.close()
			return dato

	def limpiar_formulario(self):

		self.usuario.delete(0,END)


if __name__ == '__main__':
	ventana_recuperacion = Tk()
	application = 	Recuperar(ventana_recuperacion)
	ventana_recuperacion.mainloop()