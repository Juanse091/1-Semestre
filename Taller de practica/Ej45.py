#1 -2 3 -3
num= int(input("Enter a number: "))
cont = 0
numeros = []
while cont < num:
    cont += 1
    if cont % 2 == 0:
        cont1 = cont * -1
        numeros.append(cont1)
    else:
        numeros.append(cont)

print(numeros)