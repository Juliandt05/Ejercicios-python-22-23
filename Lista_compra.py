#Nombre cliente
#Numero de productos
import flet as ft



vlista=[]

def main(page: ft.Page):
    
    page.title="Frutería"
    def añadirelemento(e):
        vlista.append(textField_Nombre.value)
        vlista.append (textField_Apellido.value)
        vlista.append(dropDown_Menu.value)
        vlista.append(slider_carne.value)
        vlista.append(dropDown_Menu2.value)
        vlista.append(slider_verdura.value)
        vlista.append(dropDown_Menu3.value)

    
        textField_Datos.value=vlista
        print(vlista)
        textField_Nombre.value=""
        textField_Apellido.value=""
        dropDown_Menu.value=""
        dropDown_Menu2.value=""
        dropDown_Menu3.value=""
        slider_carne.value=0
        slider_verdura.value=0

        page.update()
    
    
    img=ft.Image(src="https://frutasmontijo.com/wp-content/uploads/2018/10/fruterias.jpg",width=200,height=200)
    page.add(img)
    
    #Componente tetxo
    t=ft.Text(value="Introducción a flet",color="light blue",size=20)

    page.add(t) # add hace dos cosas 1-Añadir 2-Actualizar

    t.value="Lista de alimentos"
    page.update()
    #page update actualiza los datos
    #componente boton
    
    textField_Nombre=ft.TextField(label="Nombre",hint_text="Escribe tu nombre")
    textField_Apellido=ft.TextField(label="Apellido",hint_text="Escribe tu apellido")
    fila=ft.Row(controls=[textField_Nombre,textField_Apellido])
    page.add(fila)
    
    #page.add(textField_Nombre)

    dropDown_Menu= ft.Dropdown(width=300,options=[ft.dropdown.Option("Ternera")],label="Carnes")
    dropDown_Menu.options.append(ft.dropdown.Option("Cerdo 2€/g"))
    dropDown_Menu.options.append(ft.dropdown.Option("Pollo"))
    page.add(dropDown_Menu)
    slider_carne=ft.Slider(min=0,max=2000,divisions=2000,label="Gramos:{value} g")
    page.add(slider_carne)

    dropDown_Menu2= ft.Dropdown(width=300,options=[ft.dropdown.Option("Lechuga")],label="Verdura")
    dropDown_Menu2.options.append(ft.dropdown.Option("Brocoli"))
    dropDown_Menu2.options.append(ft.dropdown.Option("Zanahorias"))
    page.add(dropDown_Menu2)
    slider_verdura=ft.Slider(min=0,max=2000,divisions=2000,label="Gramos:{value} g")
    page.add(slider_verdura)

    dropDown_Menu3= ft.Dropdown(width=300,options=[ft.dropdown.Option("Huevos")],label="Otros")
    dropDown_Menu3.options.append(ft.dropdown.Option("Leche"))
    dropDown_Menu3.options.append(ft.dropdown.Option("Agua"))
    page.add(dropDown_Menu3)

    

    textField_Datos=ft.Text("Aqui apareceran los datos")
    page.add(textField_Datos)
    
    bt=ft.ElevatedButton(text="Confirmar compra",on_click=añadirelemento)
    page.add(bt)
    
    
    

ft.app(target=main)