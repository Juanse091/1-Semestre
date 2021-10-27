#Leer cantidad, P, N, Pares, Impares, mult. 8
n= int(input("Íngrese cuantos números desee evaluar: "))
x=0
contP=0
contN=0
contImpar=0
contPar=0
cont8=0
list=[]
def P(n):
    if n>0:
        return int(1)
    return int(0)

def N(n):
    if n<0:
        return int(1)
    return int(0)

def Par(n):
    if n%2==0:
        return int(1)
    return int(0)

def Impar(n):
    if n%2!=0:
        return int(1)
    return int(0)

def M8(n):
    if n%8==0:
        return int(1)
    return int(0)

while x<n:
    x+=1
    num=int(input(f"Ingrese el número {x}: "))
    list.append(num)
    contP=P(num)+contP
    contN=N(num)+contN
    contPar=Par(num)+contPar
    contImpar=Impar(num)+contImpar
    cont8=M8(num)+cont8
print(f"""
Números registrados: {list}
Números positivos: {contP} 
Números negativos: {contN}
Números pares: {contPar}
Números impares: {contImpar}
Números multiplos de 8: {cont8}""")