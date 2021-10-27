#Sumar un número hasta llegar a 10

#Variables
N = 0
Suma = 0

#Operaciones
N = N+1
Suma = Suma+N

if N == 10:
    print(int(Suma))

while N != 10:
    N = N+1
    Suma = Suma+N
print(int(Suma))
