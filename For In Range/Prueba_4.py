y1= int(input("Ingresar el año inicial: "))
y2= int(input("Ingresar el año final: "))
for x in range(y1, y2+1):
    if not x % 10==0:
        continue
    if not x % 4==0:
        continue
    if x % 100!=0 or x % 400 == 0:
        print(x)