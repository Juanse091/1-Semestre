x=1
b=0
cont=0
x=0
num=0
n=int(input("Favor ingresar cuantas materias desea sacarle el promedio: "))
for x in range(n+1):
    name=input("Nombre de la materia: ")
    notes=int(input("Cuantas notas a promerdiar: "))
    for i in range(notes):
        num=num+1
        a=float(input(f"ingrese la nota {num}: "))
        b=a+b
        if num == notes:

         prom=b/num
         print(name, prom)