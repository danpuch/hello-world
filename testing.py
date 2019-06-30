

def leer_archivo_txt():
    f = open('texto.txt')
    print('archivo: ', f.name)

arch = f.read()

crea_lista(arch)

f.close()
print('cerrado? ', f.closed)


def crea_lista(archivo):
    lista_palabras = []
    letras = 'qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM'
    palabra = ''

for l in archivo:
    if l in letras:
    palabra += l
elif palabra != '':
lista_palabras.append(palabra)
palabra = ''

print(lista_palabras)


leer_archivo_txt()