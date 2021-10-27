x = input("ingrese un numero de 4 cifras: ")
inv = 0

while x == 0:
    r = x % 10
    x = x / 10
    inv = inv*10 + r

print(inv)