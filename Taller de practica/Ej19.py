#Denomicación de billetes
print ("Inicio del programa")
bill=int(input("Ingrese la cantidad de dinero "))

print("Billetes de:")
if bill % 100000 == 0: # Realizamos condicionales para cada valor del billetes
    print(f"100k: {int(bill/100000)}")
    bill= bill%100000
else:
    print(f"100k: {int(bill/100000)}")
    bill= bill%100000

if bill % 50000 == 0:
    print(f"50k: {int(bill/50000)}")
    bill= bill%50000
else:
    print(f"50k: {int(bill/50000)}")
    bill= bill%50000

if bill % 20000 == 0:
    print(f"20k: {int(bill/20000)}")
    bill= bill%20000
else:
    print(f"20k: {int(bill/20000)}")
    bill= bill%20000

if bill % 10000 == 0:
    print(f"10k: {int(bill/10000)}")
    bill= bill%10000
else:
    print(f"10k: {int(bill/10000)}")
    bill= bill%10000

if bill % 5000 == 0:
    print(f"5k: {int(bill/5000)}")
    bill= bill%5000
else:
    print(f"5k: {int(bill/5000)}")
    bill= bill%5000

if bill % 2000 == 0:
    print(f"2k: {int(bill/2000)}")
    bill= bill%2000
else:
    print(f"2k: {int(bill/2000)}")
    bill= bill%2000

if bill % 1000 == 0:
    print(f"1k: {int(bill/1000)}")
    bill= bill%1000
else:
    print(f"1k: {int(bill/1000)}")
    bill= bill%1000
print("Monedas de:") #Realizamos operaciones para cada valor de monedas
if bill % 500 == 0:
    print(f"500: {int(bill/500)}")
    bill= bill%500
else:
    print(f"500: {int(bill/500)}")
    bill= bill%500

if bill % 200 == 0:
    print(f"200: {int(bill/200)}")
    bill= bill%200
else:
    print(f"200: {int(bill/200)}")
    bill= bill%200

if bill % 100 == 0:
    print(f"100: {int(bill/100)}")
    bill= bill%100
else:
    print(f"100: {int(bill/100)}")
    bill= bill%100

if bill % 50 == 0:
    print(f"50: {int(bill/50)}")
    bill= bill%50
else:
    print(f"50: {int(bill/50)}")
    bill= bill%50
print("Final del programa")