import math as mt
A = int(input("Ingrese la variable a: "))
B = int(input("Ingrese la variable b: "))
C = int(input("Ingrese la variable c: "))

if ((B**2)-4*A*C) < 0:
    print("La solución de la ecuación es con números complejos")
else:
    x1 = (-B+mt.sqrt(B**2-(4*A*C)))/(2*A)
    x2 = (-B-mt.sqrt(B**2-(4*A*C)))/(2*A)
    print("Las soluciones de la ecuación son: ", x1, "y", x2)