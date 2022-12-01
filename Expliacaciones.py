#Tipos de datos y variables

#Numéricos
#enteros -- int
#real -- float
#nombre -- str

nombre="Julián"
edad=17
mayorOmenorEdad=False
print (type (mayorOmenorEdad))

#Entrada y salida de datos.
#Salida con print

print ("Buenos dias",nombre, "y tu edad es",edad)

#Entrada de datos -- input()
nombre = input ("Dime tu nombre: \n")
edad= input("Dime tu edad: \n")
print ("Buenos dias",nombre, "y tu edad es",edad)

#Pasar de entero a Caracter 
edad=5
edad_Como_Texto= str(edad)
edad=int(edad_Como_Texto)


print(edad/5)
print(len("Juan"))
edad2=int(input("Dime tu edad: "))



##Bucle while
x=0
while(7<x):
    print("Explicación")
    x=x+1

