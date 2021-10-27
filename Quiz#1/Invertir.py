numero = int(input("ingresar un número de 4 cifras: "))
invertido = 0

while numero > 0:
    resto = int(numero) % 10 
    numero = int(numero) / 10
    invertido = invertido * 10 + resto


print(int(invertido))