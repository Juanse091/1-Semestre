def sumaDigitos(numero):
	suma=0
	for i in range(numero):
	    digito=numero%10
	    suma=suma+digito
	    numero=numero//10
	return suma
num=int(input("Número a procesar, si quiere finalizar ingrese el numero 0: "))
while num!=0:
    print("Suma:",sumaDigitos(num))
    num=int(input("Número a procesar, si quiere finalizar ingrese el numero 0: "))