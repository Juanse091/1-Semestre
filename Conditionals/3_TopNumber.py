import math

print("Favor digite 3 números:")

a= int(input("Número 1:"))
b= int(input("Número 2:"))
c= int(input("Número 3:"))


if a < b > c:
    print(f"El número {int(b)} es el mayor")

elif b < a > c:
    print(f"El número {int(a)} es el mayor")

elif a < c > b:
    print(f"El número {int(c)} es el mayor")
elif a==b==c:
    print("Todos los números son iguales")