#Listas en python
vNombre=[]


#Insertar un dato
vNombre.insert(0,"Julio")
vNombre.insert(1,"Álvaro")
vNombre.insert(2,"Rofi")
vNombre.append("Alberto")
vNombre.insert(1,"Jose")

vNombre.remove("Jose")
print("El nombre borrado es"),vNombre.pop(1)

#Ordenar una lista
vNombre.sort(reverse=True)


print(type(vNombre))

#Contar el número de elementos de la lista
print(vNombre.count("Rofi"))
print("La lista tiene", len(vNombre))

