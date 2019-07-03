capitulos=["Capitulo_1\n","Capitulo_2\n","Capitulo_3\n","Capitulo_4\n","Capitulo_5\n"]
print(capitulos)


file1 = open('test.txt', 'w')
file1.writelines(capitulos)

file1.write("\n\t-Titulo del archivo \n")
file1.write("We add a new Line in the file!\n")
file1.write("The second line in the file!\n")
file1.write("And the last line in the file.")
print(file1)

file1.close()
print("Esta cerrado ahora?: ", file1.closed)