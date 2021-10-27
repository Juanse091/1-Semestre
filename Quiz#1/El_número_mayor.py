# Vamos a poner los números en una lista
numeros = []

# Le agregamos 5 números
for i in range(5):
  numero = float(input("Introduce el número #{}: ".format(i + 1)))
  numeros.append(numero)

ordenados = sorted(numeros, reverse=True)
    
# Imprimir el resultado
print(ordenados)


