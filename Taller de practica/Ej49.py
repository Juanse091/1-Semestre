# n numeros
n= int(input("Ingrese cuantos números desea promediar y sumar: "))
x=0
list = []
suma=0
for i in range(n):
    x+=1
    num= float(input(f"Ingrese el número {x}: "))
    list.append(num)
for i in list:
    suma += i
print(f"Los números ingresados son los siguientes -> {list}")
print(f"La suma de todos los números es: {int(suma)}")
print(f"El promedio de los números ingresados es: {suma/n}")
