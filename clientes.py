from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import sys
from subprocess import call


class Clientes():
	db_name = "C:/Users/Santiago/Desktop/ADSO/trimestre_5/trabajos_yuly/tiendita/base_datos_proyecto2503319.db"
	def __init__(self,ventana_clientes):
		# Atributos de la ventana
		self.ventana_clientes = ventana_clientes
		menubar = Menu(ventana_clientes)
        # Titulo
		self.ventana_clientes.title("Clientes")

		self.ventana_clientes.geometry("1080x920")
        # Icono
		#self.ventana_clientes.iconbitmap("C:/Users/Aprendiz/Desktop/tienda/tiendaform_icon_142679.ico")
        # Permisos de acondicionar el tamaño
		self.ventana_clientes.resizable(0,0)
        # Color de la ventana
		self.ventana_clientes.config(bd=10, menu=menubar)
	#--------------Menu de la ventana----------------------
		Productos = Menu(menubar, tearoff=0)
		Clientes = Menu(menubar, tearoff=0)
		Ventas = Menu(menubar, tearoff=0)
		Informacion = Menu(menubar, tearoff=0)

		menubar.add_cascade(label="Productos",menu=Productos)
		menubar.add_cascade(label="Clientes",menu=Clientes)
		menubar.add_cascade(label="Ventas",menu=Ventas)
		menubar.add_cascade(label="Informacion",menu=Informacion)

		#self.img_registrar =PhotoImage(file="")
		#self.img_buscar =PhotoImage(file="")
		#self.img_registrar =PhotoImage(file="")

		self.boton_registrar = Productos.add_command(label="Registrar",command=self.widgets_crud, compound=LEFT)
		#Arriba va una imagen
		self.boton_buscar = Productos.add_command(label="Buscar",command=self.widgets_buscador, compound=LEFT)
		#Arriba va una imagen
		self.boton_informacion = Informacion.add_command(label="Informacion del sistema",command=self.widgets_informacion, compound=LEFT)
		#Arriba va una imagen
		self.boton_cliente = Clientes.add_command(label="Apartado Clientes",command=self.llamar_clientes, compound=LEFT)

		self.boton_venta = Ventas.add_command(label="Apartado de Ventas",command=self.llamar_ventas, compound=LEFT)

		#----------------------------------------WIDGETS DEL MENU-----------------------
		self.label_titulo_crud = LabelFrame(ventana_clientes)
		self.frame_logo_productos = LabelFrame(ventana_clientes)
		self.frame_registro = LabelFrame(ventana_clientes, text= "Informacion de los clientes", font=("comic sans", 10, "bold"),pady=5)
		self.frame_botones_registro = LabelFrame(ventana_clientes)
		self.frame_tabla_crud = LabelFrame(ventana_clientes)

		self.label_titulo_buscador = LabelFrame(ventana_clientes)
		self.frame_buscar_producto = LabelFrame(ventana_clientes, text= "Buscar Clientes", font=("comic sans", 10, "bold"),pady=10)
		self.frame_boton_buscar = LabelFrame(ventana_clientes)

		self.label_informacion = LabelFrame(ventana_clientes)

		self.widgets_crud()
		#------------------------------------------------------------------------------


		titulo = Label(ventana_clientes, text="Registro del Clientes	", fg="black", font=("Arial", 10, "bold"));"""pack()"""

		frame_registro = LabelFrame(ventana_clientes, text="Datos del Cliente	", font=("Arial", 10, "bold"))
		frame_registro.config(bd=2, pady=5)
		"""marco.pack()"""
		#--------------------------------------- Columna 1--------------------------------------------------------------------------------
		label_codigo = Label(self.frame_registro, text= "Codigo: ",font=("Arial", 10, "bold")).grid(row=0,column=0,sticky='s',padx=5,pady=10)
		self.codigo = Entry(self.frame_registro,width=25)
		self.codigo.focus()
		self.codigo.grid(row=0,column=1,padx=5,pady=10)
		#----------------------------------------DATO 2--------------------------------------------------------------------------------
		label_nombre = Label(self.frame_registro, text= "Nombre: ",font=("Arial", 10, "bold")).grid(row=1,column=0,sticky='s',padx=5,pady=10)
		self.nombre = Entry(self.frame_registro,width=25)
		self.nombre.focus()
		self.nombre.grid(row=1,column=1,padx=5,pady=10)
		#----------------------------------------DATO 3-------------------------------------------------------------
		label_email = Label(self.frame_registro, text="Email: ",font=("Arial", 10, "bold")).grid(row=2, column=0,sticky='s',padx=5,pady=0)
		self.email = Entry(self.frame_registro,width=25)
		self.email.focus()
		self.email.grid(row=2,column=1,padx=5,pady=5)
		#--------------------------------------Colunma2-------------------------------------------------------------------------------------------
		label_direccion = Label(self.frame_registro, text= "Direccion: ",font=("Arial", 10, "bold")).grid(row=0,column=2,sticky='s',padx=5,pady=10)
		self.direccion = Entry(self.frame_registro,width=25)
		self.direccion.focus()
		self.direccion.grid(row=0,column=3,padx=5,pady=10)
		#-------------------------------------DATO 2---------------------------------------------------------------------
		label_edad = Label(self.frame_registro, text= "Edad: ",font=("Arial", 10, "bold")).grid(row=1,column=2,sticky='s',padx=5,pady=10)
		self.edad = Entry(self.frame_registro,width=25)
		self.edad.focus()
		self.edad.grid(row=1,column=3,padx=5,pady=10)


		"""------------------------------------Frame de registro-----------------------------------------------------------------"""

		frame_botones_registro = Frame(ventana_clientes)
		"""frame_botones_registro.pack()"""


		boton_registo = Button(self.frame_botones_registro, text="Registrar",command=self.registrar_clientes, height=2, width=9, bg="green", fg="white", font=("Comic Sans MS",8,"bold")).grid(row=1, column=1, padx=10, pady=10)
		boton_editar = Button(self.frame_botones_registro, text="Editar",command=self.editar_clientes, height=2, width=9, bg="blue", fg="white", font=("Comic Sans MS",8,"bold")).grid(row=1, column=2, padx=10, pady=10)
		boton_limpiar = Button(self.frame_botones_registro, text="Limpiar",command=self.limpiar_formulario, height=2, width=9, bg="brown", fg="white", font=("Comic Sans MS",8,"bold")).grid(row=1, column=3, padx=10, pady=10)
		boton_cancelar= Button(self.frame_botones_registro, text="Cancelar",command=ventana_clientes.quit, height=2, width=9, bg="red", fg="white", font=("Comic Sans MS",8,"bold")).grid(row=1, column=4, padx=10, pady=10)
		boton_eliminar= Button(self.frame_botones_registro, text="Eliminar",command=self.eliminar_clientes, height=2, width=9, bg="orange", fg="white", font=("Comic Sans MS",8,"bold")).grid(row=1, column=5, padx=10, pady=10)

	#------------------------------Metodos----------------------------------------------------------------------------------------------------------------------
	def registrar_clientes(self):
		if self.validar_formulario() and self.validar_registrar():
			query = "INSERT INTO Clientes VALUES(NULL,?,?,?,?,?)"
			parametros = (self.codigo.get(),self.nombre.get(),self.email.get(),self.direccion.get(),self.edad.get())
			self.ejecutar_consulta(query, parametros)
			messagebox.showinfo("Registro exitoso",f"el Cliente fue registrado")
			self.limpiar_formulario()

	#--------------------------------Validar Formulario--------------------------------------------------------------------------------
	def validar_formulario(self):
		if  len(self.codigo.get())!=0 and len(self.nombre.get())!=0 and len(self.email.get())!=0 and len(self.direccion.get())!=0 and len(self.edad.get())!=0:
			return True
		else:
			messagebox.showerror("Error en el registro. ",f"Diligencie todos los campos del Formulario")

	def validar_formulario(self):
				if  len(self.codigo.get())!=0 and len(self.nombre.get())!=0 and len(self.email.get())!=0 and len(self.direccion.get())!=0 and len(self.edad.get())!=0:
					return	True
				else:
					messagebox.showerror("Error en el registro",f"Diligencie el formulario de nuevo")


	#------------------------------------Ejecutar Consulta-------------------------------------------------------------------------------------------------------
	def ejecutar_consulta(self,query,parametros =()):
		print(parametros)
		with sqlite3.connect(self.db_name) as conexion:
			cursor = conexion.cursor()
			result = cursor.execute(query, parametros)
			conexion.commit()
			return result
	#----------------------------------------- Limpiar Formulario-------------------------------------------------------------------------------------
	def limpiar_formulario(self):
		self.codigo.delete(0,END)
		self.nombre.delete(0,END)
		self.email.delete(0,END)
		self.direccion.delete(0,END)
		self.edad.delete(0,END)
	#----------------------------------------- Listar Clientes-------------------------------------------------------------------------------------------
	def listar_Clientes(self):
		records = self.tree.get_children()
		for element in records:
			self.tree.delete(element)
		query = 'SELECT * FROM	Clientes ORDER BY  nombre  DESC'
		db_rows = self.ejecutar_consulta(query)
		for	row in db_rows:
			self.tree.insert("",0, text=row[1], values=(row[2],row[3],row[4],row[5]))
	#---------------------------------Editar Producto--------------------------------------------------------------------------------------------------
	def editar_clientes(self):
		try:
			self.tree.item(self.tree.selection())['values'][0]
		except IndexError as e:
			messagebox.showerror("ERROR",f"Debe seleccionar una venta de la tabla")

		codigo = self.tree.item(self.tree.selection())['text']
		nombre = self.tree.item(self.tree.selection())['values'][0]
		email = self.tree.item(self.tree.selection())['values'][1]
		direccion = self.tree.item(self.tree.selection())['values'][2]
		edad = self.tree.item(self.tree.selection())['values'][3]


		self.ventana_editar = Toplevel()
		self.ventana_editar.title("EDITAR PRODUCTO")
		self.ventana_editar.resizable(0,0)


		label_codigo = Label(self.ventana_editar, text="Código de la venta:", font=("Comic Sans", 10, "bold")).grid(row=0, column=0, sticky='s', padx=5, pady=8)
		nuevo_codigo = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=codigo), width=25)
		nuevo_codigo.grid(row=0, column=1, padx=5, pady=8)

		label_email = Label(self.ventana_editar, text="Email:", font=("Comic Sans", 10, "bold")).grid(row=0, column=2, sticky='s', padx=5, pady=8)
		nuevo_email = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=email), width=25)
		nuevo_email.grid(row=0, column=3, padx=5, pady=0)

		label_nombre = Label(self.ventana_editar, text="Nombre del Clientes:", font=("Comic Sans", 10, "bold")).grid(row=1, column=0, sticky='s', padx=5, pady=8)
		nuevo_nombre = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=nombre), width=25)
		nuevo_nombre.grid(row=1, column=1, padx=5, pady=0)

		label_direccion = Label(self.ventana_editar, text="Direccion:", font=("Comic Sans", 10, "bold")).grid(row=2, column=0, sticky='s', padx=5, pady=8)
		nueva_direccion = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=direccion), width=25)
		nueva_direccion.grid(row=2, column=1, padx=5, pady=0)

		label_edad = Label(self.ventana_editar, text="Edad:", font=("Comic Sans", 10, "bold")).grid(row=2, column=2, sticky='s', padx=5, pady=8)
		nuevo_edad = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=edad), width=25)
		nuevo_edad.grid(row=2, column=3, padx=5, pady=0)

		boton_actualizar = Button(self.ventana_editar, text="ACTUALIZAR", command=lambda:self.actualizar(nuevo_codigo.get(), nuevo_nombre.get(), nuevo_email.get(), nueva_direccion.get(), nuevo_edad.get(),  codigo), height=2, width=20, bg="blue", fg="white", font=("Comic Sans MS", 9, "bold"))
		boton_actualizar.grid(row=3, column=1, columnspan=2, padx=10, pady=15)

		self.ventana_editar.mainloop()

	#---------------------------------------------------- Actulizar Producto-----------------------------------------------------------------------------------------

	def actualizar(self, nuevo_codigo, nuevo_nombre, nuevo_email, nueva_direccion, nuevo_edad,  codigo):
		query = 'UPDATE Clientes SET codigo = ?, nombre = ?, email = ?, direccion = ?, edad = ?  WHERE codigo = ?'
		parameters = (nuevo_codigo, nuevo_nombre, nuevo_email, nueva_direccion, nuevo_edad, codigo)
		self.ejecutar_consulta(query, parameters)
		messagebox.showinfo('EXITO',f'Cliente Actualizado:{nuevo_nombre}')
		self.ventana_editar.destroy()
		self.listar_Clientes()

	#--------------------------------------------------- Eliminar Producto----------------------------------------------------------------------------------

	def eliminar_clientes(self):
		try:
			self.tree.item(self.tree.selection())['values'][0]
		except IndexError as e:
			messagebox.showerror('Error',f'Debe seleccionar un producto de la tabla')
		dato = self.tree.item(self.tree.selection())['text']
		nombre = self.tree.item(self.tree.selection())['values'][0]
		query = "DELETE FROM Clientes WHERE codigo = ?"
		respuesta = messagebox.askquestion("ADVERTENCIA",f"¿Està seguro que desea eliminar este Cliente: {nombre}?")
		if respuesta == "yes":
			self.ejecutar_consulta(query,(dato,))
			self.listar_Clientes()
			messagebox.showinfo('Exito',f'Cliente eliminado: {nombre}')
		else:
			messagebox.showerror('ERROR',F'Error al eliminar el cliente: {nombre}')

	#----------------------------------------------- Widgets Crud ------------------------------------------------------------------------------------
	def widgets_crud(self):
		self.label_titulo_crud.config(bd=0)
		self.label_titulo_crud.grid(row=0, column=0, padx=5, pady=5)
	#----------------------------------------------- Titulo de la ventana-----------------------------------------------------------------------

		self.titulo_crud = Label(self.label_titulo_crud, text="LISTA DE CLIENTES",fg="aquamarine",bg="black",font=("Comic Sans", 17, "bold"),pady=10)
		self.titulo_crud.grid(row=0, column=0, padx=5, pady=5)
	#------------------------------------------------------


		self.frame_logo_productos.config(bd=2)
		self.frame_logo_productos.grid(row=2, column=0, padx=5, pady=5)
	#---------------------------------------------------------------------------------------------------------------------------------------------
		#              Marco de la ventana
		self.frame_registro.config(bd=2)
		self.frame_registro.grid(row=2, column=0, padx=5, pady=5)

		#  frame  botones
		self.frame_botones_registro.config(bd=0)
		self.frame_botones_registro.grid(row=3,column=0,padx=5,pady=5)

		#------------------ Tabla de productos ----------------------
		self.frame_tabla_crud.config(bd=2)
		self.frame_tabla_crud.grid(row=4,column=0,padx=5,pady=5)
		self.tree = ttk.Treeview(self.frame_tabla_crud,height=13, columns=("columna1", "columna2", "columna3", "columna4", "columna5"))

		self.tree.heading("#0", text="Codigo: ", anchor=CENTER)
		self.tree.column("#0", width=90 ,minwidth=50, stretch=False)

		self.tree.heading("columna1", text="Codigo: ", anchor=CENTER)
		self.tree.column("columna1", width=150 ,minwidth=50, stretch=False)

		self.tree.heading("columna1", text="nombre: ", anchor=CENTER)
		self.tree.column("columna1", width=150 ,minwidth=75, stretch=False)

		self.tree.heading("columna2", text="email: ", anchor=CENTER)
		self.tree.column("columna2", width=150 ,minwidth=75, stretch=False)

		self.tree.heading("columna3", text="direccion: ", anchor=CENTER)
		self.tree.column("columna3", width=150 ,minwidth=75, stretch=False)

		self.tree.heading("columna4", text="edad: ", anchor=CENTER)
		self.tree.column("columna4", width=150 ,minwidth=75, stretch=False)

		self.tree.heading("columna5", text="descripcion: ", anchor=CENTER)
		self.tree.column("columna5", width=150 ,minwidth=75, stretch=False)

		self.tree.grid(row=0,column=0,sticky=E)

		#self.tree.pack()
		self.listar_Clientes()

		self.widgets_buscador_remove()
		self.label_informacion.grid_remove()



	#---------------------------------------------- widgets Buscador------------------------------------------------------------------------------
	def widgets_buscador(self):
		self.label_titulo_buscador.config(bd=0)
		self.label_titulo_buscador.grid(row=0, column=0, padx=5, pady=5)

		self.titulo_buscador = Label(self.label_titulo_buscador, text="BUSCADOR DE CLIENTES ",fg="black",font=("Comic Sans", 17, "bold"))
		self.titulo_buscador.grid(row=0, column=0)

		self.frame_buscar_producto.config(bd=2)
		self.frame_buscar_producto.grid(row=2, column=0, padx=5, pady=5)

		self.label_buscar = Label(self.frame_buscar_producto, text="Buscar por: ",font=("Arial", 10, "bold")).grid(row=0, column=0,sticky='s',padx=5,pady=5)
		self.combo_buscar= ttk.Combobox(self.frame_buscar_producto, values=["Codigo","Nombre"], width=22, state="readonly")
		self.combo_buscar.current()
		self.combo_buscar.grid(row=0,column=1,padx=5,pady=5)

		self.label_codigo_nombre = Label(self.frame_buscar_producto, text= "Codigo / Nombre del cliente : ",font=("comic sans", 10, "bold")).grid(row=0,column=2,sticky='s',padx=5,pady=5)
		self.codigo_nombre = Entry(self.frame_buscar_producto,width=25)
		self.codigo_nombre.focus()
		self.codigo_nombre.grid(row=0,column=3,padx=5,pady=5)

		self.frame_boton_buscar.config(bd=0)
		self.frame_boton_buscar.grid(row=3, column=0, padx=5, pady=5)

		self.boton_buscar = Button(self.frame_boton_buscar, text="BUSCAR", command=self.buscar_Clientes, height=2, width=20, bg="black", fg="white",font=("comic sans", 10, "bold"))
		self.boton_buscar.grid(row=0,column=0,padx=5,pady=5)

		self.tree.delete(*self.tree.get_children())

		self.widgets_crud_remove()
		self.label_informacion.grid_remove()
#------------------------------------------------------------------------ widgets ---------------------------------------------------------------------------------
	def widgets_crud_remove(self):
		self.label_titulo_crud.grid_remove()
		self.frame_registro.grid_remove()
		self.frame_botones_registro.grid_remove()

	def widgets_buscador_remove(self):
		self.label_titulo_buscador.grid_remove()
		self.frame_buscar_producto.grid_remove()
		self.frame_boton_buscar.grid_remove()

	def widgets_informacion(self):
		self.frame_logo_productos.grid_forget()
		self.frame_tabla_crud.grid_forget()
		self.label_informacion.config(bd=0)
		self.label_informacion.grid(row=0, column=0)
		#self.imagen_soporte.config(row=0,column=0)

		self.label_titulo = Label(self.label_informacion, text= "APLICACION DE ESCRITORIO", fg="aquamarine", bg="aquamarine",font=("comic sans", 25, "bold"),padx=137, pady=20)
		self.label_titulo.grid(row=0, column=0)

		#imagen_soporte = Image()
		#nueva_imagen = imagen_soporte.resize((170,170))
		#render = ImageTK.PhotoImage(nueva_imagen)
		#label_imagen = Label(self.imagen_soporte, image=render)
		#label_imagen.image = render
		#label_imagen.grid(row=1,column=0,padx=10,pady=15)

		self.label_titulo = Label(self.label_informacion, text="> Codigo de tienda de Tecnologìa", fg="black", font=("comic sans", 18, "bold"))
		self.label_titulo.grid(row=2,column=0,sticky="W",padx=30,pady=10)

		self.label_titulo = Label(self.label_informacion, text="> En esta tienda encuentra productos de Tecnologìa", fg="black", font=("comic sans", 18, "bold"))
		self.label_titulo.grid(row=3,column=0,sticky="W",padx=30,pady=10)

		self.label_titulo = Label(self.label_informacion, text="> Instructora: Yuli Sàenz", fg="black", font=("comic sans", 18, "bold"))
		self.label_titulo.grid(row=4,column=0,sticky="W",padx=30,pady=10)


		self.label_titulo = Label(self.label_informacion, text="> Creado por Yuli Sàenz - Ficha 25003319 Tgo.ADSO. - 2023 ", fg="black", font=("comic sans", 10, "bold"))
		self.label_titulo.grid(row=7,column=0,pady=60)

		self.widgets_buscador_remove()
		self.widgets_crud_remove()
		#-------------------------------MAS metodos-----------------------------------------------------------------------------------------
	def buscar_Clientes(self):
		if(self.validar_busqueda()):
			records = self.tree.get_children()
			for element in records:
				self.tree.delete(element)

			if (self.combo_buscar.get() == "codigo"):
				query= ("SELECT * FROM Clientes WHERE codigo LIKE ?")
				parametros = (self.codigo_nombre.get()+"%")
				db_rows = self.ejecutar_consulta(query,(parametros, ))
				for row in db_rows :
					self.tree.insert("",0,text=row[1],values=(row[2],row[3],row[4],row[5],row[6]))

				if(list(self.tree_get_children() == []) ==[]):
					messagebox.showerror("Error",f"Clientes no encontrado")
			else:
				query = ("SELECT * FROM Clientes WHERE nombre LIKE ?")
				parametros = ("%"+self.codigo_nombre.get()+"%")
				db_rows = self.ejecutar_consulta(query,(parametros, ))
				for row in db_rows :
					self.tree.insert("",0,text=row[1],values=(row[2],row[3],row[4],row[5],row[6]))
				if(list(self.tree.get_children() == []) ==[]):
					messagebox.showerror("Error",f"Cliente no encontrado")
	def validar_busqueda(self):
		if len(self.codigo_nombre.get()) !=0:
			return True
		else:
			self.tree.delete(*self.tree.get_children())
			messagebox.showerror("ERROR",f"Complete todos los campos")

	def validar_registrar(self):
		parametros = self.codigo.get()
		query = "SELECT  * FROM Clientes WHERE codigo = ?"
		dato = self.ejecutar_consulta(query, (parametros, ))
		if (dato.fetchall() == []):
			return True
		else:
			messagebox.showerror("ERROR EN REGISTRO",f"Codigo no registrado anteriormente")


	def llamar_clientes(self):
		ventana_clientes.destroy()
		call([sys.executable,'clientes.py'])

		call([sys.executable, 'C:/Users/Santiago/Desktop/ADSO/trimestre_5/trabajos_yuly/tiendita/clientes.py'])


	def llamar_ventas(self):
		ventana_clientes.destroy()

		call([sys.executable, 'C:/Users/Santiago/Desktop/ADSO/trimestre_5/trabajos_yuly/tiendita/venta.py'])













if __name__ == '__main__':
	ventana_clientes = Tk()
	application = Clientes(ventana_clientes)
	ventana_clientes.mainloop()

