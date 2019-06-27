actual=int(input("Ano actual: "))

ficha=[]

for i in range(3):
    name=input("Nombre: ")
    year=int(input("Born in: "))
    ficha.append((name,year))

print(ficha)

for i in ficha:
    for name, year in i:
        print(name, year)
