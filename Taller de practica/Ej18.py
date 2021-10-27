#Ingresar segundos e imprimir, horas, minutos y segundos
print("Inicio del programa")
import math
seg=float(input("Ingresar la cantidad de segundos: "))
hor= math.trunc(seg/ 3600)
min=math.trunc((seg-hor*3600)/60)
sec= math.trunc(seg-(hor*3600+min*60))

print(f"{hor}:{min}:{sec}")
print("Fin del programa")
