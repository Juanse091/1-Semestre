frase=input("Ingrese una frase: ")
print("Las vocales de la frase son: ")

for x in "aeiou":
    if x in frase.lower():
        print(x)