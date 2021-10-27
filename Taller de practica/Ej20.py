#Invertir un número
def invet(n):
    numero=0
    while n!=0:
        numero = 10*numero+n % 10
        n//=10
    return numero
num=int(input("Ingresar el número a invertir: "))
print(f"El numero {num} es {invet(num)} invertido")

