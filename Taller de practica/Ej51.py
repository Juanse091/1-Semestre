#Value Error
x=0
while x== 0:
    try:
        n= int(input("Ingrese un número entero: ")) 
        if n > 0:
            print(f"El número {n} es un número positivo")
            break
    
        else:
            print("Error, Ingrese nuevamente un número")
            continue
    
    except ValueError:
        print("El dato ingresado es invalido")