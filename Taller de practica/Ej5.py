#Imprimir un número decimal con su respectiva parte entera
print("Inicio del programa") #Imprimimos en pantalla el inicio del programa
num=float(input("Ingrese un número decimal: "))
print(f"""Parte entera: {int(num)} 
Parte decimal: {num%int(num)}""")
print("Fin del programa") #Imprimimos en pantalla el final del programa
