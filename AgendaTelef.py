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
            opc=int(input())
        except:
            print("Las opciones son de la 1 a la 5")
    return opc


pintaMenu()

   
#Muy bien Julian, bien hecho, como bien te indique yo, tu maestro y querido profesor Julio. Un saludos y un besito. Saludos desde Corea del Norte.