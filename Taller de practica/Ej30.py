#Suma del primer y segundo número mayor que el tercero?
print("Inicio del programa")
n1= int(input("Ingrese el primer valor: "))
n2= int(input("Ingrese el segundo valor: "))
n3= int(input("Ingrese el tercer valor: "))

sum = n1 + n2
print("La suma del primer y segundo valor es:",sum)
if sum > n3:
    print("La suma del primer y segundo valor es mayor que el tercer valor")
elif sum == n3:
    print("La suma del primer y segundo valor es igual que el tercer valor")
else:
    print("La suma del primer y segundo valor es menor que el tercer valor")
print("Fin del programa")

