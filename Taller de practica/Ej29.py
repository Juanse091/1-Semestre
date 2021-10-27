#Mayor y menor de una lista
print ("Inicio del programa")
list=[]
x=int(input("Cuantos valores desea enlistar: "))

for i in range(x): #El usuario decide cuantos números entraran a la lista
    num=int(input(f"Ingrese un valor {i+1}: "))
    list.append(num)

print(f"""La lista se compone de los sigientes números:
{list}
El número mayor de los enlistados es: {max(list)}
y el menor es: {min(list)}""")


