#Denomicación de billetes
print ("Inicio del programa")
bill= (input("Ingrese la cantidad de dinero: "))
bill = bill.split(".")
bill = int("".join(bill))
x=1

while x==1: #Iniciamos un bucle para que se pueda ejecutar mejor el programa
    print("Billetes de:")
    print(f"100k: {int(bill/100000)}")
    bill= bill%100000
    print(f"50k: {int(bill/50000)}")
    bill= bill%50000
    print(f"20k: {int(bill/20000)}")
    bill= bill%20000
    print(f"10k: {int(bill/10000)}")
    bill= bill%10000
    print(f"5k: {int(bill/5000)}")
    bill= bill%5000
    print(f"2k: {int(bill/2000)}")
    bill= bill%2000
    print(f"1k: {int(bill/1000)}")
    bill= bill%1000
    print("Monedas de:") #Realizamos operaciones para cada valor de monedas
    print(f"500: {int(bill/500)}")
    bill= bill%500
    print(f"200: {int(bill/200)}")
    bill= bill%200
    print(f"100: {int(bill/100)}")
    bill= bill%100
    print(f"50: {int(bill/50)}")
    bill= bill%50
    print("Fin del programa")
    break