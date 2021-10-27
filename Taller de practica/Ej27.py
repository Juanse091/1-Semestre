list=[]
x=int(input("Cuantos valores desea enlistar: "))

for i in range(x): #El usuario decide cuantos números entraran a la lista
    num=int(input("Ingrese un valor: "))
    list.append(num)

print("El número mayor de los enlistados es: ",max(list))
