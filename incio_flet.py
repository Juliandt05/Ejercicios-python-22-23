import flet as ft





def main(page: ft.Page):
    
    page.title="Flet inicio"
    def cambiarcolor(e):
        for i in range(10):
            text=ft.Text(value=f"Texto nummero{i}",size=30)
            page.add(text)
 

    #Componente tetxo
    t=ft.Text(value="Introducción a flet",color="yellow",size=20)

    page.add(t) # add hace dos cosas 1-Añadir 2-Actualizar

    t.value="cambiado los datos"
    page.update()
    #page update actualiza los datos
    #componente boton
    bt=ft.FloatingActionButton(icon=ft.icons.ADD,on_click=cambiarcolor)
    page.add(bt)
    textField_Nombre=ft.TextField(label="Nombre",hint_text="Escribe tu nombre")
    page.add(textField_Nombre)








ft.app(target=main)