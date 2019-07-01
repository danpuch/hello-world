


def carga_datos():
    alumnos={}
    for i in range(3):
        dni=int(input("Numero identidad: "))
        valores=[]
        nmat=int(input("Cuantas materias cursas?: "))
        for i in range(nmat):
            materia=input("Nombre de materia: ")
            nota=int(input("Nota: "))
            valores.append((materia, nota))
        alumnos[dni]=valores
    return alumnos

def imprimir(alumnos):
    print(alumnos)


alumnos=carga_datos()
imprimir(alumnos)
