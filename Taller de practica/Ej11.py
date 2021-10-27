#Caída libre
import math
print("Inicio del programa")

h= float(input("Ingrese la altura en metros desde donde se suelta el objeto: "))
t= math.sqrt(2*h/9.8)
t=("{0:.2f}".format(t))
print(f"Tiempo de caída= {t}seg")
print("Fin del programa")
