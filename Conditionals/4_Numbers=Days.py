num_dia= int(input("Favor seleccionar un número del 1 al 7:"))

while num_dia > int(7) or num_dia < int(1):
        print("Error.. Introducir un número entre 1 y 7")
        num_dia= int(input("Favor seleccionar un número del 1 al 7"))
        print("")
if num_dia == 1:
        print("La equivalencia del número en días de la semana es: Lunes")
elif num_dia == 2:
        print("La equivalencia del número en días de la semana es: Martes")
elif num_dia == 3:
        print("La equivalencia del número en días de la semana es: Miercoles")
elif num_dia == 4:
        print("La equivalencia del número en días de la semana es: Jueves")
elif num_dia == 5:
        print("La equivalencia del número en días de la semana es: Viernes")
elif num_dia == 6:
        print("La equivalencia del número en días de la semana es: Sabado")
elif num_dia == 7:
        print("La equivalencia del número en días de la semana es: Domingo") 