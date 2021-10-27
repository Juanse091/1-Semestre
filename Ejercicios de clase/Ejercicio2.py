n=[]
for i in range(5):
    numero = float(input("Introduce el número #{}: ".format(i + 1)))
    n.append(numero)

ordenados = sorted(n, reverse=True)
    
# Imprimir el resultado
print(n[0],n[5])
