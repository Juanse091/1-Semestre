#Números fubonacci

#Se asignan valores a las variables
a,b = 0,1

#Se le pide al usuario que ingrese la cantidad de números  
#para el rango delalgoritmo
n = int(input("Ingresar la cantidad de números: "))

#Se ejecuta el for in range, donde se suma a + b y a va tomando el valor de b
for i in range(n+1):
    print(i,"]", a)
    a,b =b,a+b