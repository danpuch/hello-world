

file1 = open('test.txt', 'w')
file1.write("\t-Titulo del archivo \n")
file1.write("We add a new line in the file!\n")
file1.write("The second line in the file!\n")
file1.write("And the last line in the file.")
print(file1)
file1.close()