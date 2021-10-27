Suma = 0
I = 0
Cantidad = 0
n=int(input("Favor ingresar un número: "))

while n!=0:
    Cantidad = Cantidad + 1
    Suma = Suma + n
    I= I + 1
    n=int(input("Favor ingresar un número: "))

Media = Suma / I
print(f"La sumatoria de los valores ingresados es",Suma)
print(f"El promedio de los valores ingresados es",Media)
print(f"La cantidad de los valores ingresados es",Cantidad)
