# 10 numeros o 20 veces el 5
print ("Ingresar 10 números pares o 20 veces el 5")
print ("------------------------------------------")
#Contadores
cont=0
contPar=0
contImpar=0
contCinco=0
def Par(n):
    if n % 2 == 0:
        return 1
    return 0
def Impar(n):
    if n % 2 != 0:
        return 1
    return 0
def Cinco(n):
    if n % 5 == 0:
        return 1
    return 0
while x != 10 and x1 != 20:
    n=int(input("Ingrese un número: "))
    cont=cont+1
    x= Par(n)+x
    x1=Cinco(n)+x1
    contPar=Par(n)+contPar
    contImpar=Impar(n)+contImpar
    contCinco=Cinco(n)+contCinco
print(f"""
Se han ingresado una cantidad de {cont} números
La cantidad de números pares fueron: {contPar}
La cantidad de números impares fueron: {contImpar}
La cantidad de cincos fueron: {contCinco}
""")
