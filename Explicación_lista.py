#Listas en python
vNombre=[]


#Insertar un dato
vNombre.insert(0,"Julio")
vNombre.insert(1,"Ildefonso Salvador")
vNombre.insert(2,"Leandro")
vNombre.append("Anastasio")
vNombre.insert(1,"Rofi")

vNombre.remove("Anastasio")
print("El nombre borrado es"),vNombre.pop(1)

#Ordenar una lista
vNombre.sort(reverse=True)


print(type(vNombre))

#Contar el número de elementos de la lista
print(vNombre.count("Rofi"))
print("La lista tiene", len(vNombre))