age=int(input("Introduzca la edad del piloto: "))

if age<int(18):
    print("El piloto es muy joven")
    exit()

elif age>=int(65):
    print("El piloto es muy viejo")
    exit()

ft=input("¿Realizo un vuelo nacional? ")
anf='a'
anf2='b'
inter=int(0)
nac=int(0)
km1=int(0)
km2=int(0)

#Condicional si sí tuvo un vuelo nacional
if ft.lower()=='si':
    nac=1
    km1=int(input("Ingrese la distancia del vuelo en kilometros: "))
    anf=input("¿Realizo algún otro vuelo nacional?: ")
    while anf.lower()=='si':
        nac=1+nac
        km1=int(input("Ingrese la distancia del vuelo en kilometros: ")) + km1
        anf=input("¿Realizo algún otro vuelo nacional?: ")
#Condicional si no tuvo un vuelo nacional
anf2=input("¿Realizo algún vuelo internacional?: ")
if anf2.lower()=='si':
    inter=1
    km2=int(input("Ingrese la distancia del vuelo en kilometros: "))
    anf2=input("¿Realizo algún otro vuelo internacional?: ")
    while anf2.lower()=='si':
        inter=1+inter
        km2=int(input("Ingrese la distancia del vuelo en kilometros: ")) + km2
        anf2=input("¿Realizo algún otro vuelo internacional?: ")

km=km1+km2

if int(18)<=age<=int(50):
    fh=float(km/int(893))
elif int(50)<age<int(65):
    fh=float(km/int(893)*(1.20))

tf=input("¿Realizo un vuelo el dia anterior?: ")
nf='c'

if tf.lower()=='si':
    nf=input("¿Su siguiente vuelo sera internacional?: ")
elif tf.lower()=='no':
    tfh=fh+nac+inter*2

if nf.lower()=='si':
    tfh=fh+nac+inter*2+1
elif nf.lower()=='no':
    tfh=fh+nac+inter*2

if tfh<=int(40):
    print("El piloto aun puede volar, le quedan aproximadamente,",round(int(40)-tfh),"horas de vuelo")
else:
    print("El piloto no puede volar, sobrepaso su limite de horas aproximadamente por,",round(tfh-int(40)),"horas de vuelo")