#Sumar dos números
print("Inicio del programa") 
def suma(num,num2): #Definimos una función llamada suma
    sum= num+num2 
    return sum #Regresamos el resultado de la suma

n=int(input("Ingrese el primer valor a sumar: ")) 
n2= int(input("Ingrese el segundo valor a sumar: ")) 
print(f"La suma de {n} y {n2} es igual a", suma(n,n2)) 
print("Fin del programa") 

