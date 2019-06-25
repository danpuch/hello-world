'''define tupla con 3 valores.
Convertir el contenido de la tupla a lista.
modificar la lista y convertir a tupla. '''


fechatupla1 = (25, 12, 2016)
print("Imprimimos la primera tupla")
print((fechatupla1))
fechalista1 = list(fechatupla1)
print("Imprimimos la listra que se copió de la tupla")
print(fechalista1)
fechalista1[0]=31
print("Imprimimos la lista modificada")
print(fechalista1)
fechatupla2 = tuple(fechalista1)
print("Imprimimos la segunda tupla que se copio de la lista")
print(fechatupla2)