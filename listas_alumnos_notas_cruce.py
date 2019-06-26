#Ingresar nombre y nota de 4 alumnos
#lista con nombre, nota y condicion de alumno
#muy bueno si nota >=8
#bueno si nota entre 4 y 7
#insificiente si nota <4
#imprimir los alumnos que tienen muy bueno

lista_alumnos = []
lista_notas = []

for i in range(4):
    name = input("Ingresa tu nombre: ")
    lista_alumnos.append(name)
    nota = float(input("Ingresa tu nota: "))
    lista_notas.append(nota)

contador=0
for i in range (4):
    print("Nombre: ",lista_alumnos[i])
    print("Nota: ", lista_notas[i])
    if lista_notas[i]>= 8:
        print("Condicion: Muy Bueno." )
        contador +=1
    elif 4< lista_notas[i] <8:
        print("Condicion: Bueno.")
    else:
        print("Insuficiente")

print("Los alumnos con condicion 'Muy bueno' son:", contador)