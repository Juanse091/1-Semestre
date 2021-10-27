import math
print("Favor digite 4 número")

a= int(input("Número 1: "))
b= int(input("Número 2: "))
c= int(input("Número 3: "))
d= int(input("Número 4: "))

Avrg= int(a+b+c+d)/4

if Avrg >= 11.5:
    print("Aprovado")
else:
    print("Desaprovado")