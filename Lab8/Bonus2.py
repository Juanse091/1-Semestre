list=[]
x=int(input("Cuantos valores desea enlistar: "))

for i in range(x):
    num=int(input("Ingrese un valor: "))
    list.append(num)

print("El número menor de los enlistados es: ",min(list))
