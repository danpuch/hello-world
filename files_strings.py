capitulos='Capitulo_1  Capitulo_2  Capitulo_3  Capitulo_4  Capitulo_5'.split()
print(capitulos)


file1 = open('test.txt', 'w')
file1.writelines(capitulos)

file1.write("\n\t-Titulo del archivo \n")
file1.write("We add a new line in the file!\n")
file1.write("The second line in the file!\n")
file1.write("And the last line in the file.")
print(file1)

file1.close()
print("Esta cerrado ahora?: ", file1.closed)