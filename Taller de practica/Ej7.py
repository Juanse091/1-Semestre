#área y perimetro de un circulo
print("Inicio del programa")
r= float(input("Ingresar el radio del circulo: "))

perimeter= 2*3.14159265359*r
area= 3.14159265359*r**2
a=("{0:.3f}".format(area))
p=("{0:.3f}".format(perimeter))
print(f"""El area del circulo es {a}cm²
El perimetro del circulo es {p}cm""")
print("Fin del programa")