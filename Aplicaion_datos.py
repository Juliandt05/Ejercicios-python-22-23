from tkinter import *
from tkinter import ttk


ventana = Tk()
ventana.title("Registro")
ventana.geometry("700x500")
ventana.resizable(width=False,height=False)
ventana.config(background="snow3")

label_titulo=ttk.Label(ventana,text="Datos usuario")

entry_nombre_usuario=ttk.Entry(ventana)
Label_nombre_usuario=ttk.Label(ventana,text="Nombre usuario: ")

entry_pass_usuario=ttk.Entry(ventana)
Label_pass_usuario=ttk.Label(ventana,text="Contraseña")

entry_repitepass_usuario=ttk.Entry(ventana)
Label_repitepass_usuario=ttk.Label(ventana,text="Confirma la contraseña")

boton_guardar=ttk.Button(ventana,text="Guardar")
boton_salir=ttk.Button(ventana,text="Salir")

#Mostrar por pantalla
label_titulo.grid(row=0,column=0)
Label_nombre_usuario.grid(row=1,column=0)
entry_nombre_usuario.grid(row=1,column=1)

Label_pass_usuario.grid(row=2,column=0)
entry_pass_usuario.grid(row=2,column=1)

Label_repitepass_usuario.grid(row=3,column=0)
entry_repitepass_usuario.grid(row=3,column=1)

boton_guardar.grid(row=4,column=0)
boton_salir.grid(row=4,column=1)

ventana.mainloop()