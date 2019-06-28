
def carga_empleados():

    empleados={}
    for i in range(3):
        name=input("Introduzca su nombre: ")
        sueldo=int(input("Sueldo: "))
        bonificacion=float(input("Bonificación: "))
        asignacion=float(input("Asignación: "))
        empleados[name]=(sueldo, bonificacion, asignacion)
    return empleados

def

print(carga_empleados())