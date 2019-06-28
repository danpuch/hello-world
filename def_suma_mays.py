cadena=" Hola Nano Como Estas "
cadena.replace(' ','')
cadena.strip()

print(cadena)
letras_mays=0
for i in cadena:
    if i!=i.lower():
        letras_mays+=1
print(letras_mays)