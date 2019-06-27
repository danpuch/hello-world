''''''
curso=int(input("Introduce the current year: "))
lnom=[]
for i in range(3):
    nombre=input("Nombre: ")
    naci=int(input("Ano nacimiento: "))
    lnom.append((nombre, naci))
    for name, age in lnom:
        print(name, "tiene ", curso-age)
