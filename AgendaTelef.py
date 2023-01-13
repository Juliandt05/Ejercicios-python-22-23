'''
Opcion 1:
Lista para nombres 
Lista para teléfonos

Opcion 2:
Lista para nombres y teléfonos
Ejemplo [Juan - Teléfono, Pepe - Teléfono]
'''

#Opción 1
vNombre=[]
vTelefonos=[]

'''
1- Insertar contacto
2- Borrar contacto
3- Buscar contacto
4- Ver todos los contactos
5- Salir
'''


def pintaMenu():
    opc=0
    while (opc<1 or opc>5):
        print("###### MENÚ AGENDA #######")
        print("1- Insertar contacto")
        print("2- Borrar contacto")
        print("3- Buscar contacto")
        print("4- Ver todos los contactos")
        print("5- Salir")
        print ("#########################")
        try:
            opc=int("Dime el número",input())
        except:
            print("Las opciones son de la 1 a la 5")
    return opc

opc=pintaMenu()
while(opc!=5):
    opc=pintaMenu()


import flet as ft

def main(page: ft.Page):
    page.title = "DropdownMenu Equipos"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    Dropdown_Equipos=ft.Dropdown(width=300,options=[ft.dropdown.Option("Rayo Fuentealvilla")],label="Equipos")
    Dropdown_Equipos.options.append(ft.dropdown.Option("Depor"))
    Dropdown_Equipos.options.append(ft.dropdown.Option("Leganés"))
    Dropdown_Equipos.options.append(ft.dropdown.Option("Real Zaragoza"))
    Dropdown_Equipos.options.append(ft.dropdown.Option("Borusia Mochenglasbach"))
    page.add (Dropdown_Equipos)

ft.app(target=main)