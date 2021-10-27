# 10 nums
x= 0
list= []
print ("A continuación debes ingresar 10 números:")
print("-------------------------------------------")
suma = 0
while x != 10:
    x= x+1
    n= float(input(f"Ingrese el número {x}: "))
    list.append(n)
for i in list:
    suma += i
print(f"Los números ingresados son los siguientes -> {int(list)}")
print(f"La suma de todos los números es: {int(suma)}")
print(f"El promedio de los números ingresados es: {suma/10}")