import math
anw= input("Desea hallar el volumen de un cilindro o la circunferencia de un ciruclo: ")

if anw.lower() == "la circunferencia de un ciruclo":
    r= float(input("favor introducir el radio del circulo: "))
    C= 2*math.pi*r
    print(f"la circunferencia del circulo con radio {r} es = {C} (La formula implementada fue C= 2*pi*r)")

elif anw.lower() == "el volumen de un cilindro":
    r2= float(input("favor introducir el radio del cilindro: "))
    h= float(input("favor introducir la altura del circulo: "))
    V= math.pi*r2**int(2)*h
    print(f"el volumen del cilindro con radio {r2} y altura {h} es = {V} (La formula implementada fue V=pi*r^2*h)")
else:
    print("Dijite bien que es lo que desea hacer")
