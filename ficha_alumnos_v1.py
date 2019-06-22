'''Se desea almacenar los datos de 3 alumnos.
Definir un diccionario cuya clave sea el número de documento del alumno.
Como valor almacenar una lista con componentes de tipo tupla donde almacenamos
 nombre de materia y su nota.

Crear las siguientes funciones:
1) Carga de los alumnos (de cada alumno solicitar su dni y los nombres de
las materias y sus notas)
2) Listado de todos los alumnos con sus notas
3) Consulta de un alumno por su dni, mostrar las materias que cursa y
sus notas.'''

#definicion de funciones:

def my_data():
    ficha={}
    again='y'
    while again=='y':
        dni=int(input("Introduce DNI del alumno:"))
        again2='y'
        lficha=[]
        while again2=='y':
            asignatura=input("Asignatura:")
            nota=int(input("Nota:"))
            lficha.append((asignatura,nota))
            again2=input("Do you want to add more materias? [y/n]:")
        ficha[dni]=lficha
        again=input("Do you want to add more students? [y/n]:")
    return ficha

def imprimir_ficha(ficha):
    print("**********IMPRIMIMOS FICHA DE ALUMNOS************")
    for elem in ficha:
        print("DNI del alumno", elem)
        for asig, nota in ficha[elem]:
            print(asig, nota)

def filtro_alumno(ficha):
    print("**********BUSCA ALUMNOS************")
    again=input("Quieres buscar algun alumno? [y/n]:")
    while again=='y':
        dni=int(input("Introduce el DNI del alumno a buscar:"))
        if dni in ficha:
            print("El alumno con DNI", dni, "tiene las siguientes asignaturas:")
            for asig, nota in ficha[dni]:
                print("Asignatura: ", asig, "// Nota: ", nota)
            again=input("Quieres buscar nuevamente? [y/n]:")
        else:
            print("No hay resultados")
            again=input("Quieres buscar nuevamente? [y/n]:")
    print("HASTA PRONTO")

#bloque principal

ficha=my_data()
imprimir_ficha(ficha)
filtro_alumno(ficha)






#bloque principal





#35