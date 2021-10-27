print("Inicio de la operación")
def sumaDigitos(numero):
	suma=0
	for i in range(numero):
	    digito=numero%10
	    suma=suma+digito
	    numero=numero//10
	return suma
sumTotal=0
num=int(input("Número a procesar, si desea finalizar ingrese el número 0: "))
while num!=0:
    print("Suma:",sumaDigitos(num))
    sumTotal=sumTotal+num
    num=int(input("Número a procesar, si desea finalizar ingrese el número 0: "))
print("Sumatoria:", sumTotal) 
print("Dígitos:", sumaDigitos(sumTotal)) 
print("Operación terminada")
