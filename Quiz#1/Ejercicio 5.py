#Un programa que pida al usuario un número y que diga si el número es mayor, menor o igual a cero.
num1=int(input("Favor escribir un número:"))
if num1<0:
        print(f"El número {num1} es menor que cero")
elif num1>0:
        print(f"El número {num1} es mayor que cero")
elif num1==0: 
        print(f"El número {num1} es igual que cero")