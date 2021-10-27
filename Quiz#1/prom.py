cont=0
p2=0

while cont!=int(5):
    cont=cont+1
    name = input("Ingrese el nombre del estudiante: ")
    n1 = float(input("Ingrese la primera nota: ")) 
    n2 = float(input("Ingrese la segunda nota: "))
    n3 = float(input("Ingrese la tercera nota: "))
    p1= (n1*0.3)+(n2*0.3)+(n3*0.4)
    p2= p2 + p1
    pt= float(p2/5)
    if p1<float(2.0):
        print("El estudiante no puede habilitar")
    elif p1<float(3.0):
        print("El estudiante reprobo")
    elif p1>=float(3.0) and p1<=float(4.5):
        print("El estudiante aprobo")
    elif p1>float(4.5):
        print("Felicitaciones")

if pt>=float(3.5):
    print(pt,"El grupo tuvo un promedio positivo")
else:
    print(pt,"El grupo tuvo un promedio negativo")