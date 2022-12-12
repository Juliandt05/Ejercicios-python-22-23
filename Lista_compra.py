#Nombre cliente
#Numero de productos
import flet as ft



vlista=[]

def main(page: ft.Page):
    
    page.title="Lista de la compra"
    def añadirelemento(e):
        vlista.append(textField_Nombre.value)
        vlista.append (textField_Apellido.value)
        vlista.append(dropDown_Menu.value)
        vlista.append(slider_carne.value)
        vlista.append(dropDown_Menu2.value)
        vlista.append(slider_verdura.value)
    
        t.value=vlista
        page.update()
       
 

    #Componente tetxo
    t=ft.Text(value="Introducción a flet",color="light blue",size=20)

    page.add(t) # add hace dos cosas 1-Añadir 2-Actualizar

    t.value="Lista de alimentos"
    page.update()
    #page update actualiza los datos
    #componente boton
    bt=ft.FloatingActionButton(icon=ft.icons.ADD,on_click=añadirelemento)
    page.add(bt)
    textField_Nombre=ft.TextField(label="Nombre",hint_text="Escribe tu nombre")
    textField_Apellido=ft.TextField(label="Apellido",hint_text="Escribe tu apellido")
    #page.add(textField_Nombre)

    dropDown_Menu= ft.Dropdown(width=300,options=[ft.dropdown.Option("Ternera")],label="Carnes")
    dropDown_Menu.options.append(ft.dropdown.Option("Cerdo"))
    dropDown_Menu.options.append(ft.dropdown.Option("Pollo"))
    slider_carne=ft.Slider(min=0,max=2000,divisions=2000,label="Gramos:{value} g")

    dropDown_Menu2= ft.Dropdown(width=300,options=[ft.dropdown.Option("Lechuga")],label="Verdura")
    dropDown_Menu2.options.append(ft.dropdown.Option("Brocoli"))
    dropDown_Menu2.options.append(ft.dropdown.Option("Zanahorias"))
    slider_verdura=ft.Slider(min=0,max=2000,divisions=2000,label="Gramos:{value} g")
    



    
    

    #Crear fila
    fila=ft.Row(controls=[textField_Nombre,dropDown_Menu,dropDown_Menu2])
    page.add(fila)
    fila2=ft.Row(controls=[textField_Apellido,slider_carne,slider_verdura])
    page.add(fila2)








ft.app(target=main)