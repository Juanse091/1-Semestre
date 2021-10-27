#Pasaje de un avión
def pasaje(num):
    num = num * 5000
    return num

distance = int(input("¿Distancia a recorrer? "))
days = int(input("¿Número de días de estadia? "))


if days > 7 and distance > 1000:
    print(f"""--------------------------------------------
Se le aplicara un descuento del 15%
El cual equivale a ${pasaje(distance) * 0.15} pesos col""")
    print(f"El total a pagar es de: ${pasaje(distance)-(distance * 0.15)} pesos col")

else:
    print(f"El total a pagar es de: ${pasaje(distance)} pesos col") 
