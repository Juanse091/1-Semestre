# m y n

nums= input("Ingrese el número inicial y final separados por una coman(,): ")
num= nums.split(",")
n= int(num[0])
m = int(num[1])
cont= 0
list=[]
if n < m:
    for i in range(m-n):
        n=n+1
        list.append(n)
    print(list)
else:
    print("El número final es mayor que el inicial")