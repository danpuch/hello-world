'''Agenda.
Clave = fecha
valores= hora y actividad
1.carga de datos en agenda
2.listado completo de la agenda
3.consulta de una fecha'''

def my_data():
    agenda={}
    again='y'
    while again == 'y':
        date=input("Introduce la fecha actual [dd/mm/aa]:")
        again2='y'
        lday=[]
        while again2 == 'y':
            hour=input("Hora:")
            activity=input("Actividad:")
            lday.append((hour, activity))
            again2=input("Do you want to add a new activity for this day? [y/n]:")
        agenda[date]=lday
        again=input("Do you want to add a new entry? [y/n]:")
    return agenda

def imprimir_agenda(agenda):
    print("El contenido de la agenda es el siguiente: ")
    for elem in agenda:
        print("Para la fecha: ", elem)
        for hora, actividad in agenda[elem]:
            print(hora, actividad)

def filtro_fecha(agenda):
    again='y'
    while again=='y':
        fecha= input("Que fecha quieres ver? [dd/mm/aa]: ")
        if fecha in agenda:
            for hora, actividad in agenda[fecha]:
                print(hora, actividad)
            again=input("Quieres filtrar otra fecha?")
        else:
            print("No se encuentra actividad en esta fecha.")
            again=input("Quieres filtrar otra fecha?")




#bloque principal

agenda=my_data()
imprimir_agenda(agenda)
filtro_fecha(agenda)