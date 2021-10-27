#Área de un hexágono
print("Inicio del programa")
peri= float(input("Ingresar el perimetro del herxagono: "))
ap= float(input("Ingresar el apotema del herxagono: "))

area= peri*ap/2
a=("{0:.2f}".format(area))
print(f"El área del herxágono es: {a}cm²")
print("Fin del programa")