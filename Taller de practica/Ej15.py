#Distancia entre dos coordenadas
import math

print("Inicio del programa")
x1= float(input("Ingresar la coordenada x1: "))
y1= float(input("Ingresar la coordenada y1: "))
x2= float(input("Ingresar la coordenada x2: "))
y2= float(input("Ingresar la coordenada y2: "))

d=  math.sqrt((x2-x1)**2+(y2-x1)**2)

print(f"La distancia entre los dos puntos es: {d}")

print("Fin del programa")
