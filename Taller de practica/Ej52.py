# x<100 or x>100
n= int(input("Íngrese cuantos números desee evaluar: "))
listM=[]
listm=[]
cont=n+1
for i in range(n):
    num= int(input(f"Ingrese número {i+1}: "))
    if num >= 100:
        listM.append(num)
    else:
        listm.append(num)
print(f"""Números mayores a 100: {listM}
Números menores a 100: {listm}""")
