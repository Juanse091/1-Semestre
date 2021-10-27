#Elevar un número al cuadrado
print("Inicio del programa") #Imprimimos en pantalla el inicio del programa
def elevado(num): #Creamos una función llamada elevado
    num = num ** 2 #Hacemos la respectiva operación
    return num #Regresamos el valor hallado
n= int(input("Ingrese el numero al cual quiere elevar al cuadrado: ")) #Le pedimos al usuario que ingrese el número a elevar
print(f"{n} al cuadrado es",elevado(n)) #Imprimimos el resultado
print("Fin del programa") #Imprimimos en pantalla el final del programa
