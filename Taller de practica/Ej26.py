#Promdio de notas
print("Inicio del programa")

n1= float(input("Ingrese la nota 1: "))
n2= float(input("Ingrese la nota 2: "))
n3= float(input("Ingrese la nota 3: "))
n4= float(input("Ingrese la nota 4: "))
n5= float(input("Ingrese la nota 5: "))

prom= ((n1*0.15)+(n2*0.20)+(n3*0.15)+(n4*0.30)+(n5*0.20))
print(f"""
El estudiante tiene un promedio de: {prom}""")

if prom < 2.0:
        print("No podra habilitar")
elif prom < 3:
        print("Reprobo")
elif prom >= 3 and prom < 4.5:
        print("Aprobó")
elif prom > 4.5:
        print("Felicitaciones")

