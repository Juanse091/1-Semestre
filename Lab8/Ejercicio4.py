#Algoritmo que cálculo mediante booleano si es o no primo.
cond = "si" 
def primo(num): 
    for i in range(2,num):

        if num%i==0:
            return False
    return True
while cond == "si":
    x=int(input("Ingrese un número entero: "))
    if x == 1 or x == 0:
        print("No es primo")
        continue
    if primo(x):
        print("Es primo")
    else:
        print("No es primo")
    if cond == "no":
        print("Hasta luego, vuelva pronto.")
