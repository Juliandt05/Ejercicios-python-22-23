#Nombre cliente
#Numero de productos
import flet as ft





def main(page: ft.Page):
    
    page.title="Lista de la compra"
    def cambiarcolor(e):
        t.value=textField_Nombre.value
        page.update()
       
 

    #Componente tetxo
    t=ft.Text(value="Introducción a flet",color="yellow",size=20)

    page.add(t) # add hace dos cosas 1-Añadir 2-Actualizar

    t.value="Lista de alimentos"
    page.update()
    #page update actualiza los datos
    #componente boton
    bt=ft.FloatingActionButton(icon=ft.icons.ADD,on_click=cambiarcolor)
    page.add(bt)
    textField_Nombre=ft.TextField(label="Nombre",hint_text="Escribe tu nombre")
    page.add(textField_Nombre)

    dropDown_Menu= ft.Dropdown(width=300,options=[ft.dropdown.Option("L")])
    page.add(dropDown_Menu)
    dropDown_Menu.options.append(ft.dropdown.Option("Nueva"))
    page.update()

    slider_edad=ft.Slider(min=0,max=120,divisions=120,label="Edad:{value}")
    page.add(slider_edad)

    #Crear fila
    fila=ft.Row(controls=[textField_Nombre,dropDown_Menu])
    page.add(fila)








ft.app(target=main)