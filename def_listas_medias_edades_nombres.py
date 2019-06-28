'''carga 5 nombres de personas y sus edades por teclado.
imprimir nombre de personas mayores de edad (>=18
imprimir edad promedio de las personas
'''


def cargaDatos():
    name=[]
    ed=[]
    for i in range(5):
        nam=input("Ingrese nombre: ")
        name.append(nam)
        edad = int(input("Edad: "))
        ed.append(edad)
    return [name, ed]

def mayor_18 (name, ed):
    mayor = []
    for i in range(len(name)):
        if ed[i]>=18:
            mayor.append(name[i])
    return mayor

def promedio(ed):
    suma = 0
    for i in range(len(ed)):
        suma += ed[i]
    promed = suma / len(ed)
    return promed

nombres, edades = cargaDatos()

print("****************EXITO***************")
print("Los mayores de 18 años son: ", mayor_18(nombres, edades))
print("El promedio de edad es: ", promedio(edades))
print("****************EXITO***************")
