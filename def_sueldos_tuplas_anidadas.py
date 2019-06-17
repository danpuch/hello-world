'''lista de 5 elementos nombres de empleados con sus 3 sueldos (valores en tupla)
1. carga nombres de mpleados y sus tres sueldos
2. print monto total cobrado por empleado
3. print nombres de empleados que con ingreso trimestral mayor a 10.000 en tres meses.
Animo!!!'''

def cargas_datos():
    casablanca = []
    for i in range(5):
        name_emp=input("Ingresa nombre de empleado:")
        salary1=int(input("Primer sueldo: "))
        salary2=int(input("Segundo sueldo: "))
        salary3=int(input("Tercer sueldo: "))
        casablanca.append((name_emp, (salary1, salary2, salary3)))
    return casablanca

def promedio(lista):
    prom_salary=[]
    for i in range(len(lista)):
        sumame = lista[i][1][0]+lista[i][1][1]+lista[i][1][2]
        prom_salary.append((lista[i][0], sumame))
    return prom_salary

def mayor_que(lista1):
    lista_mayor=[]
    for i in range(len(lista1)):
        if lista1[i][1]>10000:
            lista_mayor.append(lista1[i][0])
    print("Los que han cobrado mas de 10.000 € son: ", lista_mayor)

lista=cargas_datos()
lpromedio=promedio(lista)

print(lpromedio)
mayor_que(lpromedio)