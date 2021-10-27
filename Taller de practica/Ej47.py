nums= input("Ingrese el número inicial y final separados por una coman(,): ")
num= nums.split(",")
n= int(num[0])
m = int(num[1])
cont= 0
a= 0
list=[]
if n < m:
    for i in range(m-n):
        n=n+1
        a= n+a
        list.append(n)
    print(list)
    print("La suma de todos los numeros ingresados es: ",a)
else:
    print("El número final es mayor que el inicial")