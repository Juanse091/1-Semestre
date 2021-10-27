#Suma, resta, multiplicación, división y residuo de dos valores dados
print("Inicio del programa") #Imprimimos en pantalla el inicio del programa

n=float(input("Ingrese el primer valor a sumar: ")) #Le pedimos al usuario que ingrese el primer valor a sumar
n2= float(input("Ingrese el segundo valor a sumar: ")) #Le pedimos al usuario que ingrese el segundo valor a sumar

#Hacemos las operaciones matemáticas
sum = n + n2  
rest= n - n2  
multipli= n * n2 
divi= n / n2  
residuo= n % n2  

print(f"""Suma={sum}  
Resta={rest}
Multiplicación={multipli}
División={divi}
Residuo={residuo}""") #Imprimimos todos los restulados como si fuera una lista
print("Fin del programa") #Imprimimos en pantalla el final del programa
