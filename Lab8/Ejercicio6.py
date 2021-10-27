def factorial(num):
    f=1
    if num!=0:
        for i in range(1,num+1):
         f=f*i
    return f

cont=0
number=int(input("Ingrese un número, si quiere terminar ingrese un -1 para cortar: "))
while number!=-1:
    print("Factorial:", factorial(number))
    cont+=1
    number=int(input("Ingrese un número, si quiere terminar ingrese un -1 para cortar: "))
print("Se leyeron",cont,"números ingresados")