# Same numbers

num = input("Por favor ingrese 3 números separandolos con comas(,): ")
num = num.split(",")

if int(num[0]) == int(num[1]) == int(num[2]):
    print("Todos los números ingresados son iguales.")

elif int(num[0]) == int(num[1]):
    print("Los dos primeros números ingresados son iguales","("+num[0]+" y "+num[1]+").")

elif int(num[1]) == int(num[2]):
    print("Los dos ultimos números ingresados son iguales","("+num[1]+" y "+num[2]+").")
elif int(num[0]) == int(num[2]):
    print("El primer y ultimo número ingresado son iguales","("+num[0]+" y "+num[2]+").")
else:
    print("Todos los números ingresados son diferentes.")