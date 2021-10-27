a,b=0,1
v=0
n = int(input("Ingresar número de terminos: "))
for i in range(n+1+v):
    print(i,"]", a)
    a,b=b,a+b
