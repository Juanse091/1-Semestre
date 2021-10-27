#divir en sus factores
n=int(input("Ingrese un número: "))
x=0
cont=0
print("El número es divisible en:")
while cont!=n:
    cont=cont + 1
    if n % cont == 0:
        print(cont)
