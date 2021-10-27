#Promedio de 3 números
print("Inicio del programa")
cont=0
a=0
num= int(input("Cantidad de números a promediar: "))
for i in range(num): #Creamos un bucle para que el programa pregunte al usuario 3 veces lo mismo
    cont+=1
    n= int(input(f"Ingrese el número {cont}: "))
    suma=a+n
    a=suma
prom=suma/3
print(f"Promedio de los números ingresados: {prom}")
print("Fin del programa")
