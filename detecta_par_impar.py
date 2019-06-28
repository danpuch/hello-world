#identificar si la suma es par o impar:

num1=int(input("Primer numero: "))
num2=int(input("Segundo numero: "))

def par_impar(num1, num2):
    total=num1 + num2
    if total %2 == 0:
        print("La suma de los numeros es par")
    else:
        print("La suma es impar")

par_impar(num1, num2)