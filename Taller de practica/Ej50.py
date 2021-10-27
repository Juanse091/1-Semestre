# Prom Par e Impar
nums=input("De un rango de números(Enteros), separados por una coma(,): ")
nums=nums.split(",")
n1= int(nums[0])
n2= int(nums[1])
#VARIABLES
CountPar=0
CountImpar=0
par = []
sumpar=0
impar = []
suimpar=0
x=0
np1=n1
#INICIO PAR O IMPAR
print(f"Rango de los números ingresados {n1} a {n2}")
if n1 % 2 == 0:
    while n1 <= n2:
        CountPar+=1
        n1+=2
        par.append(n1)
    for i in par:
        sumpar += i
    print(f"""Suma de pares = {sumpar}
Promedio de pares = {sumpar/(CountPar)}""")
elif n1 % 2 != 0:
    while n1 <= n2:
        CountImpar+=1
        print(n1)
        impar.append(n1)
        n1+=2
    for i in impar:
        suimpar += i
    print(f"""Suma de impares = {suimpar}
Promedio de impares = {suimpar/(CountImpar)}""")
np1 = np1 + 1
if np1 % 2 == 0:
    while np1 <= n2:
        CountPar+=1
        par.append(np1)
        np1+=2
    for i in par:
        sumpar += i
    print(f"""Suma de pares = {sumpar}
Promedio de pares = {sumpar/(CountPar)}""")
elif np1 % 2 != 0:
    while n1 <= n2:
        CountImpar+=1
        n1+=2
        impar.append(np1)
    for i in impar:
        suimpar += i
    print(f"""Suma de impares = {suimpar}
Promedio de impares = {suimpar/(CountImpar)}""")

