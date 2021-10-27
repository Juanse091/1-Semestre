print("Favor ingresar el estudiante 1 sus notas: ")
n1_1=float(input("Nota 1: "))
n1_2=float(input("Nota 2: "))
n1_3=float(input("Nota 3: "))

n1_1 =(n1_1) * 0.30 
n1_2 =(n1_2) * 0.30 
n1_3 =(n1_3) * 0.40 

n1 = n1_1 + n1_2 + n1_3 

if n1 < 2.0:
    print("El primer estudiante no puede habilitar")
elif n1 < 3.0:
    print("El primer estudiante reprobo")
elif n1 >= 3.0:
    print("El primer estudiante aprobo")
elif n1 > 4.5:
    print("Felicidades al primer estudiante aprobo con exitos")

#ESTUDIANTE 2
print("Favor ingresar el estudiante 2 sus notas: ")
n2_1=float(input("Nota 1: "))
n2_2=float(input("Nota 2: "))
n2_3=float(input("Nota 3: "))

n2_1 =(n2_1) * 0.30 
n2_2 =(n2_2) * 0.30 
n2_3 =(n2_3) * 0.40 

n2 = n2_1 + n2_2 + n2_3

if n2 < 2.0:
    print("El segundo estudiante no puede habilitar")
elif n2 < 3.0:
    print("El segundo estudiante reprobo")
elif n2 >= 3.0:
    print("El segundo estudiante aprobo")
elif n2 > 4.5:
    print("Felicidades al segundo estudiante aprobo con exitos")


#ESTUDIANTE 3
print("Favor ingresar el estudiante 3 sus notas: ")
n3_1=float(input("Nota 1: "))
n3_2=float(input("Nota 2: "))
n3_3=float(input("Nota 3: "))

n3_1 =(n3_1) * 0.30 
n3_2 =(n3_2) * 0.30 
n3_3 =(n3_3) * 0.40 

n3 = n3_1 + n3_2 + n3_3

if n3 < 2.0:
    print("El tercer estudiante no puede habilitar")
elif n3 < 3.0:
    print("El tercer estudiante reprobo")
elif n3 >= 3.0:
    print("El tercer estudiante aprobo")
elif n3 > 4.5:
    print("Felicidades al tercer estudiante aprobo con exitos")


#ESTUDIANTE 4
print("Favor ingresar el estudiante 4 sus notas: ")
n4_1=float(input("Nota 1: "))
n4_2=float(input("Nota 2: "))
n4_3=float(input("Nota 3: "))

n4_1 =(n4_1) * 0.30 
n4_2 =(n4_2) * 0.30 
n4_3 =(n4_3) * 0.40 

n4 = n4_1 + n4_2 + n4_3

if n4 < 2.0:
    print("El cuarto estudiante no puede habilitar")
elif n4 < 3.0:
    print("El cuarto estudiante reprobo")
elif n4 >= 3.0:
    print("El cuarto estudiante aprobo")
elif n4 > 4.5:
    print("Felicidades al cuarto estudiante aprobo con exitos")


#ESTUDIANTE 5
print("Favor ingresar el estudiante 5 sus notas: ")
n5_1=float(input("Nota 1: "))
n5_2=float(input("Nota 2: "))
n5_3=float(input("Nota 3: "))

n5_1 =(n5_1) * 0.30 
n5_2 =(n5_2) * 0.30 
n5_3 =(n5_3) * 0.40 

n5 = n5_1 + n5_2 + n5_3

if n5 < 2.0:
    print("El quinto estudiante no puede habilitar")
elif n5 < 3.0:
    print("El quinto estudiante reprobo")
elif n5 >= 3.0:
    print("El quinto estudiante aprobo")
elif n5 > 4.5:
    print("Felicidades al quinto estudiante aprobo con exitos")

numeros = [n1, n2, n3, n4, n5]

ordenados = sorted(numeros, reverse=True)
    
# Imprimir el resultado
print("los promedios ordenados de mayor a menor", ordenados)