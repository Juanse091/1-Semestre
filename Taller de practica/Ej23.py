#Par o impar + positivo o negativo
num = int(input("Ingrese un número entero: "))
if num % 2 == 0 and num >= 0:
    print(f"{num} es un par positivo")
elif num % 2 == 0 and num < 0:
    print(f"{num} es un par negativo")

elif num % 2 != 0 and num >= 0:
    print(f"{num} es un impar positivo")
else:
    print(f"{num} es un impar negativo")
    