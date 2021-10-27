#Promdio de notas
print("Inicio del programa")
cont= 0
x=1
num=[]  
while cont !=5:
    cont+=1
    n= float(input(f"Ingrese la nota {cont}: "))
    num.append(n)
prom= ((num[0]*0.15)+(num[1]*0.20)+(num[2]*0.15)+(num[3]*0.30)+(num[4]*0.20))
print(f"""
El estudiante tiene un promedio de: {prom}""")

if prom < 2.0:
    print("No podra habilitar")
elif prom < 3:
    print("Reprobo")
elif prom >= 3 and prom < 4.5:
    print("Aprobó")
else:
    print("Felicitaciones")