'''Diccionarios como listas, tuplas y diccionarios.
Codigo: de producto como clave
valores: nombre, precio, cantidad stock
 1.carga datos de diccionario
 2.listado completo de productos
 3.consulta de producto por su clave y mostrar nombre, precio y stock
 4.filtro de productos con valor stock 0'''

def my_data():
    database= {}
    new = 'y'
    while new == 'y':
        code=int(input("Introduce the code: "))
        name=input("Description:")
        price=float(input("Price:"))
        stock=int(input("Stock: "))
        database[code]=(name, price, stock)
        new=input("Do you want to add more products?[y/n]:" )
    return database

def mostrar_productos(database):
    print("Current products: ")
    for elem in database:
        print("********************")
        print(elem, " //  Description: " , database[elem][0], " //  Price:", database[elem][1], "//  Stock:", database[elem][2])

def filtro_productos(database):
    new='y'
    while new == 'y':
        search=int(input("Introduce el codigo a mostrar: "))
        if search in database:
            print(search, database[search][0], database[search][1], database[search][2])
            new=input("Do you want to search again?:")
        else:
            print("The product is not on the list.")
            new=input("Do you want to search again?:")

def stock_productos(database):
    print("Los productos que no tienen stock son: ")
    for elem in database:
        if database[elem][2]==0:
            print(database[elem][0])

#bloque principal

database=my_data()
mostrar_productos(database)
filtro_productos(database)
stock_productos(database)