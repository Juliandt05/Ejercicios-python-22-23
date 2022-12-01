from tkinter import *
from tkinter import ttk
from tkinter import messagebox

vLista=[]
vContra=[]
usuario=""
contraseña=""
confirmcon=""

def guardarDatos():
    usuario=entry_nombre_usuario.get()
    contraseña=entry_pass_usuario.get()
    confirmcon=entry_repitepass_usuario.get()
    if contraseña==confirmcon:
        vLista.append(usuario)
        vLista.append(contraseña)
        entry_nombre_usuario.delete(0,len(usuario))
        entry_pass_usuario.delete(0,len(contraseña))
        entry_repitepass_usuario.delete(0,len(confirmcon))
        messagebox.showinfo("Usuario Guardado",f"Usuario ")
    print(vLista)

def imprimirDatos():
    print(vLista)


ventana = Tk()
ventana.title("Registro")
ventana.geometry("500x300")
ventana.resizable(width=False,height=False)
ventana.config(background="snow3")

label_titulo=ttk.Label(ventana,text="Datos usuario")

entry_nombre_usuario=ttk.Entry(ventana)
Label_nombre_usuario=ttk.Label(ventana,text="Nombre usuario: ")

entry_pass_usuario=ttk.Entry(ventana,show="*")
Label_pass_usuario=ttk.Label(ventana,text="Contraseña")

entry_repitepass_usuario=ttk.Entry(ventana,show="*")
Label_repitepass_usuario=ttk.Label(ventana,text="Confirma la contraseña: ")

boton_guardar=ttk.Button(ventana,text="Guardar",command=guardarDatos)
boton_salir=ttk.Button(ventana,text="Salir",command=ventana.destroy)

#Mostrar por pantalla
label_titulo.grid(row=0,column=0,pady=5,padx=10)
Label_nombre_usuario.grid(row=1,column=0,pady=10,padx=10)
entry_nombre_usuario.grid(row=1,column=1,pady=10,padx=10)

Label_pass_usuario.grid(row=2,column=0,pady=10,padx=10)
entry_pass_usuario.grid(row=2,column=1,pady=10,padx=10)

Label_repitepass_usuario.grid(row=3,column=0,pady=10,padx=10)
entry_repitepass_usuario.grid(row=3,column=1,pady=10,padx=10)

boton_guardar.grid(row=4,column=1,pady=10,padx=10)
boton_salir.grid(row=4,column=0,pady=10,padx=10)



ventana.mainloop()