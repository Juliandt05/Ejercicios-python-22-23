# Programa para indicar qué camino escoger a spiderman

emer1=int(input("Dime la distancia a la que esta la primera emergencia "))
emer2=int(input("Dime la distancia a la que esta la segunda emergencia "))

if abs(emer1)<abs(emer2):
    print("Ve primero a la primera emergencia","recorreras una distancia de",abs(emer1)*2+abs(emer2),"kilometros")
else:
    print("Ve primero a la segunda emergencia","recorreras una distancia de",abs(emer1)+abs(emer2)*2,"kilometros")